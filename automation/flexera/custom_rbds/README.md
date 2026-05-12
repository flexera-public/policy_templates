# Custom Rule-Based Dimensions

## What It Does

This policy template creates or updates a set of pre-built custom Rule-Based Dimensions (RBDs) within the Flexera organization. If a selected RBD already exists, its rules are overwritten with the pre-built version; otherwise it is created fresh. Optionally, information about the created or updated RBDs can be emailed.

__NOTE: This policy template only needs to execute once to perform the above task. It is recommended that the policy template be terminated after execution completes.__

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new Rule-Based Dimensions are created.
- *Rule-Based Dimensions (Built-In)* - The specific pre-built Rule-Based Dimensions you wish to create. Available options: AI Models, AI Tokens, AI Tools, Object Storage Tier Category, Object Storage Usage Category.
- *Rule-Based Dimensions (External)* - The full URLs of any external Rule-Based Dimension JSON files you wish to also create. External files must be publicly accessible and in JSON format matching the Flexera Rule-Based Dimensions API. The JSON file must contain `name`, `id`, and `rules` fields at the top level. Example: `https://awebdomain.com/path/rbd_file.json`
- *Effective Date* - Year/month you want the Rule-Based Dimension rules to start applying in YYYY-MM format. Defaults to `2010-01` so that rules apply to all historical cost data.

## Policy Actions

- Creates new Rule-Based Dimensions or updates the rules of existing ones
- Sends an email notification listing which Rule-Based Dimensions were created or updated

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `observer`
  - `rule_based_dimensions_manager`
  - `policy_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any additional costs.
