# MSP Invoiceable Spend Report

## What It Does

This policy template produces a report on MSP Customer Organization processed spend for invoicing purposes. It retrieves costs from the MSP Parent Org using the `rbd_partner_child_org` allocation dimension, breaking down spend by child organization and bill source. The report includes invoiceable spend, excluded spend (based on contractual exclusions), and total processed spend.

## How It Works

- The applied policy retrieves a list of MSP Customer Organizations from the MSP Parent Org.
- It gathers cost data from the parent org, grouped by `rbd_partner_child_org` and bill source, using a single aggregated query for performance and reliability.
- Costs not allocated to any child org are reported separately under the MSP Parent Org.
- Contractual exclusions (such as Flexera Adjustments, Tax, Marketplace, Support Charges, Credits, and Refunds) are applied to separate invoiceable spend from excluded spend.
- The applied policy generates a markdown report summarizing costs by bill connection type, bill source, currency, and organization.
- A CSV export is attached to the incident email for downstream consumption, including currency per bill source for currency conversion workflows.

## Input Parameters

This policy template has the following input parameters required when applying the policy template:

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Allow/Deny Child Orgs* - Determines whether the Allow/Deny Child Orgs List parameter functions as an allow list (only providing results for the listed organizations) or a deny list (providing results for all organizations except for the listed organizations).
- *Allow/Deny Child Orgs List* - A list of allowed or denied Child Org IDs. Leave empty for all.
- *Billing Period* - The billing period to report on. Options are "Previous Month" or "Specific Month".
- *Specific Billing Period* - If "Specific Month" is selected for Billing Period, specify the month in YYYY-MM format.
- *Contractual Exclusions* - Cost categories to exclude from invoiceable processed spend. Options include "Flexera Adjustments" (recommended default, keeps only Raw Cost), "Tax", "Marketplace", "Support Charges", "Credits", and "Refunds".
- *Additional Contractual Exclusions (JSON)* - Optional JSON filter expression for additional exclusions not covered by the checkbox options. Must be a valid `FilterV1RequestBody` object. Leave blank if not needed.
- *Bill Source Currencies* - Currency overrides for specific bill sources. Format: `bill_source_id:CURRENCY_CODE` (e.g. `cbi-oi-azure-ea-12345:AUD`). Bill sources not listed default to the Flexera Org currency.
- *Processed Spend Threshold* - Minimum total processed spend for an org to be included in the report. Use -1 to include all orgs.
- *MSP Parent Org Billing Center IDs (Override)* - Optional: billing center IDs to use when querying costs from the MSP parent org. Leave empty to auto-detect.

## Policy Actions

- Send an email report with CSV attachment

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `org_owner`

  The credential must have the `org_owner` role in the MSP Parent Org.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All Clouds

## Cost

This policy template does not incur any cloud costs.
