## Untagged Resources Policy Template

### What it does

This policy will check all instances in state operational, running and provisioned, and all volumes and check for the tags listed in the *Tags' Namespace:Keys List* field.  For each resource that doesn't include the tags in the field they will be included in the policy incident report.   As new resources are added or tags and included on the resource the incident report will be updated to exclude the resource.

**Resource Names**

The report will show the name or the resource_uid of the resource.  If the resource doesn't have an  name then it will display the resource_uid.  For resources that do not have a name, you can follow the resource link and provide name.  The next report will have the new resource name.   

**Validating Tag Values**

You can create a custom tag policy by using a JSON object that contains the tags, keys and validation value(s).  There are three options; string, regex and array.  You may include JSON in the field *Tags' Namespace:Keys Advanced List.* .  The first key is the tag to match, each key has two other keys: validation-type is either array, string or regex.  Validation includes the values the tag must contain.  If the tags and values are not on the resource than the resource will be reported in the email at the end of the policy execution.

You can create missing tags by setting the default-value key of the tag. You can also set a prefix-value value for invalid tag values with prefix-value key. See example below.  

Example JSON:
```json
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
	"rs_id: user": {
		"description":"Validate the tag value using a regex",		
		"validation-type": "regex",
		"validation": "^sp",
		"default-value":"none",
		"prefix-value":"invalid_"
	}
}
```

### Supported Tags

- AWS
- Azure
- Google

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.


