# Azure Reserved Instances Break Even Point Report

## What It Does

This policy template produces a report of all upfront Azure reservations along with their breakeven point in both hours and days. Optionally, this report can be emailed.

The Commitment Break Even Point is the estimated length of time to pay off the entire cost of a commitment discount (including upfront and ongoing charges) from the savings provided by that commitment. More information is available on the [FinOps Foundation website](https://www.finops.org/assets/terminology/#:~:text=Commitment%20Break%20Even%20Point).

## How It Works

- Data on reservations is pulled from both Azure directly and the Flexera platform.
- The Break Even Point in hours is calculated as follows:
  - `Cost of RI` / (`Hourly On-Demand Rate` - (`Cost of RI` / (`Reserved Hours` * `Purchased Quantity`)))
- The Break Even Point in months is calculated as follows:
  - `Break Even Point (Hours)` / (365.25 / 12 * 24)
- Reservations with no valid Break Even Point will be reported with a Break Even Point of "Never".

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - A list of email addresses to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Allow/Deny Billing Centers* - Allow or Deny entered Billing Centers.
- *Allow/Deny Billing Center List* - A list of allowed or denied Billing Center names/IDs. Leave blank to report on Reservations in all Billing Centers.

## Policy Actions

- Sends an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Capacity/reservationOrders/read`
  - `Microsoft.Capacity/reservationOrders/reservations/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
