# Flexera FOCUS Report

## What It Does

This policy generated a report of aggregated billing data for either the current month or a user-specified month that is compliant with the FinOps Foundation's [FinOps Cost and Usage Specification](https://focus.finops.org/#specification), also known as FOCUS. The user can filter this report by billing center and report on either amortized or unamortized costs by using the appropriate parameters.

## How It Works

- The policy gathers currency information from the [Flexera Bill Analysis API](https://reference.rightscale.com/bill_analysis/).
- The policy then makes an API request to the [Flexera Bill Analysis API](https://reference.rightscale.com/bill_analysis/) to gather aggregated costs for the relevant month. The Flexera dimensions specified in the request body are equivalent to various FOCUS dimensions.
- The results of the above are then normalized to match the FOCUS specification.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Billing Month* - Billing month to report on in YYYY-MM format. Leave blank to do current month.
- *Amortization* - Whether to report costs amortized or unamortized.
- *Billing Centers* - List of Billing Center names/IDs to report on. Leave empty to report on the entire organization without filtering by Billing Center.

## Policy Actions

The following policy actions are taken automatically upon completion:

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This Policy Template does not incur any cloud costs.
