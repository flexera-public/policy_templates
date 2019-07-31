## Unattached Volumes Policy Template

### What it does

This Policy Template scans all volumes in the given account and identifies any unattached volumes that have been unattached for at least the number of user-specified days. If any are found, an incident report will show the volumes, and related information and an email will be sent to the user-specified email address.

If the user specifies that the volumes should be deleted, the policy will delete the volumes.
If the volume is not able to be deleted, say, due to it being locked, the volume will be tagged to indicate the CloudException error that was received.
If the issue causing the delete failure is removed, the next run of the policy will delete the volume.
Note: The unattached volumes report will reflect the updated set of unattached volumes on the subsequent run.

Optionally, the user can specify one or more RightScale tags that if found on a volume will exclude the volume from the list.
Additionally, the user can optionally specify if the aged volumes should be deleted by the policy.

- *Estimated Savings* - is not a reflection of what you will actually save by moving the instance. It is the total cost of the instances in the current region. You will need to take into account any RI Purchases and the cost of running the instance in the new region. *You have been warned!!!*

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Identify volumes that have been Unattached for the given number of days* - enter the age of volumes for the incident.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *List of RightScale volume tags to exclude from policy.* - a list of tags used to excluded volumes from the incident.
- *Choose the appropriate action you wish to take on the Volumes* - selection to choose to email or email and delete volumes.
- *Create Final Snapshot* - Boolean for whether or not to take a final snapshot before deleting

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Delete Unattached volumes found in the incident
- Send an email report

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
