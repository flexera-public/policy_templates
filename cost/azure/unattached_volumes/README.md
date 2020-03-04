# Azure Delete Unattached Volumes

## What it does

This Policy Template scans all volumes in the given account and identifies any unattached volumes that have been unattached for at least the number of user-specified days. Using log analytics, we will determine the number of days the disk has been ditached. If any are found, an incident report will show the volumes, and related information and an email will be sent to the user-specified email address.

If the user approves that the volumes should be deleted, the policy will delete the volumes.
If the volume is not able to be deleted, say, due to it being locked, the volume will be tagged to indicate the error that was received.

If the issue causing the delete failure is removed, the next run of the policy will delete the volume.
Note: The unattached volumes report will reflect the updated set of unattached volumes on the subsequent run.

Optionally, the user can specify one or more tags that if found on a volume will exclude the volume from the list.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Unattached days* - The number of days a volume has been unattached.
- *Email addresses* - A list of email addresses to notify.
- *Exclude Tags.* - A list of tags used to excluded volumes from the incident.
- *Create Final Snapshot* - Boolean for whether or not to take a final snapshot before deleting.
- *Workspace ID* - ID of the log analytics workspace which is created in the Azure portal.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.
In the log analytics workspace provided, Microsoft-Windows-Disk/Operational event log should be enabled.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.OperationalInsights/workspaces/analytics/query/action
- Microsoft.StorSimple/managers/devices/iscsiservers/disks/read
- Microsoft.StorSimple/managers/devices/iscsiservers/disks/delete
- Microsoft.StorSimple/managers/devices/iscsiservers/disks/write
- Microsoft.Compute/snapshots/write

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Delete Unattached volumes after approval
- Send an email report

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.