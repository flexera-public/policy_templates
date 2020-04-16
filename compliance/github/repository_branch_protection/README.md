# GitHub.com Repository Branches without Protection

## What it does

This Policy Template gets the top-level / parent Teams for a GitHub.com Org and creates an incident if any do not match the whitelisted values.

## Input Parameters

1. GitHub.com Organizations to check - Example: `flexera`
2. Branches that should be protected - Example: `master`
3. Repositories that are whitelisted from the policy - Example: `flexera/repository-name`
4. Email address to send escalation emails to - Example: `noreply@example.com`
5. Protection Option: Enforce all configured restrictions for administrators. 
6. Protection Option: Require at least this number of approving review on a pull request, before merging.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- After approval, updates branch protection rule on repositories

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
