# AWS Publicly Accessible RDS Instances

## What it does

This policy checks all Relational Database Service (RDS) instances and reports on any that are publicly accessible. When such an instance is detected, the user can choose to disable the publicly accessible option and the user can also choose to delete by enabling 'delete action' option as mentioned in Enable delete action section below.

## Functional Details

When a publicly accessible RDS instance is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have an option to modify configuration after manual approval, and even Users can perform delete action if required.

- *remove public access rule* - modifies the configuration of the RDS instance by disabling the public access rule

## Input Parameters

- *Allowed Regions* - A list of allowed regions for an AWS account. Click [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) to check regions in AWS and enter the region code. If this field is left empty, then the policy will throw an error.
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Tags to ignore* - List of tags that will exclude resources from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Update RDS Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be updated.

## Policy Actions

- Sends an email notification
- Disable the publicly accessible RDS instances after approval
- Delete publicly accessible RDS instances after approval

Note:

- RDS Instances with 'DB Instance Status' other than 'Available' and RDS instances with 'Delete Protection Enabled' cannot be deleted
- RDS instances with 'DB Instance Status' other than 'Available' can not be modified.
- When delete action is performed, DB snapshot gets created with name '<--RDS Instance Name-->-finalSnapshot' Ex mySQL-DBinstance-finalSnapshot before deleting DB instance.
- For Aurora instance, policy creates Cluster snapshot Since DB instance snapshot cannot be created directly.

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
  "Action":["rds:DescribeDBInstances",
            "rds:ListTagsForResource",
            "rds:ModifyDBInstance",
            "rds:CreateDBClusterSnapshot",
            "rds:DescribeDBClusterSnapshots",
            "rds:DeleteDBInstance"],
    "Resource":"*"
    },
    {
      "Effect":"Allow",
      "Action":["ec2:DescribeRegions"],
      "Resource":"*",
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
