# Currency Conversion

## What It Does

This policy template creates adjustment rules that convert the currency of the costs associated with the cost dimensions of choice. It utilizes xe.com to retrieve the latest exchange rates.

## How It Works

- This policy supports currency codes as per [ISO 4217](https://www.xe.com/iso4217.php), and uses the xe.com API to retrieve monthly average exchange rate.
- This policy supports four cloud providers natively: AWS, Azure, Google Cloud, and Oracle Cloud.
- This policy also supports custom cloud provider names to handle specialized use cases.
- This policy creates an adjustment rule for currency conversion using the exchange rate from xe.com.
- This policy can create such adjustment rules for the current month or backfill previous months.
- This policy can also set the Flexera CCO user interface to present all costs in the currency that costs are being converted to.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Backfill Adjustments* - Whether to add/modify currency conversion to just the current month or to backfill previous months.
- *Backfill Start Date* - The month and year in YYYY-MM format to backfill adjustments to. Only applicable if `Backfill Previous Months` is selected for the `Backfill Adjustments` parameter.
- *Backfill Exchange Rates* - Whether or not to use the current exchange rate, or the exchange rate at the time, when applying currency conversion to previous months. Only applicable if `Backfill Previous Months` is selected for the `Backfill Adjustments` parameter.
- *Dimensions* - The Flexera CCO cost dimension names/ids and values to apply the currency conversion to in 'Dimension=Value' format. Example: Cloud Vendor=AWS
- *Dimensions Boolean* - Whether to apply the currency conversion to costs that match any of the criteria in the `Dimensions` parameter or only those that match all of them. Only applicable if more than one value is specified for the `Dimensions` parameter.
- *Currency From* - Currency you want to convert from (based on ISO 4217 codes - e.g., 'USD' for US Dollar)
- *Currency To* - Currency you want to convert to (based on ISO 4217 codes - e.g., 'EUR' for Euro)
- *Set Organization Currency* - Whether or not to configure the Flexera CCO user interface to present costs in the currency specified in the `Currency To` parameter. If set to `Yes`, this will be done, and all costs in Flexera CCO for this organization will be presented in the currency costs are converted to.

## Policy Actions

- None. Currency conversion is applied during policy execution.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `enterprise_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All configured clouds

## Cost

This policy template does not incur any cloud costs.
