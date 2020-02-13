# Google Unused CloudSQL Instances

## What it does

This Policy Template checks for unused CloudSQL instance in Google Compute Engine and then terminates them upon approval.

## Functional Details

- This policy uses the GCP API to identify unused CloudSQL instances using performance metrics from Google StackDriver and delivers a report for instances whose connections are below the thresholds set in the **DB Connections Threshold** parameter. These thresholds are what you would consider to be an used instance.
- This policy can terminate instances after approval for instances that match the criteria.
- This policy only pulls running CloudSQL instances, as it is unable to get correct monitoring metrics from instances in other states

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *DB Connections Threshold* - Number of database connections to consider a db is unused.
- *Exclusion label Key:Value* - Cloud native label to ignore instances. Format: Key:Value

## Policy Actions

- Sends an email notification
- Delete DB instances after approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `Monitoring Viewer` Role
- The `sqlservice.admin` permission
- The `resourcemanager.projects.get` permission

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.
