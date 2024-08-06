# Vendor Spend Commitment Forecast

## What It Does

This policy template calculates the total projected spend for the user-specified cloud vendor (or all spend if no vendor is specified) for the specified time period and compares that projection to a user-specified commitment target. The results, along with a chart, are provided in a report. Optionally, this report can be emailed.

The purpose of this policy template is to assist in tracking and projecting total spend with a cloud vendor to ensure that any discounts due to spend commitments are not lost due to insufficient spend.

## How It Works

Projected spend is extrapolated from the spend of whatever portion of the specified time period is in the past. Future spend is assumed to be straight-forwardly commensurate with past spend. For example, if the time period specified is for 1 year, and 1 month has passed, then the projected spend will be the spend for that month multiplied by 12.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to send the report to.
- *Total Commitment Target* - The total commitment target for the specified time period. Value should be in the currency the Flexera One organization is configured to use.
- *Cost Metric* - Cost metric to use for the report. `Unamortized Unblended` is recommended for accuracy.
- *Commitment Period Start Date* - Start date for the Commitment Period in YYYY-MM format. Example: 2024-01
- *Commitment Period End Date* - End date for the Commitment Period in YYYY-MM format. Example: 2025-01
- *Cloud Vendor* - Cloud Vendor to report on. Examples: AWS, Azure, GCP. Leave blank to report on all vendors.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All

## Cost

This Policy Template does not incur any cloud costs.
