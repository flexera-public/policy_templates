## Discover Old Snapshots Policy Template

### What it does

This Policy Template will create a list old snapshots in the cloud account. The age of snapshots to list is provided in the *Number of days old snapshot to delete* parameter.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Number of days old snapshot to delete* - if a snapshot is older than this parameter it will be added to list
- *Snapshot Tag List* - list of tags that a snapshot can have to exclude it from the list.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Snapshots" action while applying the policy, all the snapshots that didn't satisfy the policy condition will be deleted.

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete old snapshots after an approval

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, volumes, volume_snapshots and tags).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer

### Supported Clouds

- AWS
- Azure
- Google
- VMWare (RCA-V)

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
