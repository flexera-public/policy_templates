# AWS Unused ECS Clusters

## What it does

This policy checks all ECS clusters to determine if any are unused (no registered instances, no running tasks, no pending tasks, no active services) and offers the option to delete the cluster after manual approval.

## Functional Details

The policy leverages the AWS API to determine if the ECS cluster is in use.

When an unused ECS cluster is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the cluster after manual approval if needed.

## Input Parameters

- *Allowed Regions* - A list of allowed regions for an AWS account. Click [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) to check regions in AWS and enter the region code. If this field is left empty, then the policy will throw an error.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - ECS clusters with any of these tags will be ignored
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Clusters" action while applying the policy, all the resources that didn't satisfy the policy condition will be deleted.

## Policy Actions

- Send an email report

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
  "Action":["ecs:ListClusters",
            "ecs:DescribeClusters",
            "ecs:DeleteCluster"],
    "Resource":"*"
    },
    {
      "Effect":"Allow",
      "Action":["ec2:DescribeRegions"],
      "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.

## Limitation

This policy generates a report of upto 100 clusters.
