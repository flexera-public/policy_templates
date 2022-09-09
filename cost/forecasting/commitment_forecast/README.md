# Vendor Commitment Forecast

## What it does

This Policy uses Optima to determine a forecast against the commitment amount agreed with your Cloud Service Provider/s. This policy allows the user to specify a Commitment target value, and track the current commitment spend to date, as well as projected commitment spend for a given period. The commitment amount can be measured against a specific Cloud Provider spend or for the entire Organization spend.

The policy uses the specified previous number of months, not including the current month to determine a straight-line forecast.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- This policy supports a commitment target amount for a single Cloud Service Provider (e.g., AWS) or the entire Organization.
- This policy produces a view of forecasted spend to the specified end date, based on previous spend to date from the specified start date.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Cloud Vendor* - Name of the Cloud Vendor if the Budget Scope is 'Cloud Vendor'. Example: 'AWS' or 'GCP'. Leave this blank for 'Organization' scope
- *Commitment Period Start Date* - A date in the past to generate forecast from (YYYY-MM format)
- *Commitment Period End Date* - A date in the future to forecast up to (YYYY-MM format)
- *Total Commitment Target* - Specify total commitment target for the given Cloud Vendor and the specified time period.  Currency is irrelevant; the policy will default to whichever currency is used in Optima
- *Email addresses* - A list of email addresses to notify

## Supported Clouds

- All configured clouds

## Cost

This Policy Template does not incur any cloud costs.
