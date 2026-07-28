# Azure Rule-Based Dimension For Tenant ID

## What It Does

This policy template creates and maintains a Rule-Based Dimension in Flexera Cloud Cost Optimization that shows the Azure tenant ID associated with each Azure subscription. This allows costs to be sliced, filtered, or grouped by tenant ID, which is useful for organizations that manage multiple Azure tenants. Rules added to this rule-based dimension manually, or by other policy templates, will not be deleted.

## How It Works

1. The policy retrieves all Bill Connections configured in the Flexera organization and filters them down to the Azure Bill Connections (Azure EA, Azure MCA, and Azure CSP).
1. For each Azure Bill Connection, the policy extracts the associated Azure tenant ID.
1. The policy queries Flexera CCO for the last 12 months of cost data, filtered to only the Azure Bill Connections identified above, in order to build a complete list of Azure vendor accounts (subscriptions) and the Bill Connection each one belongs to.
1. The policy combines this data into a table of vendor accounts, their Bill Connection, and the associated tenant ID.
1. The policy creates or updates a Rule-Based Dimension with one rule per vendor account, mapping the vendor account to its tenant ID.

## Input Parameters

- *Dimension Name* - The name to give the new dimension for the Azure tenant ID. This is how the dimension will appear in Flexera One.
- *Dimension ID* - The internal ID to give the new dimension for the Azure tenant ID. Default is recommended for most use cases.
- *Effective Date* - The month and year in YYYY-MM format that you want the rules to apply. This should be left at its default value in most cases to ensure that the rules apply to all costs, including historical costs. Only used when *Effective Date Mode* is set to "Static".
- *Effective Date Mode* - Whether to use the static value in the *Effective Date* parameter for all rule updates ("Static"), or to automatically use the current month (in YYYY-MM format) as the effective date each time the policy runs ("Current Month").

## Policy Actions

- Create/update rule-based dimension for Azure tenant ID.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `ca_user`
  - `billing_center_viewer`
  - `rule_based_dimensions_manager`
  - `policy_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
