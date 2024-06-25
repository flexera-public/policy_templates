# GitHub.com Repository Branches without Protection

## What It Does

Gets the repositories under a list of GitHub.com Organizations and creates incidents for any that do not have protection enabled for their default branch.

## Input Parameters

1. GitHub.com Organizations to check - Example: `flexera`
1. Branches that should be protected - Example: `master`
1. Include default branch regardless of branches list.
1. Repositories that are whitelisted from the policy - Example: `flexera/repository-name`
1. Email address to send escalation emails to - Example: `noreply@example.com`
1. Protection Option: Enforce all configured restrictions for administrators.
1. Protection Option: Require at least this number of approving review on a pull request, before merging.
1. Automatic Actions: When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Protect Branches" action while applying the policy, all the branches that didn't satisfy the policy condition will be protected.

## Policy Actions

- Sends an email notification.
- Updates branch protection rule on repository after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**GitHub Credential**](https://docs.flexera.com/flexera/EN/Automation/GenericCredentials.htm#automationadmin_1982464505_1121389) (*provider=github*) which has the following permissions:
  - `Organization Owner`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- GitHub

## Cost

This Policy Template does not incur any cloud costs.
