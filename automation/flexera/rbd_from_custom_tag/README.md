# Rule-Based Dimension From Custom Tags

## What It Does

This policy template creates and updates custom Rule-Based Dimensions that duplicate Custom Tags that have been configured in the Flexera platform. The user can then add or remove rules above or below the generated rules, either through automation or the Flexera One UI, to further customize the dimension; rules added to these rule-based dimensions manually, or by other policy templates, will not be deleted.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Effective Date* - The month and year in YYYY-MM format that you want the rules to apply. This should be left at its default value in most cases to ensure that the rules apply to all costs, including historical costs.
- *Custom Tags* - A list of Custom Tags keys to build Rule-Based Dimensions from. Can be either the Custom Tag name as seen in the Flexera platform or the ID returned by Flexera APIs.
- *Dimension Names* - A list of names to give the Rule-Based Dimensions in the Flexera platform. Needs to be in the same order as the 'Custom Tags' parameter. Names will be derived automatically from Custom Tag names if this list is empty.
- *Lowercase Values* - Whether or not to normalize all values by converting them to lowercase. Note that, if the same value appears multiple times with different casing, and this option is disabled, the rule-based dimension will be rejected and this policy template will fail.

## Policy Actions

- Create/update rule-based dimensions

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `observer`
  - `billing_center_viewer`
  - `rule_based_dimensions_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All

## Cost

This policy template does not incur any cloud costs.
