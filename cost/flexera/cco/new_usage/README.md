# New Usage

## What It Does

This policy compares billing data from 3 days ago to billing data from a user-specified number of days ago (10 by default) to see if any new usage types exist for the user-specified dimension. For example, if the user specifies the `Service` dimension, any new values for this dimension that did not exist previously will be reported. A list of the new usage types and their estimated monthly cost is raised as an incident and, optionally, emailed.

## How It Works

The policy includes the estimated monthly cost. Flexera's Cloud Cost Optimization (CCO) API is used to retrieve cloud costs for a full day (3 days ago). The daily cost of any new values for the user-specified dimension are then multiplied by 30.44 (the average number of days in a month). The cost is displayed in the Estimated Monthly Cost column. The incident message detail includes the sum of each product *Estimated Monthly Cost* as *Potential Monthly Cost*.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Dimension* - The name or ID of the Flexera dimension whose values you want to check for new usage; for example, `Service`.
- *Minimum Cost Threshold* - Minimum monthly cost to report on new usage. New usage whose estimated monthly cost is lower will not be reported.
- *Look Back Period (Days)* - How far back, in days, to compare to current usage to see if new usage has been added.
- *Cost Metric* - The cost metric to use when assessing new usage spend.
- *Allow/Deny Billing Centers* - Allow or Deny entered Billing Centers.
- *Allow/Deny Billing Center List* - A list of allowed or denied Billing Center names/IDs. Leave blank to run report across entire Flexera organization.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All

## Cost

This policy template does not incur any cloud costs.
