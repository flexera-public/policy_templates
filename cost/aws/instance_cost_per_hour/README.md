# AWS Cost Report - EC2 Instance Cost Per Hour

## What It Does

This policy template generates a report and chart showing the average AWS EC2 instance cost per hour per month going back a user-specified number of months. Instance costs are normalized to [NFUs (Normal Form Units)](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/normalization-factor-for-dedicated-ec2-instances.html). Optionally, this report, with chart, can be emailed.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Months Back* - Number of previous months to include in the report
- *Aggregation* - Whether to report the entire organization in aggregate or by Billing Center
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

This policy template does not incur any cloud costs.
