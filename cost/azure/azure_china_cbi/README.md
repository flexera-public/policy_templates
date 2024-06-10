# Azure China Cloud Common Bill Ingestion

## What It Does

This Policy Template is used to automatically take billing data for Azure China and send the data to Flexera CBI so that Azure China costs are visible in Flexera One.

## Functional Details

- The policy uses the Azure China Usage Report API to retrieve Azure China billing data for user-specified month for the provided Enrollment ID.
- The policy then sends this data, unmodified, into the Flexera Common Bill Ingestion endpoint so that the data can be ingested and then become visible on the Flexera One platform.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Month To Ingest* - Whether to process bills for the current month, previous month, or a specific month.
- *Billing Period* - The year and month to process bills for in YYYY-MM format. Only relevant if Specific Month is selected for the Month To Ingest parameter. Example: 2022-09
- *Azure Enrollment ID* - Your Azure EA Enrollment ID from Azure China Billing Portal
- *Flexera CBI Endpoint* - Name of the Flexera CBI endpoint to use. Ex: cbi-oi-azure-china-myaccount

## Policy Actions

The following policy actions are taken on execution:

- Upload Azure China billing data to Flexera One.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure China Enterprise Agreement Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_ea_china*). The API Key can be retrieved from the 'Usage + charges' blade under 'Billing' in the Azure Portal.

![image](https://user-images.githubusercontent.com/92175447/203563225-e816dd01-de3c-4f2e-ac46-65d284ec9a3e.png)

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure China

## Cost

This Policy Template does not incur any cloud costs.
