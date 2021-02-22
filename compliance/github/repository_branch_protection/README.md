# GitHub.com Repository Branches without Protection

## What it does

Gets the repositories under a list of GitHub.com Organizations and creates incidents for any that do not have protection enabled for their default branch.

## Input Parameters

1. GitHub.com Organizations to check - Example: `flexera`
1. Repositories that are whitelisted from the policy - Example: `flexera/repository-name`
1. Email address to send escalation emails to - Example: `noreply@example.com`
1. Protection Option: Enforce all configured restrictions for administrators.
1. Protection Option: Require at least this number of approving review on a pull request, before merging.
1. Automatic Actions: When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Protect Branches" action while applying the policy, all the branches that didn't satisfy the policy condition will be protected.

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

