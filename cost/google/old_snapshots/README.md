# Google Delete Old Snapshots

## What it does

This Policy finds Google snapshots older than the specified days and deletes them.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify
- *Snapshot age* - The number of days since the snapshot was created.
- *Exclusion Label List* - list of tags that a snapshot can have to exclude it from the list.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete old snapshots after an approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `compute.snapshots.delete` permission
- The `compute.snapshots.list` permission
- The `compute.snapshots.get` permission
- The `compute.regions.list` permission
- The `resourcemanager.projects.get` permission

## Supported Clouds

- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
