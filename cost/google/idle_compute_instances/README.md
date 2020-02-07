# Google Idle Compute Instances Policy

## What it does

This Policy Template checks for idle instance in Google Compute Engine and then terminates them upon approval.

## Functional Details

- This policy identifies all instances reporting performance metrics to Google StackDriver and delivers a report, for instances whose CPU or Memory utilization is below the thresholds set in the **Average used memory percentage** and **Average used CPU percentage** parameters. These thresholds are what you would consider to be and idle instance.
- This policy can terminate instances after approval for instances that match the criteria.
- If you get an **N/A** in a field you will need to install the [StackDriver Agent](https://cloud.google.com/monitoring/agent/install-agent) on the instance to get those metrics.
- This policy only pulls running instances, as it is unable to get correct monitoring metrics from instances in other states

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Average used memory percentage"* - Set to -1 to ignore memory utilization
- *Average used CPU percentage* - Set to -1 to ignore CPU utilization
- *Exclusion label Key:Value* - Cloud native label to ignore instances. Format: Key:Value

## Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete all instances after approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

-  The `Monitoring Viewer` Role
-  The `compute.instances.delete` permission
-  The `compute.instances.list` permission
-  The `compute.instances.get` permission

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.
