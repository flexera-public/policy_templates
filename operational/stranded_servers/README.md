# Stranded Servers

## What it does

This policy checks all Servers in Cloud Management and reports on any that have stranded during the boot process. It provides the option to terminate any stranded servers after approval.

## Functional Details

The policy leverages Cloud Management APIs to identify servers that have not successfully completed their boot sequence (i.e. have "stranded in booting"). Servers can optionally be terminated after approval.

Note: Locked instances will not be terminated.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify.
- *Ignore tags* - Instances with any of these tags will be ignored.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Resource Names

The report will show the name or the resource_uid of the resource. If the resource doesn't have an name then it will display the resource_uid. For resources that do not have a name, you can follow the resource link and provide name. The next report will have the new resource name.

### Required Permissions

This policy requires permissions to access RightScale resources (instances and tags). Before applying this policy add the following roles to the user applying the policy. The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Actor
- Cloud Management - Observer

## Supported Clouds

- All

## Cost

This Policy Template does not incur any cloud costs.
