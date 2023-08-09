# Azure Unused Volumes

## What it does

This Policy Template scans all volumes in the given account and identifies any unattached volume that has been unused for at least the number of days specified by user. Using activity logs, we will determine whether any activity related to the unattached disk occurred in the range specified by user. If no activity detected, then the disk is deemed to be unused. If any unused disks are found, an incident report will show the volumes and related information. An email will be sent to the user-specified email address.

If the user approves that the volumes should be deleted, the policy will delete the volumes.
If the volume is not getting deleted, say, because it is locked, then the volume will be tagged to indicate the error that was received.

If the issue causing delete failure is removed, the next run of the policy will delete the volume.
Note: Unused volumes report will reflect the updated set of unused volumes on the subsequent run.

Optionally, the user can specify one or more tags that if found on a volume will exclude the volume from the list.

### Policy savings details

The policy includes the estimated savings.  The estimated savings is recognized if the resource is terminated.   Optima is used to receive the estimated savings which is the product of the most recent full day’s cost of the resource * 30.  The savings is displayed in the Estimated Monthly Savings column.  If the resource can not be found in Optima the value is 0.0.  The incident detail message includes the sum of each resource Estimated Monthly Savings as Total Estimated Monthly Savings.
If the user is not having the minimum required role of `billing_center_viewer` or if there is no enough data received from Optima to calculate savings, appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as 0.0 in the incident table.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/disks/read`
  - `Microsoft.Insights/eventtypes/values/read`
  - `Microsoft.StorSimple/managers/devices/iscsiservers/disks/delete`*
  - `Microsoft.StorSimple/managers/devices/iscsiservers/disks/write`*
  - `Microsoft.Compute/snapshots/write`*

\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Unused Age* - Number of days the volume is unused.
- *Email addresses* - A list of email addresses to notify.
- *Exclusion Tag Key* - A list of tags used to excluded volumes from the incident.
- *Create Final Snapshot* - Boolean for whether or not to take a final snapshot before deleting.
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Unused Volumes" action while applying the policy, the identified resources will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Delete Unused volumes after approval
- Send an email report

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
