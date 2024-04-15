# Azure Usage Report - Number of Instance vCPUs Used

## What It Does

This Policy Template leverages Flexera CCO APIs to produce a stacked bar chart showing Total Instance vCPUs for Azure Virtual Machine Families used per month for the last 12 months.
This policy allows the user to specify a *Region* to filter results by, and will email the user specified in *Email addresses to notify*.

## How It Works

- This policy supports a single Azure region or the entire Organization.
- This policy produces a stacked-bar chart showing Total Instance vCPUs by Virtual Machine Family for the top 8 most used Virtual Machine Families. All other Virtual Machine Families will be aggregated and displayed as "Other". Values shown in the graph are for the past 12 months.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allow/Deny Regions* - Allow or Deny entered regions.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Example: 'US East'. Leave blank to check all regions.
- *Allow/Deny Billing Centers* - Allow or Deny entered Billing Centers.
- *Allow/Deny Billing Center List* - A list of allowed or denied Billing Center names/IDs. Leave blank to check all Billing Centers.
- *Email addresses to notify* - A list of email addresses to notify.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
