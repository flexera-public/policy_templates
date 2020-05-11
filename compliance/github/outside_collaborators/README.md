# GitHub.com Unpermitted Outside Collaborators

## What it does

This Policy Template will get all the Outside Collaborators (User that have been granted access to a repository, but are not a Member of the repository owner's Organization) under GitHub.com Organization(s) and creates an incident for each that are not included in the specified username whitelist.

## Input Parameters

1. GitHub.com Organizations to check - Example: flexera
1. Whitelisted Outside Collaborators - Example: flexera-ci
1. Email address to send escalation emails to - Example: noreply@example.com

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html)
for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no
credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed: 

Provider tag value to match this policy: `github`

Required permissions in the provider:

This policy requires permissions to access GitHub.com API as the Owner of the Organization(s).

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
