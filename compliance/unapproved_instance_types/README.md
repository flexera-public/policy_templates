## Unapproved instance types
 
### What it does

This policy Report on any instances that are running using instance types that are not approved. \n See the [README](https://github.com/rightscale/policy_templates/tree/master/compliance/approved_instance_types) and [docs.rightscale.com/policies](http://docs.rightscale.com/policies/) to learn more.

### Functional Details
 
The policy leverages the RightScale APIs to check instances across all supported clouds. When a non-approved instance type is detected, a report is emailed and the user can choose to Stop the instance after manual approval.

 
### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - Instances with any of these tags will be ignored 
- *param_approved_instance_types* - List of approved instance types of AWS, Azure and Google cloud, separated by comma. Example: 'a1.medium,a1.large,a1.xlarge,Standard_A0,Standard_A6,f1-micro,n1-highcpu-2 etc..' 
Note: You can find Instance Types of all Supported Clouds under 'Policy Data Sets' section of root README.md file(https://github.com/rightscale/policy_templates/blob/master/README.md)

### Resource Names

The report will show the name or the resource_uid of the resource. If the resource doesn't have an name then it will display the resource_uid. For resources that do not have a name, you can follow the resource link and provide name. The next report will have the new resource name.

### Required Permissions

This policy requires permissions to access RightScale resources (instances and tags). Before applying this policy add the following roles to the user applying the policy. The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Actor
- Cloud Management - Observer

### Supported Clouds
 
- AWS
- Azure
- Google
 
### Cost
 
This Policy Template does not incur any cloud costs.
