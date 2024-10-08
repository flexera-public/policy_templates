# Google Old Snapshots

## What It Does

This policy finds Google snapshots older than the specified number of days and raises an incident with a list of said snapshots. Optionally, it will delete them.

## How It Works

- The policy makes use of the Google Cloud Compute API to obtain a list of snapshots and their ages in order to produce a list of recommendations.
- The Google Cloud Billing API is used to obtain pricing information for snapshots.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is deleted.

- The `Estimated Monthly Savings` is calculated using the monthly price obtained from the Google Cloud Billing API. Regional pricing is used when the region of the snapshot's source disk is obtainable; otherwise, general pricing is used.
  - **Note:** Due to the fact that snapshot prices vary based on region and whether a snapshot is multi-region, and the fact that Google's APIs do not return this information about snapshots due to snapshots technically not being a regional resource, all estimated savings should be taken as a best guess.
- Since the prices of individual resources are *not* obtained from Flexera CCO, they will *not* take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- If the Flexera organization is configured to use a currency other than USD, the savings values will be converted from USD using the exchange rate at the time that the policy executes.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - A list of email addresses to notify
- *Snapshot Age Threshold* - The number of days since the snapshot was created to consider a snapshot old.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects.
- *Exclusion Labels* - The policy will filter resources containing the specified labels from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified label key.
  - `Key==Value` - Filter all resources with the specified label key:value pair.
  - `Key!=Value` - Filter all resources missing the specified label key:value pair. This will also filter all resources missing the specified label key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified label key.
- *Exclusion Labels: Any / All* - Whether to filter instances containing any of the specified labels or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Labels` field.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Delete Snapshots" action while applying the policy, all old snapshots will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete old snapshots after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`
  - `billing.accounts.get`
  - `compute.zones.list`
  - `compute.regions.list`
  - `compute.disks.list`
  - `compute.snapshots.get`
  - `compute.snapshots.list`
  - `compute.snapshots.delete`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally, this Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Compute Engine API](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com)
- [Cloud Billing API](https://console.cloud.google.com/flows/enableapi?apiid=cloudbilling.googleapis.com)

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
