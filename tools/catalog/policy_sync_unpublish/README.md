# Policy Template Synchronization - Unpublish

## What It Does

This Policy Template can be used to remove policy templates in your account that are not present in GitHub. It uses a JSON file stored in the GitHub repository to determine a set of Flexera's current policy templates and then compares them with your current account policies to take appropriate action.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *GitHub Organization Name* - Name of the GitHub organization containing the policy repository.
  - **Example highlighted in URL:** github.com/`flexera-public`/policy_templates/tree/master
- *GitHub Repository Name* - Name of the policy repository on GitHub.
  - **Example highlighted in URL:** github.com/flexera-public/`policy_templates`/tree/master
- *GitHub Branch Name* - Name of the Github branch to pull the active policy JSON file from.
  - **Example highlighted in URL:** github.com/flexera-public/policy_templates/tree/`master`
- *Active Policy JSON* - Path to the active policy list JSON file.
  - **Example:** data/active_policy_list/active_policy_list.json
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Unpublish Policy Templates" action while applying the policy, all published templates not present in the active policy JSON file will be unpublished.

## Policy Actions

- Sends an email notification.
- Unpublish policy templates with user approval.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `policy_designer`
  - `policy_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This Policy Template does not incur any cloud costs.
