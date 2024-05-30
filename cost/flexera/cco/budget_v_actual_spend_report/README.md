# Budget vs Actual Spend Report

## What It Does

This policy generates an email report comparing actual spending to budgeted values. It utilizes the Flexera Budget API to gather details and sends the report via email, eliminating the need for stakeholders to log in to Flexera One for report access.

## Input Parameters

- _Report Type_: Allows selection between cumulative and monthly reporting options.
- _Budget Name or ID_: The name or ID of the target Budget.
- _Filter Group By Dimensions_: Filter by dimension=value pairs (e.g., 'Cloud Vendor=AWS'). Multiple values for the same dimension can be supplied as coma-separated list.
- _Unbudgeted Spend_: Parameter to include or exclude unbudgeted funds in the calculation.
- _Email Addresses_: A list of email addresses to notify.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Functional Details

- Chart templates are updated for improved configuration adaptability.
- Various minor enhancements and bug fixes contribute to improved stability and performance.

## Cost

This Policy Template does not incur any cloud costs.
