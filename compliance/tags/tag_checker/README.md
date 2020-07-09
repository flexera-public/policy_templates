# Untagged Resources Policy Template

## What it does

This policy will check all instances in state operational, running and provisioned, and all volumes and check for the tags listed in the *Tags' Namespace:Keys List* field.  For each resource that doesn't include the tags in the field they will be included in the policy incident report.   As new resources are added or tags and included on the resource the incident report will be updated to exclude the resource.  For more information on working with tags in RightScale please refer to the [Tagging](/cm/rs101/tagging.html#what-is-a-tag-) page.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Tags' Namespace:Keys List* - Comma-separated list of Tags' Namespace:Keys to audit. For example: \"ec2:project_code\" or \"bu:id\".
- *Tags' Namespace:Keys Advanced List.* - A JSON string to describe the tag policy configuration.  See below for an example.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Tag Resources" action while applying the policy, the identified resources will be tagged.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- An email is sent to the Email lists provided of the resources out of compliance
- Tags are updated using the advanced list using the JSON payload.

### Resource Names

The report will show the name or the resource_uid of the resource.  If the resource doesn't have an  name then it will display the resource_uid.  For resources that do not have a name, you can follow the resource link and provide name.  The next report will have the new resource name.   

### Validating Tag Values

You can create a custom tag policy by using a JSON object that contains the tags, keys and validation value(s).  There are three options; string, regex and array.  You may include JSON in the field *Tags' Namespace:Keys Advanced List.* .  The first key is the tag to match, each key has two other keys: validation-type is either array, string or regex.  Validation includes the values the tag must contain.  If the tags and values are not on the resource than the resource will be reported in the email at the end of the policy execution.

You can create missing tags by setting the default-value key of the tag. You can also set a prefix-value value for invalid tag values with prefix-value key. See example below.  

Example JSON:

```
{
  "rs_agent:type": {
    "description":"Validate the tag using a array of possible values",
    "validation-type": "array",
    "validation": ["right_link_lite", "bar"]
  },
  "rs_login:state": {
    "description":"Validate the tag value using a string",
    "validation-type": "string",
    "validation": "user"
  },
  "rs_id:user":{
    "description":"Validate the tag value using a regex",
    "validation-type": "regex",
    "validation": "^sp",
    "default-value":"none",
    "prefix-value":"invalid_"
  }
}
```

## Required Permissions

This policy requires permissions to access RightScale resources (instances, volumes and tags).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Actor
- Cloud Management - Observer

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
