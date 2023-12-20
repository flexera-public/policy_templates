# Azure Expiring Savings Plans

## What It Does

This Policy Template obtains a list of all Savings Plans in the Azure estate and reports on any that have expired or are set to expire within a user-specified number of days. An email is sent containing a list of the offending Savings Plans.

## Functional Details

- The policy leverages the Azure Resource Manager API to obtain a list of Savings Plans from the `/providers/Microsoft.BillingBenefits/savingsPlans` API endpoint.
- The policy then compares the `properties.expiryDateTime` field of each Savings Plan to today's date to determine how many days from expiration each Savings Plan is.
- The policy then raises an incident with a list of any Savings Plans set to expire in fewer days than the user specified via the `Days Until Expiration` parameter.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Days Until Expiration* - The number of days before the Azure Savings Plan expires. All Savings Plans set to expire in fewer days than the specified value will be included in the report.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.BillingBenefits/savingsPlanOrders/savingsPlans/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs
