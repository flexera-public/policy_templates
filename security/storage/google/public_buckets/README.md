# Google Open Buckets Policy Template

## What it does

This Policy Template will check your account for Google Cloud Storage buckets with public permission.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - Email to alert when it finds google buckets that meet the criteria

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

## Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- storage.buckets.list
- storage.buckets.getIamPolicy2
- Scope for the credential is <https://www.googleapis.com/auth/monitoring.write https://www.googleapis.com/auth/cloud-platform https://www.googleapis.com/auth/monitoring.read https://www.googleapis.com/auth/monitoring https://www.googleapis.com/auth/compute https://www.googleapis.com/auth/compute.readonly https://www.googleapis.com/auth/devstorage.full_control>

## Supported Clouds

- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
