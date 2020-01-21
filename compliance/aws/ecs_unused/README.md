# AWS Unused ECS Clusters

## What it does

This policy checks all ECS clusters to determine if any are unused (no registered instances, no running tasks, no pending tasks, no active services) and offers the option to delete the cluster after manual approval.

## Functional Details

The policy leverages the AWS API to determine if the ECS cluster is in use.

When an unused ECS cluster is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the cluster after manual approval if needed.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - ECS clusters with any of these tags will be ignored

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

## AWS Required Permissions

This policy requires permissions to describe AWS ECS ListClusters, DescribeClusters and DeleteCluster.
The IAM user will require the following permissions:

```javascript
{
  "Version": "2014-11-13",
  "Statement":[{
  "Effect":"Allow",
  "Action":["ecs:ListClusters",
            "ecs:DescribeClusters",
            "ecs:DeleteCluster"],
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
