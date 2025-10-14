# Spot Ocean Common Bill Ingestion

## What It Does

This policy template exposes costs from the Spot Ocean Cluster Aggregated Detailed Costs API and pushes them into the Flexera Bill Upload API.

## How It Works

- The policy retrieves cost data from the Spot Ocean API.
- It processes and formats the data according to the Flexera Common Bill Ingestion (CBI) format.
- The policy uploads the formatted cost data to the Flexera Bill Upload API.
- An email notification is sent indicating the status of the bill upload.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allow/Deny Spot Accounts* - Allow or Deny entered Spot Accounts.
- *Allow/Deny Spot Accounts List* - A list of allowed or denied Spot Accounts.
- *Billing Period* - The billing period to update.
- *Billing Period - Specific Month* - The specific month to update if "Specific Month" is selected for Billing Period.
- *Reallocated Cost Granularity* - The granularity for the new line items.
- *Bill Connect ID* - The Bill Connect ID to use for reallocating costs.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Upload cost data to Flexera Bill Upload API.
- Send an email notification.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Spot Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=spotinst*) which has the following permission policies:
  - `Account Viewer` on the Spot account(s) to be used.
  OR
  - `Ocean Full Access` on the Ocean account(s) to be used.
  OR
  - `Organization Admin`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `csm_bill_upload_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Multi-Cloud

## Cost

This policy template does not incur any cloud costs.
