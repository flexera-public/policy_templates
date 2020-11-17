# AWS VPC Name Tag Sync

## What it does

This Policy Template is used to automatically synchronize the AWS VPC names to Cloud Management.
When applied, the policy will iterate through all VPCs in all AWS regions and ensure the matching network reference in Cloud Management has the correct name.

## Functional Details

This policy performs the following action:

- Synchronizes AWS VPC names to Networks in Cloud Management

## Input Parameters

This policy has the following input parameter required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. Click [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions) to check regions in AWS. If this field is left empty, then the policy will throw an error.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Update VPC" action while applying the policy, all the resources that didn't satisfy the policy condition will be updated.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Network name in Cloud Management updated to match VPC name in AWS

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

```javascript
{
    "Version": "2012-10-17",
    "Statement":[{
    "Effect":"Allow",
    "Action":["ec2:DescribeVpcs",
              "ec2:DescribeTags",
              "ec2:DescribeRegions"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
