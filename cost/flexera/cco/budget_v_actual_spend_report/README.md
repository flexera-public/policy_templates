# Budget vs Actual Spend Report

## What It Does

This policy generates an email report comparing actual spending to budgeted values. It utilizes the Flexera Budget API to gather details and sends the report via email, eliminating the need for stakeholders to log in to Flexera One for report access.

## Prerequisites

This policy requires appropriate [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authentication. Ensure a Flexera Credential is registered, compatible with this policy.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (_provider=flexera_) which has the following roles:
  - `optima:budget:index`
  - `optima:budget:report`
  - `optima:billing_center:show`

Refer to the [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page for detailed instructions on setting up Credentials.

## Functional Details

- Chart templates are updated for improved configuration adaptability.
- Various minor enhancements and bug fixes contribute to improved stability and performance.

## Input Parameters

- _Budget Name or ID_: The name or ID of the target Budget.
- _Filter Group By Dimensions_: Filter by dimension=value pairs (e.g., 'Cloud Vendor=AWS'). Multiple values for the same dimension can be supplied as coma-separated list.
- _Unbudgeted Spend_: Parameter to include or exclude unbudgeted funds in the calculation.
- _Email Addresses_: A list of email addresses to notify.

## Cost

This Policy Template does not incur any cloud costs.
