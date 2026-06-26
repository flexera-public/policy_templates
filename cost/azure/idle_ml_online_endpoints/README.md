# Azure Idle ML Online Endpoints

## What It Does

This policy template finds Azure Machine Learning managed online endpoints that are provisioned and running but receiving little or no inference traffic over a user-specified lookback window, then raises an incident with a list of those endpoints. Optionally, it deletes them. Idle managed online endpoints consume VM compute continuously regardless of actual usage, making them a significant source of avoidable cloud spend. For low-frequency or batch-oriented inference workloads, batch endpoints or on-demand invocation patterns are far more cost-effective alternatives.

## How It Works

- The `Microsoft.MachineLearningServices/workspaces` ARM API is used to enumerate all AML workspaces in each in-scope Azure subscription.
- The `Microsoft.MachineLearningServices/workspaces/{workspace}/onlineEndpoints` API lists all managed online endpoints within each workspace. Only endpoints with a `provisioningState` of `Succeeded` and a `kind` of `Managed` are evaluated; endpoints still provisioning, updating, or in a failed state are excluded, as are Kubernetes online endpoints, which have a distinct billing model.
- For each filtered endpoint, the `onlineEndpoints/{endpoint}/deployments` API retrieves the active deployments. An endpoint must have at least one deployment with a `provisioningState` of `Succeeded` to be evaluated. The VM instance type (`sku.name`) and instance count (`sku.capacity`) are collected for cost context.
- The `microsoft.insights/metrics` API retrieves the `RequestsPerMinute` metric for each qualifying endpoint over the configured lookback window, using daily granularity and `Total` aggregation. The sum of all daily `RequestsPerMinute` values represents the total inference traffic metric for the period.
- Endpoints whose total traffic metric falls at or below the configured threshold are flagged as idle.
- Estimated monthly savings are derived from the deployment's VM SKU and instance count, using hourly Linux on-demand list prices from the [Azure VM pricing data file](https://github.com/flexera-public/policy_templates/blob/master/data/azure/azure_vm_pricing.json), multiplied by the instance count and by 730 hours per month. Azure ML managed online endpoints run model containers on Linux VM infrastructure regardless of the model or framework.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the endpoint is deleted.

- The `Estimated Monthly Savings` is calculated by summing the hourly on-demand Linux list price for each active deployment's VM SKU from the [Azure VM Pricing data file](https://github.com/flexera-public/policy_templates/blob/master/data/azure/azure_vm_pricing.json), multiplied by the deployment's instance count and by 730 (the average number of hours in a month).
- Savings estimates are based on **list (on-demand) prices** and do not account for Reserved Instances, Savings Plans, enterprise agreements, or other discounts.
- If the endpoint's region or VM SKU cannot be found in the pricing data, the `Estimated Monthly Savings` for that endpoint is 0.
- Azure ML managed online endpoints always run model containers on Linux VM infrastructure, so Linux pricing is used regardless of the underlying model or framework.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Azure Endpoint* - The Azure API endpoint to use. Use the default value of `management.azure.com` unless targeting Azure China (`management.chinacloudapi.cn`).
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Default is 0 (all idle endpoints are reported).
- *Statistic Lookback Period* - How many days back to query Azure Monitor metrics for inference traffic. This value cannot be set higher than 90 because Azure does not retain metrics for longer than 90 days. Default is 30 days.
- *Requests Threshold* - Endpoints with total `RequestsPerMinute` metric values at or below this threshold over the lookback period are flagged as idle. Set to 0 to flag only endpoints with absolutely zero traffic. Higher values can be used to catch near-idle endpoints.
- *Allow/Deny Subscriptions* - Allow or Deny entered subscriptions to filter results.
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. Leave blank to check all subscriptions.
- *Allow/Deny Resource Groups* - Allow or Deny entered Resource Groups to filter results.
- *Allow/Deny Resource Groups List* - A list of allowed or denied Resource Group names. Entries can optionally use the format `SUBSCRIPTION_ID/RESOURCE_GROUP_NAME` to limit filtering to a specific subscription. Leave blank to check all resource groups.
- *Allow/Deny Regions* - Allow or Deny entered regions to filter results.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Leave blank to check all regions.
- *Exclusion Tags* - Cloud native tags to ignore resources that you don't want to produce recommendations for. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter endpoints containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Exclusion Endpoint Names* - A list of Azure ML online endpoint names to exclude from the results. Enter exact endpoint names.
- *Automatic Actions* - When set, the policy will automatically take the selected action(s).
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Delete Idle ML Online Endpoints" action while applying the policy template, all the Azure ML managed online endpoints that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete idle Azure ML managed online endpoints after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Resources/subscriptions/read`
  - `Microsoft.MachineLearningServices/workspaces/read`
  - `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/read`
  - `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/deployments/read`
  - `Microsoft.Insights/metrics/read`
  - `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/delete`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_viewer`
  - `policy_manager`*

  \* Only required for meta-policy self-termination; not required if not using the meta parent of this policy template.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
