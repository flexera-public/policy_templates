# Alibaba Cloud Common Bill Ingestion

## What It Does

This policy template downloads cost reports from Alibaba Cloud Object Storage and sends them to Flexera Cloud Cost Optimization (CCO) via Common Bill Ingestion (CBI) so that Alibaba Cloud costs are visible in Flexera One. An incident is raised on every execution of the policy to provide status information to the user. Optionally, this incident can be emailed.

## How It Works

- The policy connects to Alibaba Cloud Object Storage to download billing reports for the specified month (or current month if none is specified).
- Reports can be processed either as daily files (one per day of the month) or as a single monthly file, depending on configuration.
- The policy sends these reports unmodified into a Flexera CBI endpoint so they can be ingested and made visible on the platform.

## Input Parameters

This policy template has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when billing data is uploaded
- *Month To Ingest* - Whether to process bills for the current month, previous month, or a specific month
- *Billing Period* - Month to process bills for in YYYY-MM format. Only relevant if Specific Month is selected for Month To Ingest parameter. Example: 2020-01
- *Flexera CBI Endpoint* - The name of the Flexera CBI endpoint to use. Example: cbi-oi-alibaba-alibabacloud
- *Frequency* - Whether cost reports are generated monthly (single file for the month) or daily (one file per day)
- *Alibaba Cloud Account ID* - Account ID for the Alibaba Cloud Account
- *Alibaba Cloud Region* - Region of the Alibaba Cloud Object Storage bucket containing the cost reports. Example: oss-cn-shanghai
- *Alibaba Cloud Billing Report Bucket* - Alibaba Cloud Object Storage bucket containing the billing reports. Example: flexera-billing-data
- *Alibaba Cloud Billing Report Path* - The path within the Alibaba Cloud Object Storage bucket containing the Billing reports. Leave blank if reports are at the root level. Example: /billing

## Policy Actions

- Upload Alibaba Cloud bills to Flexera Cloud Cost Optimization (CCO)
- Send an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Alibaba Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has access to read objects from the Alibaba Cloud Object Storage bucket containing the billing data.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Alibaba Cloud

## Cost

This Policy Template does not incur any cloud costs
