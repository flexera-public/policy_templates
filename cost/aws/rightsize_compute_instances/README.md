# AWS Rightsize Compute Instances

## What it does

This policy checks all the instances in an AWS Account for CPU and Memory usage over the last 30 days. If the usage is less than the user provided Idle Instance CPU/Memory percentage threshold then the Virtual Machine is recommended for termination. If the usage is less than the user provided Underutilized Instance CPU/Memory percentage threshold then the Virtual Machine is recommended for downsizing. Both sets of Virtual Machines returned from this policy are emailed to the user.

## Functional Details

- The policy leverages the AWS API to check all instances and then uses the AWS CloudWatch API to check the instance average CPU and Memory utilization over the past 30 days.
- The utilization data is provided for the following statistics: Average, 99th percentile, 95th percentile, 90th percentile.
- The policy identifies all instances that have CPU utilization and/or Memory utilization below the Idle Instance CPU/Memory Threshold/s defined by the user, to provide a recommendation.
- (Coming soon) The recommendation provided for Idle Instances is a termination action. These instancse can be terminated in an automated manner or after approval.
- The policy identifies all instances that have CPU utilization and/or Memory utilization below the Underutilized Instance CPU/Memory Threshold/s defined by the user, to provide a recommendation.
- (Coming soon) The recommendation provided for Inefficient/Underutilized Instances is a downsize action. These instancse can be downsized in an automated manner or after approval.
