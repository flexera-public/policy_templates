# Google Unlabeled Resources

## What It Does

This policy template checks for Google Cloud resources missing the user-specified labels. An incident is raised containing the unlabeled resources, and the user has the option to label them.

## How It Works

- The policy leverages the Google Compute and Storage APIs to retrieve a list of all resources in the Google Cloud estate.
- The policy then filters that list based on user-specified parameters.
- The policy then identifies the resources in the filtered list that are missing the labels specified by the user.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects.
- *Resource Types* - The types of resources to check labels for. Any options not selected will not be reported on.
- *Labels* - The policy will report resources missing the specified labels. The following formats are supported:
  - `Key` - Find all resources missing the specified label key.
  - `Key==Value` - Find all resources missing the specified label key:value pair and all resources missing the specified label key.
  - `Key!=Value` - Find all resources that have the specified label key:value pair.
  - `Key=~/Regex/` - Find all resources where the value for the specified key does not match the specified regex string and all resources missing the specified label key.
  - `Key!~/Regex/` - Find all resources where the value for the specified key matches the specified regex string.
- *Any / All* - Whether to report on instances missing any of the specified labels or all of them. Only applicable if more than one value is entered in the `Labels` field.

This policy has the following input parameters required when adding labels to resources from a raised incident:

- *Add Labels (Key=Value)* - Cloud native labels to add to resources with missing labels. Use Key=Value format. Examples: env=production, team=finance

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Label to the selected resources with given input

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`
  - `compute.disks.list`
  - `compute.disks.setLabels`*
  - `compute.externalVpnGateways.list`
  - `compute.externalVpnGateways.setLabels`*
  - `compute.images.list`
  - `compute.images.setLabels`*
  - `compute.instances.list`
  - `compute.instances.setLabels`*
  - `compute.snapshots.list`
  - `compute.snapshots.setLabels`*
  - `compute.vpnGateways.list`
  - `compute.vpnGateways.setLabels`*
  - `storage.buckets.list`
  - `storage.buckets.update`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally, this Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Compute Engine API](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com)

## Supported Clouds

- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
