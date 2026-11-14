# Azure Storage Accounts without Lifecycle Management Policies

## What It Does

This policy template checks all Azure Storage Accounts that support blob tiering to verify that they have lifecycle management policies enabled. If any are found that do not, an incident is raised with a list of the offending Storage Accounts, a `Recommendation` for each one, and a conservative estimate of the monthly savings that moving their Hot block blobs to the Cool tier could provide. Optionally, an email is sent with this list.

Only `StorageV2` and `BlobStorage` Storage Accounts with a `Standard` SKU support blob tiering. Other Storage Accounts, such as Storage (general purpose v1), `FileStorage`, `BlockBlobStorage`, and Premium SKU accounts, are never reported because there is no reason to recommend a lifecycle management policy for them.

The `Recommendation` is to create a lifecycle management policy for the Storage Account that moves Hot block blobs to the Cool tier after the number of days set in the `Days Until Cool Tier` parameter.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if a lifecycle management policy is created for the Storage Account with a rule that moves Hot block blobs to the Cool tier after the number of days set in the `Days Until Cool Tier` parameter. The `Estimated Monthly Savings` is a conservative lower bound based on the last `Days Until Cool Tier` days of Azure Monitor metrics, and it is calculated for each Storage Account via the following:

- Savings are only estimated for Storage Accounts with a `Standard` SKU redundancy of `LRS`, `GRS`, `RA-GRS`, `ZRS`, `GZRS`, or `RA-GZRS` that do not have a hierarchical namespace. Any other Storage Account that is checked has an `Estimated Monthly Savings` of 0 and a `Savings Note` explaining why no estimate was made. Like any Storage Account with an `Estimated Monthly Savings` of 0, it is only reported if the `Minimum Savings Threshold` is set to 0.
- The following Azure Monitor metrics of the blob service of the Storage Account are collected for the last `Days Until Cool Tier` days:
  - `BlobCapacity` (average) for Hot block blobs. The most recent daily value is the Hot capacity.
  - `BlobCount` (average) for Hot block blobs. The most recent value is the Hot blob count.
  - `Ingress` (total). The total number of bytes written to the Storage Account.
  - `Egress` (total) for the `GetBlob` API. The total number of bytes read from the Storage Account.
- If a metric is not returned for a Storage Account, its value is treated as unknown and not as zero. The Storage Account has an `Estimated Monthly Savings` of 0 and a `Savings Note` stating that the metrics were unavailable, so it is only reported if the `Minimum Savings Threshold` is set to 0. A successful `Ingress` or `Egress` response without any data points means that there was no traffic, and a successful `BlobCapacity` response without any data points means that there is no Hot block blob data.

The amount of Hot data that is eligible to move to the Cool tier is calculated as follows:

```text
hot_gb = hot_bytes / 1024^3
touched_gb = (ingress_bytes + read_bytes) / 1024^3
cold_fraction = clamp(1 - touched_gb / hot_gb, 0, 1)
eligible_gb = hot_gb * cold_fraction
eligible_blobs = hot_blob_count * cold_fraction
```

No more than `touched_gb` of data can have been written or read during the lookback period. Everything else has been untouched for at least `Days Until Cool Tier` days, which means a rule that moves Hot block blobs to the Cool tier after that many days would have moved it. Repeated reads of the same bytes only shrink the amount of data that was touched, so the eligible amount is a floor and not a guess.

The savings are then calculated using the following rates:

- The `effective Hot rate` is the cost of the Hot `Data Stored` usage of the Storage Account over the last 30 full days, as found within Flexera CCO, divided by the Hot capacity in gigabytes. The 30 days end 3 days before the policy runs to allow for delays in billing data. Since the cost is obtained from Flexera CCO, it takes into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If no Hot `Data Stored` cost can be found for the Storage Account in Flexera CCO, the Azure retail Hot rate is used instead, and the `Savings Note` says so. Retail rates do not reflect discounts, so in that case the estimate may be higher than the savings that are actually realized.
- The retail Hot and Cool `Data Stored` rates, the retail Cool `Write Operations` rate (per 10,000 operations), and the retail Cool `Data Retrieval` rate (per gigabyte) are obtained from the Azure Retail Prices API for the region and redundancy of the Storage Account, in the currency of the Flexera organization. If any of them cannot be found, the `Estimated Monthly Savings` is 0 and the `Savings Note` lists the missing rates.
- The `discount ratio` is the effective Hot rate divided by the retail Hot rate, or 1 if the retail Hot rate is used. It is applied to the retail Cool `Data Stored` and `Write Operations` rates under the assumption that any discounts or other changes from list price that applied to Hot storage will also apply to Cool storage.

