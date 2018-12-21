## Discover Old Snapshots Policy Template

### What it does

This Policy Template will check your account for old snapshots. It takes several parameters:
- `Number of days old snapshot to delete` - if a snapshot is older than this parameter it will be added to list
- `Email address to send escalation emails to` - Email to alert when it finds snapshots that meet the criteria
- `Snapshot Tag List` - list of tags that a snapshot can have to exclude it from the list.

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, volumes, volume_snapshots and tags).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer

### Supported Clouds

- AWS
- Azure
- Google

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
