# AWS Usage Forecast - Instance Time Used

## What It Does

This Policy Template leverages Flexera CCO APIs to produce a stacked bar chart showing projected Total Instance Time for AWS Instance Families. The policy uses the specified previous number of months, not including the current month, to to determine a straight-line forecast using a linear regression model. The user can specify which unit of time and which instance spec to use to normalize time against; for example, a chart can be produced for total instance vCPU hours. The data feeding this chart can be filtered by AWS region or Flexera Billing Center if desired. Optionally, the result can be emailed.

## How It Works

- This policy uses data up until the last full month before current date to guarantee full data.
- This policy produces a straight-line forecast by calculating a line of best fit (linear regression line) from the historical dataset and then extrapolating this to calculate forecasted costs.
- The forecast is displayed as a stacked-bar chart showing Total Instance Hours by Instance Family for the top 8 most used Instance Families. All other Instance Families will be aggregated and displayed as "Other". Values shown in the graph are for the past 12 months.
- The unit used for normalizing instance usage depends on the value of the `Instance Unit` parameter.
- The unit used for time depends on the value of the `Time Unit` parameter.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Look Back Months (#)* - Number of months into the past to use for calculating forecast.
- *Forecast Months (#)* - Number of months in the future to forecast.
- *Instance Unit* - Instance unit to normalize usage against. Supported units:
  - `Normalized Units (NFUs)` - Normalize the data against each [NFU](https://aws.amazon.com/about-aws/whats-new/2019/02/normalized-units-information-for-amazon-ec2-reservations-in-aws-cost-explorer/) of each instance.
  - `vCPUs` - Normalize the data against each vCPU of each instance.
  - `Memory (GiB)` - Normalize the data against each GiB of total memory of each instance.
- *Time Unit* - Unit of time to use for results. The `Instance Unit` will be normalized to this time unit. Units are calculated as follows:
  - `Hours` - 1 hour.
  - `Days` - 24 hours.
  - `Weeks` - 168 hours e.g. 7 days * 24 hours.
  - `Months` - 730 hours e.g. 365 days / 12 months * 24 hours.
  - `Years` - 8760 hours e.g. 365 days * 24 hours.
- *Allow/Deny Regions* - Whether to treat `Allow/Deny Regions List` parameter as allow or deny list. Has no effect if `Allow/Deny Regions List` is left empty.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Example: `US West (Oregon)`. Leave blank to check all regions.
- *Allow/Deny Billing Centers* - Whether to treat `Allow/Deny Billing Center List` parameter as allow or deny list. Has no effect if `Allow/Deny Billing Center List` is left empty.
- *Allow/Deny Billing Center List* - A list of allowed or denied Billing Center names/IDs. Leave blank to check all Billing Centers.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
