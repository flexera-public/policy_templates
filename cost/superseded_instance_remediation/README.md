# Superseded Instance Types Remediation Policy

## What it does

This Policy Template is used to automatically resize instances based on user-defined standards.  For example, the Policy uses a Disallowed Instance Type and its corresponding Superseded Instance Type.  If any Instances are found using the Disallowed type, they will be included in the corresponing Policy Incident.  Upon approval, Cloud Workflow will resize the Instance to the Superseded type. 

## Prerequesites

The following RightScale Permissions

  - Cloud Management - `Actor`
  - Cloud Management - `Observer`

## Functional Details

- This policy supports a single old-to-new instance type mapping.  To apply this policy for multiple old-to-new instance type scenarios, the policy will need to be applied multiple times.  This will allow for flexibility in managing applied policies.
- For Example:
  - Old Instance Type: `c1.medium`, Superseded Instance Type: `c5.large`
  - Old Instance Type: `Standard_A1`, Superseded Instance Type: `Standard_A1_v2`
- The Exclude Tag parameter is a list value. Supply tags for instances you want excluded from the policy
- Upon Approval, the Instances that appear in the Incident will be immediately stopped, resized, and started via Cloud Workflow. 

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Old Instance Type* - a single instance type that should be resized
- *Superseded Instance Type* - the new instance type that instances should be resized to
- *Exclude Tags* - A list of tags to filter out instances from being checked 
- *Email addresses* - A list of email addresses to notify
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Update Instances" action while applying the policy, the identified instances will be resized based on user defined standards.

## Supported Clouds

- Amazon
- Google
- Azure

## Cost

This Policy Template does not incur any cloud costs.
