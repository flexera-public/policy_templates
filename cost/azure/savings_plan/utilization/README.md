# Azure Savings Plan Utilization

## What It Does

This Policy Template leverages the Azure Billing API ([Savings Plans By Savings Plan Order](https://learn.microsoft.com/en-us/rest/api/billing/savings-plans/list-by-savings-plan-order?view=rest-billing-2024-04-01&tabs=HTTP)) to report on Savings Plan utilization. It will notify only if utilization of a Savings Plan falls below the value specified in the `Maximum Savings Plan Utilization Threshold` field. It examines the Savings Plan utilization for the prior 1 day, 7 days or 30 days in making this determination.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Look Back Period* - Number of days of prior Azure Savings Plan usage to analyze.
- *Maximum Savings Plan Utilization Threshold* - Show Savings Plans with utilization below this value (%).

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Sends an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Billing/billingAccounts/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
