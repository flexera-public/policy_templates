# AWS RDS Instance License Info

## What it does

This Policy Template gathers AWS RDS Instance data related to licensing.

## Functional Details

- This policy identifies all RDS instances and provides details on engine, version, license, and vCPU.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

- Read access to RDS

## Supported Clouds

- Amazon

## Cost

This Policy Template does not incur any cloud costs.
