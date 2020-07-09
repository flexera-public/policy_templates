### Terminate Instances with End Date Policy

**What it does**

This Policy allows you to set a tag with a timestamp and terminate an instance at a specific time. It will not terminate locked instances. 

**How to Use**

This policy relies on a tag to terminate instances based on a schedule.  The tag value is in a timestamp notation.

You can use the following example when tagging your instances. If you tag in the cloud natively you can ignore `ec2`,`gce`,`azure`, Flexera CMP will automatically add that on discovery.

***Instance Terminate Tag Example***

***Rightscale***
  * `instance:terminate=2019-05-20T13:48:21Z`

***Tag to set in cloud provider***
  * `terminate=2019-05-20T13:48:21Z`

***Tag discovered by CMP***
  * `ec2:terminate=2019-05-20T13:48:21Z`
  * `gce:terminate=2019-05-20T13:48:21Z`
  * `azure:terminate=2019-05-20T13:48:21Z`

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - Email addresses of the recipients you wish to notify
- *Tag of instances to terminate* - Tags of instances to terminate in timestamp format, Eg: `instance:terminate=*`, `ec2:terminate=*`, `gce:terminate=*`, `azure:terminate=*`
- *Tags to ignore* - List of tags that will exclude instances from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag must be of the format 'namespace:predicate=value'.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, the identified instances will be terminated.

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Terminate the instances. 
- Send an email report

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, instances and tags).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Actor
- Cloud Management - Observer

## Supported Clouds

The following clouds are supported:
- All RightScale enabled clouds

**Cost**

This Policy Template does not incur any cloud costs.
