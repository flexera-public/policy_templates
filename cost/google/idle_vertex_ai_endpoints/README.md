# Google Idle Vertex AI Online Prediction Endpoints

## What It Does

This policy template identifies Google Cloud Vertex AI online prediction endpoints that have dedicated compute resources but have received little or no prediction traffic over a configurable lookback window. Only endpoints with at least one deployed model using `dedicatedResources` are evaluated; endpoints configured with `automaticResources` scale to zero and incur no continuous compute cost. Idle endpoints are reported to the user via an incident and can optionally be deleted automatically or after manual approval.

## How It Works

- The policy leverages the [Google Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com) to obtain a list of accessible Google projects and the [Vertex AI API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com) to list all online prediction endpoints across all locations in each project.
- Only endpoints with at least one deployed model that specifies `dedicatedResources` are considered. Endpoints using only `automaticResources` are excluded because they scale to zero and do not incur continuous compute charges.
- For each qualifying endpoint, the policy queries the [Cloud Monitoring API](https://console.cloud.google.com/flows/enableapi?apiid=monitoring.googleapis.com) for the total `aiplatform.googleapis.com/prediction/online/request_count` over the configured lookback window.
- Endpoints whose total request count over the lookback period is at or below the configured *Requests Threshold* are flagged as idle and included in the incident report.
- Estimated monthly savings are calculated from pre-fetched Vertex AI online prediction pricing data stored in `data/google/google_vertex_ai_pricing.json`.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the idle endpoint is deleted.

- The `Estimated Monthly Savings` is calculated as `pricePerHour × nodeCount × 730` for each deployed model using `dedicatedResources`, where `nodeCount` is the minimum replica count and `730` is the average number of hours in a month.
- Pricing is sourced from the pre-fetched data file `data/google/google_vertex_ai_pricing.json`, keyed by region and machine type. This data does not account for Flexera adjustment rules or negotiated discounts.
- If pricing data is not available for a given machine type in the endpoint's region, the cost for that machine type is treated as `$0`.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Statistic Lookback Period* - How many days back to query Cloud Monitoring for prediction traffic data. This value cannot be set higher than 42 because Google does not retain metrics for longer than 42 days.
- *Requests Threshold* - Endpoints with a total prediction request count at or below this threshold over the lookback period are flagged as idle. Set to `0` to flag only endpoints with absolutely zero traffic. Higher values can be used to catch near-idle endpoints.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects.
- *Ignore System Projects* - Whether or not to automatically ignore system projects e.g. projects whose id begins with `sys-`.
- *Ignore Google Apps Script Projects* - Whether or not to automatically ignore Google Apps Script projects e.g. projects whose id begins with `app-`.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all regions.
- *Exclusion Labels* - The policy will filter resources containing the specified labels from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified label key.
  - `Key==Value` - Filter all resources with the specified label key:value pair.
  - `Key!=Value` - Filter all resources missing the specified label key:value pair. This will also filter all resources missing the specified label key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified label key.
- *Exclusion Labels: Any / All* - Whether to filter instances containing any of the specified labels or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Labels` field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to `0` to not show an incident table at all, and `100000` to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action. For example, if a user selects the "Delete Idle Vertex AI Endpoints" action while applying the policy, all idle Vertex AI online prediction endpoints will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete idle Vertex AI online prediction endpoints after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#google) (*provider=gce*) which has the following:
  - `resourcemanager.projects.list`
  - `aiplatform.endpoints.list`
  - `aiplatform.locations.list`
  - `monitoring.timeSeries.list`
  - `aiplatform.endpoints.delete`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_viewer`
  - `policy_manager`*

  \* Only required for meta-policy self-termination; not required if not using the meta parent of this policy template.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally, this Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Vertex AI API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com)
- [Cloud Monitoring API](https://console.cloud.google.com/flows/enableapi?apiid=monitoring.googleapis.com)

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
