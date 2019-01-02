## Discover Old Snapshots Policy Template

### What it does

This Policy Template will create a list old snapshots in the cloud account. The age of snapshots to list is provided in the *Number of days old snapshot to delete* parameter.


### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Number of days old snapshot to delete* - if a snapshot is older than this parameter it will be added to list
- *Snapshot Tag List* - list of tags that a snapshot can have to exclude it from the list.

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Stop and Start the instances with the schedule tag.
- Send an email report

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, volumes, volume_snapshots and tags).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer

### Supported Clouds

- AWS
- Azure
- Google

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
