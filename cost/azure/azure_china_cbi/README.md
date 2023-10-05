# Azure China Cloud Common Bill Ingestion

## What it does

This Policy Template is used to automatically take billing data for Azure China and send the data to Flexera CBI so that Azure China costs are visible in Flexera One.

## Functional Details

- The policy uses the Azure China Usage Report API to retrieve Azure China billing data for the current month for the provided Enrollment ID.
- The policy then sends this data, unmodified, into the Flexera Common Bill Ingestion endpoint so that the data can be ingested and then become visible on the Flexera One platform.
- The policy requires a valid Azure China EA API key credential in Flexera One

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Month To Ingest* - Whether to process bills for the current month, previous month, or a specific month.
- *Billing Period* - The year and month to process bills for in YYYY-MM format. Only relevant if Specific Month is selected for the Month To Ingest parameter. Example: 2022-09
- *Azure Enrollment ID* - Your Azure EA Enrollment ID from Azure China Billing Portal
- *Bill Connect ID* - Bill Connect ID created in CBI API. Example: cbi-oi-azure-china-*
- *Email addresses* - A list of email addresses to notify

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy, you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_ea_china`

Required permissions from the provider:

This policy will require you to generate or retrieve your Enterprise Agreement API Key with Admin permissions.

Your API Key can be retrieved from the 'Usage + charges' blade under 'Billing' in your Azure Portal.
![image](https://user-images.githubusercontent.com/92175447/203563225-e816dd01-de3c-4f2e-ac46-65d284ec9a3e.png)

## Supported Clouds

- Azure China

## Cost

This Policy Template does not incur any cloud costs.
