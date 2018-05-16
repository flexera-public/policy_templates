### Untagged Resources Policy

**What it does**

This policy will check all instances in state operational, running and provisioned, and all volumes and check for the tags listed in the *Tags' Namespace:Keys List* field.  For each resource that doesn't include the tags in the field they will be included in the policy incident report.   As new resources are added or tags and included on the resource the incident report will be updated to exclude the resource.

**Resource Names**

The report will show the name or the resource_uid of the resource.  If the resource doesn't have an  name then it will display the resource_uid.  For resources that do not have a name, you can follow the resource link and provide name.  The next report will have the new resource name.   
