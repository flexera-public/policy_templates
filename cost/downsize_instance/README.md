# Downsize Instances Policy Template

## What it does

This Policy Template uses user defined tags to determine if it can decrease the size of your running instance after user approval.

## Usage

The Downsize Instances Policy Template is used to actually downsize instances user defined tags on the instances.  The policy will use the *Tags to find instances* list to find the instances with provided tags and downsize them.  The tags must be inform of a [RightScale Tag](https://docs.rightscale.com/cm/ref/list_of_rightscale_tags.html#overview)
To downsize the instance it must be **stopped**.  If you don't want to stop and resize the instance you can add an additional tag and include that tag in the *Tags to ignore instances* input.
If a server is marked `N/A`, no action will be taken and only the resize tag will be removed. You will need to manually move that instance to another family type.
When an instance is downsized a new tag *rs_downsize:cooldown* is added which value is the date and time of the number of days from the Downsize to the Cooldown Days parameter.  This tag is then deleted after the Cooldown Days has exceeded

## Parameters

- Email list - List of email addresses to send incident report to
- Tags to find instances - List of tags used to filter instances that must validate policy. (e.g.: ec2:downsize:true, azure:downsize:true, gce:downsize=true)
- Tags to ignore instances - List of tags that will exclude instances from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'
- Cooldown Days - Days to cooldown between checks of same instance.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Downsize Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be instances.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Downsize instances
- Delete Cooldown tag after cooldown days has exceeded
- Send an email report

## Required Permissions

This policy requires permissions to access RightScale resources (clouds, instances and tags).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer
- Cloud Management - Actor (needed for actions)

## Supported Clouds

- AWS
- Azure
- Google

## Instance Size Relationship Mapping

This policy template uses instance mappings that we have defined in the following files:

- AWS: [https://github.com/flexera/policy_templates/blob/master/data/aws/instance_types.json](https://github.com/flexera/policy_templates/blob/master/data/aws/instance_types.json)
- Azure:  [https://github.com/flexera/policy_templates/blob/master/data/azure/instance_types.json](https://github.com/flexera/policy_templates/blob/master/data/azure/instance_types.json)
- Google: [https://github.com/flexera/policy_templates/blob/master/data/google/instance_types.json](https://github.com/flexera/policy_templates/blob/master/data/google/instance_types.json)

If you would like to modify the relationships, you can take the following steps:

1. Clone the relevant `instance_types.json` file to a publicly available storage location. We recommend GitHub.
1. Make the necessary updates to the mapping file(s)
1. Update the relevant datasources within the Policy Template to pull the `instance_types.json` file from the new location.
  - If using GitHub to store the updated mapping files, you simply need to update the `path` field in the datasources `ds_aws_instance_size_map`, `ds_azure_instance_size_map`, and `ds_google_instance_size_map`

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
