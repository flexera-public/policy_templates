# Google Label Cardinality Report

## What it does

This Policy Template is used to generate a label cardinality (how frequently each label value occurs) report for Google Cloud. The report includes cardinality for all label values for both Google Projects and Resources.

## Functional Details

This policy performs the following action:

- !!!Connect to the Google something API to get a list of AWS Accounts and their tags.

## Input Parameters

This policy has the following input parameter required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

This read-only policy is purely for reporting purposes and takes no action.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `Monitoring Viewer` Role
- The `compute.disks.list` permission
- The `compute.instances.list` permission
- The `compute.externalVpnGateways.list` permission
- The `compute.images.list` permission
- The `compute.snapshots.list` permission
- The `compute.vpnGateways.list` permission
- The `storage.buckets.list` permission
- The `resourcemanager.projects.get` permission

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.
