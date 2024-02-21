# Google Idle Cloud SQL Instance Recommender

## What It Does

This policy reports on any idle Cloud SQL instances identified by the Google Recommender service. The user can then choose to stop or delete the Cloud SQL instance if desired. Optionally, the user can filter results by label, project ID/name, or region.

### How It Works

This policy uses the following Google recommenders:

- `google.cloudsql.instance.IdleRecommender`: Checks if a Cloud SQL instance is idle and recommends stopping the instance when appropriate.

More information is available in Google's documentation:

- [Identify idle Cloud SQL instances](https://cloud.google.com/sql/docs/mysql/recommender-sql-idle)

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is deleted.

- The `Estimated Monthly Savings` is obtained directly from the Google Recommender service.
- Since the savings estimates are obtained directly from Google, they will take into account any cloud provider discounts but *not* any Flexera adjustment rules or other cost manipulations specific to the Flexera platform.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- If the Flexera organization is configured to use a currency other than the one Google Recommender is reporting the savings estimates in, the savings values will be converted using the exchange rate at the time that the policy executes.

## Prerequisites

This Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Cloud SQL API](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com)
- [Recommender API](https://console.cloud.google.com/flows/enableapi?apiid=recommender.googleapis.com)

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - Roles
    - `Cloud SQL Recommender Viewer`
    - `Cloud SQL Recommender Admin`*

  - Permissions
    - `recommender.cloudsqlIdleInstanceRecommendations.list`
    - `resourcemanager.projects.get`
    - `cloudsql.instances.list`
    - `cloudsql.instances.update`*
    - `cloudsql.instances.delete`*

\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclusion Labels* - The policy will filter resources containing the specified labels from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified label key.
  - `Key==Value` - Filter all resources with the specified label key:value pair.
  - `Key!=Value` - Filter all resources missing the specified label key:value pair. This will also filter all resources missing the specified label key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified label key.
- *Exclusion Labels: Any / All* - Whether to filter instances containing any of the specified labels or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Labels` field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Delete Cloud SQL Instances" action while applying the policy, all idle VM instances will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Stop idle Cloud SQL instances after approval
- Delete idle Cloud SQL instances after approval

## Supported Clouds

- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.

## API Quotas

Google sets quotas on the Recommender API; this will cause a `429 RESOURCE_EXHAUSTED` response when the quota is exceeded. See [Quotas & Limits](https://cloud.google.com/recommender/quotas) for more information.
