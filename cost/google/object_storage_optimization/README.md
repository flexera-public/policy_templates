# Google Object Storage Optimization

## What It Does

This policy template checks Google buckets for older objects and produces recommendations to move these objects to the 'nearline' or 'coldline' class after a given period of time. Optionally, an email report is sent of these objects and the user can change their class or delete them.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *New Storage Class* - Whether to move objects to `nearline` or `coldline` if they meet the specified.age thresholds. Select `Both` to consider moving objects to either one based on the specified age thresholds.
- *Nearline Class Age Threshold (Days)* - Time in days since object was last modified to change storage tier to `nearline`. Not applicable if `Coldline` is selected for New Storage Class.
- *Coldline Class Age Threshold (Days)* - Time in days since object was last modified to change storage tier to `coldline`. Not applicable if `Nearline` is selected for New Storage Class.
- *Storage Bucket List* - A list of Google Object Storage Buckets to assess objects in. Leave blank to assess objects in all buckets.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects.
- *Exclusion Labels* - The policy will filter resources containing the specified labels from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified label key.
  - `Key==Value` - Filter all resources with the specified label key:value pair.
  - `Key!=Value` - Filter all resources missing the specified label key:value pair. This will also filter all resources missing the specified label key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified label key.
- *Exclusion Labels: Any / All* - Whether to filter instances containing any of the specified labels or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Labels` field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Update Objects Storage Class" action while applying the policy, all the identified objects will be moved to `nearline` or `coldline`.

## Policy Actions

- Send an email report
- Change object storage class after approval
- Delete object after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`
  - `storage.buckets.list`
  - `storage.objects.list`
  - `storage.objects.create`*
  - `storage.objects.delete`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally, this Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Cloud Storage API](https://console.cloud.google.com/flows/enableapi?apiid=storage.googleapis.com)

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
