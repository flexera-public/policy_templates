# No Recent Snapshots Policy Template

### What it does

This Policy Template verifies that you have snapshots on all of your important volumes.

### Usage

**_Warning: This policy will stop your servers to guarantee consistency._**
This policy template has two options: `Email` and `Snapshot And Email`. If you choose `Email` you will get a report of volumes that have missing snapshots within the timeperiod.
If you choose `Snapshot And Email` it will email you a report of volumes that have missing snapshots, and then it will stop the server, wait for completion, take a snapshot and
start up the server.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email address to send escalation emails to* - Example: noreply@example.com
- *Number of days between snapshot*s - The number of days between snapshots that the policy will check against.
- *Escalation Options* - Allowed Values: "Email", "Snapshot And Email"
- *Include Root Device* - This option instructs the policy template whether or not to check root volumes for compliance, anything connected to `/dev/sda1`.
- *Volume and Server tags to exclude* -  Example: snapshot_policy:exclude=1
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Resources" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

### Policy actions

The following policy actions are taken on any resources found to be out of compliance.

- Stop the server and take snapshot, restart the server.
- Send an email report

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, volumes, volume_snapshots, and instances).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer

### Supported Clouds

The following clouds are supported:

- AWS
- Azure
- Google

### Cost

This Policy Template will increase the cost of overall cloud usage by taking snapshots of data.
