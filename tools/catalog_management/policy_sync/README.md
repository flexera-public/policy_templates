# Policy Template Synchronization

## What It Does

This policy template synchronizes the policy templates in a Flexera organization to a GitHub repository. This includes publishing new templates, updating existing templates, and unpublishing defunct templates. It uses a JSON file stored in the GitHub repository to determine a set of current policy templates and then compares them with your current account policies to take appropriate action.

__NOTE: It is recommended that this policy template be used alongside the [Hidden Policy Templates](https://github.com/flexera-public/policy_templates/tree/master/tools/catalog_management/hidden_policies) policy template to ensure that updated policy templates do not go unpublished due to being hidden in the catalog. Automatic actions for `Hidden Policy Templates` should be enabled to either unhide or delete hidden catalog policy templates.__

## How It Works

- The policy pulls a list of active policy templates from the GitHub repository specified in the user parameters.
- The policy pulls a list of policies in the catalog using the [Flexera Automation Policy API](https://reference.rightscale.com/governance-policies/).
- The above lists are compared.
  - Anything currently in the catalog but not in the active policy template list is flagged to be unpublished.
  - Anything missing from the catalog but present in the active policy template list is flagged to be published.
  - Anything in both lists but whose "updated_at" field is more recent in the active policy template list than in the catalog list is flagged to be published.
  - All other policy templates are ignored and not included in the results.
- Two incidents are potentially raised; one incident contains a list of policy templates to be published, and the other contains a list of policy templates to be unpublished.
- If automatic actions were selected via the `Automatic Actions` parameter, the listed policy templates will be published or unpublished respectively.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *GitHub Organization Name* - Name of the GitHub organization containing the policy repository.
  - **Example highlighted in URL:** github.com/`flexera-public`/policy_templates/tree/master
- *GitHub Repository Name* - Name of the policy repository on GitHub.
  - **Example highlighted in URL:** github.com/flexera-public/`policy_templates`/tree/master
- *GitHub Branch Name* - Name of the GitHub branch to pull the active policy JSON file from.
  - **Example highlighted in URL:** github.com/flexera-public/policy_templates/tree/`master`
- *Active Policy JSON Path* - Path to the active policy list JSON file in the GitHub repository.
  - **Example:** data/active_policy_list/active_policy_list.json
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Unpublish Defunct Policy Templates" action while applying the policy, all published templates not present in the active policy JSON file will be unpublished.

## Policy Actions

- Sends an email notification.
- Publish new policy templates and update existing published policy templates with user approval.
- Unpublish defunct policy templates with user approval.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `policy_designer`
  - `policy_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.
