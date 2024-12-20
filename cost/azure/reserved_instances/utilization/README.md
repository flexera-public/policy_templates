# Azure Reserved Instances Utilization

## What It Does

This Policy Template leverages the Azure Cost Management APIs ([Reservation Transactions](https://learn.microsoft.com/en-us/rest/api/consumption/reservation-transactions/list?view=rest-consumption-2023-05-01&tabs=HTTP) and [Reservation Summaries](https://learn.microsoft.com/en-us/rest/api/consumption/reservations-summaries/list?view=rest-consumption-2023-05-01&tabs=HTTP#reservationsummariesdailywithbillingaccountid)). It will notify only if utilization of a Reserved Instance (RI) falls below the value specified in the `Maximum Reservation Utilization Threshold` field. It examines the RI utilization for the prior 7 days or 30 days (starting from 2 days ago) in making this determination.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Azure Endpoint* - Azure Endpoint to access resources
- *Look Back Period* - Number of days of prior Azure Reservation usage to analyze.
- *Maximum Reservation Utilization Threshold* - Show Reservations with utilization below this value (%).
- *Email addresses to notify* - A list of email addresses to notify.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Billing/billingAccounts/read`
  - `Microsoft.Consumption/reservationTransactions/read`
  - `Microsoft.Consumption/reservationSummaries/read`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
