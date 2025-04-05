# Spot Eco - Commitment Source Dimension

## What It Does

This policy template creates a rule-based dimension in Flexera Cloud Cost Optimization that reports on whether commitments were purchased by Spot Eco or not. Costs will have one of three values for this dimension:

- "Eco" - The commitment was purchased by Spot Eco.
- "Non-Eco" - The commitment was not purchased by Spot Eco.
- "None" - The cost is not a commitment and therefore the commitment source is not applicable.

**NOTE: This policy template should be considered an alpha release and currently only works with a single Spot Eco organization. Support for multiple organizations may be added in a future iteration.**

## Input Parameters

- *Spot Organization ID* - The organization ID of the Spot Eco account to use for the commitment source.
- *Dimension Name* - The name to give the new dimension for the commitment source. This is how the dimension will appear in Flexera One.
- *Dimension ID* - The internal ID to give the new dimension for the commitment source. Default is recommended for most use cases.
- *Effective Date* - The month and year in YYYY-MM format that you want the rules to apply. This should be left at its default value in most cases to ensure that the rules apply to all costs, including historical costs.

## Policy Actions

- Create/update rule-based dimension for commitment source.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Spot Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=spotinst*) which has the following permission policies:
  - `Account Viewer` on the Spot account(s) to be used.
  OR
  - `Spot Security Full Access` on the Spot account(s) to be used.
  OR
  - `Organization Admin`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `observer`
  - `billing_center_viewer`
  - `rule_based_dimensions_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All clouds supported by Spot Eco

## Cost

This policy template does not incur any cloud costs.
