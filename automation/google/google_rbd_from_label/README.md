# Google Rule-Based Dimension From Project Labels

## What It Does

This policy creates and updates custom Rule-Based Dimensions that surface the specified Google Project label keys in the Flexera One platform. This allows costs to be sliced by the values of the label keys in question.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Effective Date* - The month and year in YYYY-MM format that you want the rules to apply. This should be left at its default value in most cases to ensure that the rules apply to all costs, including historical costs.
- *Label Keys* - A list of Google Project label keys to create custom Rule-Based Dimensions for.
- *Dimension Names* - A list of names to give the Rule-Based Dimensions in the Flexera platform. Enter names in the same order as the label keys in the `Label Keys` field. Dimension names will be derived from label keys directly if this list is left empty.
- *Lowercase Values* - Whether or not to normalize all values by converting them to lowercase. Note that, if the same value appears multiple times with different casing, and this option is disabled, the rule-based dimension will be rejected and this policy template will fail.

## Policy Actions

- Create/update rule-based dimensions

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `observer`
  - `billing_center_viewer`
  - `rule_based_dimensions_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
