## Superseded Instance Types Remediation Policy

### What it does

This Policy Template is used to automatically resize instances based on user-defined standards.  For example, the Policy uses a Disallowed Instance Type and its corresponding Superseded Instance Type.  If any Instances are found using the Disallowed type, they will be included in the corresponing Policy Incident.  Upon approval, Cloud Workflow will resize the Instance to the Superseded type. 

### Prerequesites
- The following RightScale Credentials
  - Cloud Management - `Actor`
  - Cloud Management - `Observer`

### Functional Details

- This policy supports a single old-to-new instance type mapping.  To apply this policy for multiple old-to-new instance type scenarios, the policy will need to be applied multiple times.  This will allow for flexibility in managing applied policies.
- The Exclude Tag parameter is a list value. Supply tags for instances you want excluded from the policy
- Upon Approval, the Instances that appear in the Incident will be immediately stopped, resized, and started via Cloud Workflow. 

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Disallowed Instance Type* - a single instance type that should be resized
- *Superseded Instance Type* - the new instance type that instances should be resized to
- *Exclude Tags* - A list of tags to filter out instances from being checked 
- *Email addresses* - A list of email addresses to notify

### Supported Clouds

- Amazon
- Google
- Azure

### Cost

This Policy Template does not incur any cloud costs.