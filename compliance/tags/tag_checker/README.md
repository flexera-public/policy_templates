### Untagged Resources Policy

**What it does**

This policy will check all instances in state operational, running and provisioned, and all volumes and check for the tags listed in the *Tags' Namespace:Keys List* field.  For each resource that doesn't include the tags in the field they will be included in the policy incident report.   As new resources are added or tags and included on the resource the incident report will be updated to exclude the resource.

**Resource Names**

The report will show the name or the resource_uid of the resource.  If the resource doesn't have an  name then it will display the resource_uid.  For resources that do not have a name, you can follow the resource link and provide name.  The next report will have the new resource name.   

**Using Advanced Tags**

You can create a custom tag policy by using a JSON object that contains the tags, keys and validation value(s).  There are three options; string, regex and array.  You may include JSON in the field *Tags' Namespace:Keys Advanced List.*  The first key is the tag to match, each key has two other keys: validation-type is either array, string or regex.  validation includes the values the tag must contain.  If the tags and values are not on the server than the server will be reported in the email at the end of the cloudapp execution.

Example JSON:
```json
{
	"rs_agent:type": {
		"validation-type": "array",
		"validation": ["right_link_lite", "bar"]
	},
	"rs_login:state": {
		"validation-type": "string",
		"validation": "user"
	},
	"rs_id: user": {
		"validation-type": "regex",
		"validation": "^sp",
	}
}
```
