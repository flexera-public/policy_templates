# Azure Unused Volumes

## What it does

This Policy Template scans all volumes in the given account and identifies any volume that has been unused for at least the number of days specified by user. Using activity logs, we will determine the number of days the volume has been unused. If any are found, an incident report will show the volumes and related information. An email will be sent to the user-specified email address.

If the user approves that the volumes should be deleted, the policy will delete the volumes.
If the volume is not getting deleted, say, because it is locked, then the volume will be tagged to indicate the error that was received.

If the issue causing delete failure is removed, the next run of the policy will delete the volume.
Note: Unused volumes report will reflect the updated set of unused volumes on the subsequent run.

Optionally, the user can specify one or more tags that if found on a volume will exclude the volume from the list.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Unused Age* - Number of days the volume is unused.
- *Email addresses* - A list of email addresses to notify.
- *Exclude Tags.* - A list of tags used to excluded volumes from the incident.
- *Create Final Snapshot* - Boolean for whether or not to take a final snapshot before deleting.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Delete Unused volumes after approval
- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.StorSimple/managers/devices/iscsiservers/disks/read
- Microsoft.StorSimple/managers/devices/iscsiservers/disks/delete
- Microsoft.StorSimple/managers/devices/iscsiservers/disks/write
- Microsoft.Compute/snapshots/write

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
