# Unapproved Instance Types

## What it does

This policy checks for instances that are using instance types that are not in the specified list and stops them after approval.

## Functional Details

The policy leverages the RightScale APIs to check instances across all supported clouds. When a non-approved instance type is detected, a report is emailed and the user can choose to Stop the instance after manual approval.

## Note: You can find Instance Types of all Supported Clouds under 'Policy Data Sets' section of root [README.md](https://github.com/flexera/policy_templates/blob/master/README.md)

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Tags to ignore* - List of tags that will exclude Servers from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag must be of the format 'namespace:predicate=value'. Example: 'rs_agent:type=right_link_lite,rs_monitoring:state=auth'
- *Approved Instance Types* - List of approved instance types of AWS, Azure and Google cloud, separated by comma. Example: 'a1.medium,a1.large,a1.xlarge,Standard_A0,Standard_A6,f1-micro,n1-highcpu-2 etc..'.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Stop Instances" action while applying the policy, the identified instances which are not in the list will be stopped.

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
