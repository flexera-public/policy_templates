# Hidden Policy Templates

## What It Does

This policy template reports on any policy templates in the catalog that are flagged as `hidden`. Optionally, it emails a report of these policies, unhides them, and/or deletes them from the catalog.

__NOTE: This policy template is primarily intended to be used alongside the [Policy Template Synchronization](https://github.com/flexera-public/policy_templates/tree/master/tools/catalog_management/policy_sync) policy template to ensure that updated policy templates do not go unpublished due to being hidden in the catalog. For this use case, automatic actions for `Hidden Policy Templates` should be enabled to either unhide or delete hidden catalog policy templates.__

## How It Works

- The policy pulls a list of active policy templates from the GitHub repository specified in the user parameters.
- The policy pulls a list of policies in the catalog using the [Flexera Automation Policy API](https://reference.rightscale.com/governance-policies/) with the `show_hidden` option enabled.
- The above list is filtered for just those policies with a `hidden` field set to `true`.
- If automatic actions were selected via the `Automatic Actions` parameter, the listed policy templates will be unhidden or deleted respectively.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Hidden Policy Templates" action while applying the policy, all hidden templates in the catalog will be deleted.

## Policy Actions

- Sends an email notification.
- Unhide hidden policy templates with user approval.
- Delete hidden policy templates with user approval.

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
