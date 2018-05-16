### Tag Checker Policy

**What it does**

Uses RightScale Cloud Language (RCL) to check all instances and volumes in an account for a given tag key and reports back which
resources are missing the tag.   When searching for volumes in AzureRM, the volume must be a managed disk.  The policy will only check RightScale Tags.  Instance tags are bi-directionally synced with the cloud, but volumes are not bi-directionally synced.  Use the [Volume Tag Sync Policy](https://github.com/rightscale/policies/tree/master/tags/volume_tag_sync_policy) to bi-directionally sync tags between the cloud and RightScale.

**Dependencies**
  - [sys_log](https://github.com/rightscale/rightscale-plugins/blob/master/libraries/sys_log.rb)
  - [mailer](https://github.com/rightscale/policies/blob/master/libraries/mailer.rb)


**Installation**
1. Be sure your RightScale account is SelfService enabled
1. Follow the Getting Started section to create a Service Account and RightScale Credentials
1. Navigate to the appropriate SelfService portal
   - For more details on using the portal review the [SS User Interface Guide](http://docs.rightscale.com/ss/guides/ss_user_interface_guide.html)
1. In the Design section, use the `Upload CAT` interface to complete the following:
   1. Upload each of packages listed in the **Dependencies** Section in order
   1. Upload `tag_checker.cat.rb`

**Resource Names**

The report will show the name or the resource_uid of the resource.  If the resource doesn't have an  name then it will display the resource_uid.  For resources that do not have a name, you can follow the resource link and provide name.  The next report will have the new resource name.   

**Using Advanced Tags**

You can create a custom tag policy by using a JSON object that contains the tags, keys and validation value(s).  There are three options; string, regex and array.  You may include JSON in the field *Tags' Namespace:Keys Advanced List.* or provide a public url that contains your JSON.  The first key is the tag to match, each key has two other keys: validation-type is either array, string or regex.  validation includes the values the tag must contain.  If the tags and values are not on the server than the server will be reported in the email at the end of the cloudapp exectuion.

You can create missing tags by setting the default-value key of the tag. You can also set a prefix-value value for invalid tag values with prefix-value key. See example below.  

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
		"default-value":"none",
		"prefix-value":"invalid_"
	}
}
```

**Adding Delete Date Tags**

You may add a new tag (rs_policy:delete_date) to all instances that do not meet the tag policy.   Use the **# of days from now for delete_date tag value** field to set the rs_policy:delete_date tag value with the date the number of days from the run date.  The resources are only tagged, no other action is taken.

**Scheduling when the policy runs**

To control the frequency that the policy CAT runs, you should [create a schedule and associate it with the CAT](http://docs.rightscale.com/ss/guides/ss_creating_schedules.html) in RightScale Self-Service.

Specify the days of the week that you want the CAT to run. For example, if you want the policy CAT to run once a week on Monday, specify a schedule of only Monday. For the hours you should specify approximately a 30 minute time window for the policy CAT to complete. (It should take less than 15 minutes to run).

<img src="imgs/create_a_new_schedule.png">

**Cost**

This policy CAT does not launch any instances, and so does not incur any cloud costs.
