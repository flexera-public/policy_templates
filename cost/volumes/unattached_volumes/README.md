## Unattached Volumes Policy Template

### What it does

This Policy Template scans all volumes in the given account and identifies any unattached volumes that have been unattached for at least the number of user-specified days. If any are found, an incident report will show the volumes, and related information and an email will be sent to the user-specified email address.

If the user specifies that the volumes should be deleted, the policy will delete the volumes.
If the volume is not able to be deleted, say, due to it being locked, the volume will be tagged to indicate the CloudException error that was received.
If the issue causing the delete failure is removed, the next run of the policy will delete the volume.
Note: The unattached volumes report will reflect the updated set of unattached volumes on the subsequent run.

Optionally, the user can specify one or more RightScale tags that if found on a volume will exclude the volume from the list.
Additionally, the user can optionally specify if the aged volumes should be deleted by the policy.

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, volumes, deployments, placement groups and tags).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Actor
- Cloud Management - Observer

### Supported Clouds

- AWS
- Azure
- AzureRM
- Google
- VMware (RCA-V)

### Cost

This Policy Template does not incur any cloud costs.
