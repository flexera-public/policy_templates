# GitHub Repository Branches Without Protection

## What It Does

This policy template reports on any repository branches under the user-specified GitHub organizations that do not have protection enabled. Optionally, this report can be emailed and the user can enable protection on these branches.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *GitHub Organizations* - A list of GitHub Organizations to check.
- *Allow/Deny GitHub Repositories* - Whether to treat Allow/Deny GitHub Repositories List parameter as allow or deny list. Has no effect if Allow/Deny GitHub Repositories List is left empty.
- *Allow/Deny GitHub Repositories List* - Filter results by GitHub repository, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the GitHub repositories in the specified organizations.
- *Protected Branches* - GitHub branches that should be protected.
- *Protect Default Branch* - Whether the default branch should be protected or not.
- *Enforce Restrictions On Admins* - When protecting branches, whether to enforce all configured restrictions for administrators.
- *Required Reviews (#)* - When protecting branches, number of approving reviews to require on a pull request before merging. Set to '0' to disable this requirement.
- *Require Code Owner Review* - When protecting branches, whether to require the code owner perform a review before merging.
- *Dismiss Stale Reviews* - When protecting branches, whether to dismiss stale reviews.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Protect Branches" action while applying the policy, all the GitHub branches that do not have protection enabled will have it enabled.

## Policy Actions

- Sends an email notification.
- Updates branch protection rule on repository after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**GitHub Credential**](https://docs.flexera.com/flexera/EN/Automation/GenericCredentials.htm#automationadmin_1982464505_1121389) (*provider=github*) which has the following permissions:
  - `admin:org`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- GitHub

## Cost

This policy template does not incur any cloud costs.
