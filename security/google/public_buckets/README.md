# Google Open Buckets

## What It Does

This Policy Template will check your account for Google Cloud Storage buckets with public permissions. Any buckets with such permissions will be included in the results.

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - Email addresses of the recipients you wish to notify.
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

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `storage.buckets.get`
  - `storage.buckets.list`
  - `storage.buckets.getIamPolicy`
  - `resourcemanager.projects.get`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally, this Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Storage API](https://console.cloud.google.com/flows/enableapi?apiid=storage.googleapis.com)

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
