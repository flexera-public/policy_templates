# Google Rightsize Cloud SQL Instances

## What It Does

This policy template checks all the Cloud SQL instances in Google Projects for the average or maximum CPU and/or memory usage over a user-specified number of days. If the usage is less than the user provided Idle Instance CPU and/or memory percentage threshold then the Cloud SQL instance is recommended for stopping. If the usage is less than the user provided Underutilized Instance CPU and/or Memory percentage threshold, then the Cloud SQL instance is recommended for downsizing. Both sets of Cloud SQL instances returned from this policy are emailed to the user.

NOTE: Estimated savings will only appear if you are ingesting Google Detailed Billing into Flexera CCO. If you have not configured Flexera One to ingest detailed billing information from Google, or prefer to receive recommendations produced by the Google Recommender service rather than Flexera, please use the [Google Rightsize Cloud SQL Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_cloudsql_recommendations) policy template instead of this one.

## How It Works

- The policy leverages the [Google Cloud SQL API](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com) to obtain a list of Google Cloud SQL instances and then uses the [Google Cloud Monitoring API](https://console.cloud.google.com/flows/enableapi?apiid=monitoring.googleapis.com) to check CPU and memory utilization over a user-specified number of days.
- The policy identifies all instances that have CPU and/or memory utilization below the user-specified idle thresholds and provides the relevant recommendation.
  - The recommendation provided for Idle Instances is a stop action. These instances can be stopped or deleted in an automated manner or after approval.
- The policy identifies all instances that have CPU and/or memory utilization below the user-specified underutilized thresholds and provides the relevant recommendation.
  - The recommendation provided for Underutilized Instances is a downsize action. These instances can be downsized in an automated manner or after approval.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized for idle resources if the resource is terminated, and for underutilized resources if the resource is downsized.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
  - For idle resources, the savings is the full cost of the resource.
  - For underutilized resources, the savings is the difference of the current cost of the resource and the estimated cost of the recommended resource type.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Enable Cross-Family Recommendations* - Whether to recommend downsizing instances to machine types outside of their current machine type family.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects
- *Ignore System Projects* - Whether or not to automatically ignore system projects e.g. projects whose id begins with `sys-`
- *Ignore Google Apps Script Projects* - Whether or not to automatically ignore Google Apps Script projects e.g. projects whose id begins with `app-`
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclusion Labels* - The policy will filter resources containing the specified labels from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified label key.
  - `Key==Value` - Filter all resources with the specified label key:value pair.
  - `Key!=Value` - Filter all resources missing the specified label key:value pair. This will also filter all resources missing the specified label key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified label key.
- *Exclusion Labels: Any / All* - Whether to filter instances containing any of the specified labels or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Labels` field.
- *Idle Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'idle' and therefore be flagged for termination. Set to -1 to ignore CPU utilization for idle instance recommendations.
- *Idle Instance Memory Threshold (%)* - The Memory threshold at which to consider an instance to be 'idle' and therefore be flagged for termination. Set to -1 to ignore memory utilization for idle instance recommendations.
- *Underutilized Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Set to -1 to ignore CPU utilization for underutilized instance recommendations.
- *Underutilized Instance Memory Threshold (%)* - The Memory threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Set to -1 to ignore memory utilization for underutilized instance recommendations.
- *Both CPU and Memory or Either* - Set whether an instance should be considered idle and/or underutilized only if both CPU and memory are under the thresholds or if either CPU or memory are under. Has no effect if other parameters are configured such that only CPU or memory is being considered.
- *Threshold Statistic* - Statistic to use when determining if an instance is idle/underutilized.
- *Statistic Lookback Period* - How many days back to look at CPU and/or memory data for instances. This value cannot be set higher than 42 because Google does not retain metrics for longer than 42 days (6 weeks).
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s). The "Downsize Cloud SQL Instances" option is only applies to underutilized instances, while the "Stop Cloud SQL Instances" and "Delete Cloud SQL Instances" options only apply to idle instances.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action. For example, if a user selects the "Delete Cloud SQL Instances" action while applying the policy, all idle Cloud SQL instances will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Downsize underutilized Cloud SQL instances after approval
- Stop idle Cloud SQL instances after approval
- Delete idle Cloud SQL instances after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`
  - `monitoring.metricDescriptors.list`
  - `monitoring.timeSeries.list`
  - `cloudsql.instances.list`
  - `cloudsql.instances.update`*
  - `cloudsql.instances.delete`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally, this Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Cloud Monitoring API](https://console.cloud.google.com/flows/enableapi?apiid=monitoring.googleapis.com)
- [Cloud SQL API](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com)

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