```text
cool_rate = retail_cool_rate * discount_ratio
gross_monthly = eligible_gb * (effective_hot_rate - cool_rate)
retrieval_monthly = (read_bytes / 1024^3) * retail_cool_retrieval_rate * (30 / days_until_cool_tier)
net_monthly = gross_monthly - retrieval_monthly
one_time_transition = (eligible_blobs / 10000) * retail_cool_write_rate_per_10k * discount_ratio
payback_months = one_time_transition / net_monthly
```

- The `Estimated Monthly Savings` is `net_monthly`, or 0 if it is not positive, rounded to 3 decimal places.
- `retrieval_monthly` is subtracted because reading data from the Cool tier is charged per gigabyte. To stay conservative, it assumes that all of the data read during the lookback period would have been read from the Cool tier.
- `one_time_transition` is the `Transition Cost (One-Time)` of moving the eligible blobs to the Cool tier. It is not subtracted from the monthly savings. Instead, the `Payback Period (Months)` is the number of months of savings that it takes to recover it.
- Storage Accounts with an `Estimated Monthly Savings` below the `Minimum Savings Threshold`, or with a `Payback Period (Months)` longer than the `Maximum Payback Period (Months)`, are not reported.
- Savings from moving data to the Cold or Archive tiers are not estimated.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.
- Storage Accounts are sorted by `Estimated Monthly Savings`, from highest to lowest.

The estimate has the following limitations:

- Only data written to the Storage Account (`Ingress`) and data read using the `GetBlob` API (`Egress`) is considered to have been touched. Reads that use other APIs, and server-side copies, are not included.
- Cool tier read operation charges and early deletion charges are not included.
- The effective Hot rate is an approximation. It divides the cost of the last 30 days by the current Hot capacity, and the Hot `Data Stored` cost of a Storage Account may include other Hot data in the same Storage Account, such as Azure Files.
- Storage Accounts with a hierarchical namespace (Azure Data Lake Storage) are not estimated.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Days Until Cool Tier* - The number of days without activity after which a lifecycle management rule would move Hot block blobs to the Cool tier. This is the assumption used to estimate savings, and also the number of days of Azure Monitor metrics that are analyzed. This value cannot be set higher than 90 because Azure platform metrics are only retained for 93 days.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Storage Accounts that no estimate could be made for have an `Estimated Monthly Savings` of 0, so they are only reported if this is set to 0.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Allow/Deny Resource Groups* - Whether to allow or deny filtering by the resource groups specified in the `Allow/Deny Resource Groups List` parameter.
- *Allow/Deny Resource Groups List* - A list of allowed or denied Resource Group names to filter the results by. Entries can be in the format `resource_group_name` to filter all resource groups with that name regardless of subscription, or `subscription_id/resource_group_name` to filter a resource group within a specific subscription. Leave blank to consider all resource groups.
- *Exclusion Tags* - The policy template will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Maximum Payback Period (Months)* - Storage Accounts are not reported if the one-time cost of moving their blobs to the Cool tier would take longer than this many months of estimated savings to recover. Storage Accounts that an estimate was made for but that are not expected to save anything have no payback period, so they are not reported unless this is set to 0. Set to 0 for no limit.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to '0' to not show an incident table at all, and '100000' to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Insights/metrics/read`
  - `Microsoft.Resources/subscriptions/read`
  - `Microsoft.Storage/storageAccounts/read`
  - `Microsoft.Storage/storageAccounts/managementPolicies/read`

  The metrics are retrieved using the Azure Monitor batch metrics API, which requires the `Monitoring Reader` role (or a role that includes `Microsoft.Insights/metrics/read`) to be assigned at the subscription scope.

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_viewer`
  - `policy_manager`*

  \* Only required for meta-policy self-termination; not required if not using the meta parent of this policy template.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs
