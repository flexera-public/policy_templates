## Downsize Instances Policy Template

### What it does

This Policy Template uses user defined tags to determine if it can decrease the size of your running instance after user approval. 

### Usage

The Downsize Instances Policy Template is used to actually downsize instances user defined tags on the instances.  The policy will use the *Tags to find instances* list to find the instances with provided tags and downsize them.  The tags must be inform of a [RightScale Tag](https://docs.rightscale.com/cm/ref/list_of_rightscale_tags.html#overview)
To downsize the instance it must be **stopped**.  If you don't want to stop and resize the instance you can add an additional tag and include that tag in the *Tags to ignore instances* input.
If a server is marked `N/A`, no action will be taken and only the resize tag will be removed. You will need to manually move that instance to another family type.
When an instance is downsized a new tag *rs_downsize:cooldown* is added which value is the date and time of the number of days from the Downsize to the Cooldown Days parameter.  This tag is then deleted after the Cooldown Days has exceeded


### Parameters

#### Downsize Instances Policy Template
1. Email list - List of email addresses to send incident report to
2. Tags to find instances - List of tags used to filter instances that must validate policy. (e.g.: ec2:downsize:true, azure:downsize:true, gce:downsize=true)
3. Tags to ignore instances - List of tags that will exclude instances from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'
4. Cooldown Days - Days to cooldown between checks of same instance.  

#### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Downsize instances
- Delete Cooldown tag after cooldown days has exceeded
- Send an email report

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, instances and tags).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer

### Supported Clouds

- AWS
- Azure
- Google

### Instance Size Relationship Mapping

This policy template uses instance mappings that we have defined in the following files:
- AWS: [/rightscale/policy_templates/master/data/aws/instance_types.json](/rightscale/policy_templates/master/data/aws/instance_types.json)
- Azure:  [/rightscale/policy_templates/master/data/azure/instance_types.json](/rightscale/policy_templates/master/data/azure/instance_types.json)
- Google: [/rightscale/policy_templates/master/data/google/instance_types.json](/rightscale/policy_templates/master/data/google/instance_types.json)

If you would like to modify the relationships, you can take the following steps:
1. Clone the relevant `instance_types.json` file to a publicly available storage location. We recommend GitHub.
1. Make the necessary updates to the mapping file(s)
1. Update the relevant datasources within the Policy Template to pull the `instance_types.json` file from the new location.
    - If using GitHub to store the updated mapping files, you simply need to update the `path` field in the datasources `ds_aws_instance_size_map`, `ds_azure_instance_size_map`, and `ds_google_instance_size_map`

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
