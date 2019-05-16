## AWS Superseded Instance Types Remediation Policy

### What it does

This Policy Template is used to automatically resize Amazon Resource Manager Instances (VMs) based on user-defined standards.  For example, the Policy allows for a Disallowed Instance Type and its corresponding Superseded Instance Type.  If any Instances are found using the Disallowed type, they will be included in the corresponing Policy Incident.  Upon approval, Cloud Workflow will resize the Instance to the Superseded type. 

### Prerequesites
- The following RightScale Credentials
  - Cloud Management - `Actor`
  - Cloud Management - `Observer`
  - The `policy_designer`, `policy_manager` & `policy_publisher` roles

### Functional Details

- This policy supports a single old-to-new instance type mapping.  To apply this policy for multiple old-to-new instance type scenarios, the policy will need to be applied multiple times.  This will allow for flexibility in managing applied policies.
- The Exclusion Tag parameter is a string value.  Supply the Tag Key only.  Tag Values are not analyzed and therefore are not need.  If the exclusion tag key is used on an Instance, that Instance is presumed to be exempt from this policy.
- Upon Approval, the Instances that appear in the Incident will be immediately stopped, resized, and started via Cloud Workflow. 

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Disallowed Instance Type* - a single Amazon instance type that should be resized
- *Superseded Instance Type* - the new Amazon instance type that instances should be resized to
- *Exclude Tags* - A list of tags to exclude servers 
- *Email addresses* - A list of email addresses to notify

### Supported Clouds

- Amazon

### Cost

This Policy Template does not incur any cloud costs.