# Google Long Stopped VM Instances

## What It Does

This policy finds Google virtual machines which have been stopped for more than a user-specified number of days and emails a report containing a list of the offending instances. Optionally, the policy will delete the instances after user approval.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclusion Labels (Key:Value)* - Google labels to ignore resources that you don't want to produce recommendations for. Use Key:Value format for specific label key/value pairs, and Key:\* format to match any resource with a particular key, regardless of value. Examples: env:production, DO_NOT_DELETE:\*
- *Stopped Days* - The number of days a Google VM needs to be stopped to include it in the incident report.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete VM Instances" action while applying the policy, all the identified stopped instances will be terminated.

## Actions

The following policy actions are taken on any resources found to be out of compliance.

- Sends an email notification.
- Delete reported virtual machines after approval.

## Prerequisites

This Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Compute Engine API](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com)

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - Permissions
    - `resourcemanager.projects.get`
    - `monitoring.metricDescriptors.list`
    - `monitoring.timeSeries.list`
    - `compute.instances.list`
    - `compute.instances.get`
    - `compute.instances.stop`*
    - `compute.instances.delete`*

\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.
