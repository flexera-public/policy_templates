# Azure New Marketplace Products

## What it does

This policy compares Azure billing data from 3 days ago to billing data from a user-specified number of days ago (10 by default) to see if any new Marketplace products have been purchased since then. A list of the new products and their estimated monthly cost is raised as an incident and, optionally, emailed.

## Functional Details

- The policy leverages the Flexera Optima API to retrieve aggregated amortized costs from each Azure bill source.
- Costs are filtered accordingly based on the kind of Azure bill source. Old bill sources pull the `usage_type` dimension and filter by the `Microsoft.Marketplace` service, while newer bill sources pull the `resource_type` dimension and filter by `manufacturer_name` not containing the substring "Microsoft".
- The list of products from 3 days ago is compared to the older list to find any new items and their cost.

### Policy Cost Reporting Details

The policy includes the estimated monthly cost. Optima is used to retrieve the cost of the Marketplace product for a full day (3 days ago) which is then multiplied by 30.44 (the average number of days in a month). The cost is displayed in the Estimated Monthly Cost column. The incident message detail includes the sum of each product *Estimated Monthly Cost* as *Potential Monthly Cost*.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Look Back Period (Days)* - How far back, in days, to look at Marketplace product purchases to see if new items have been added.
- *Minimum Cost Threshold* - Minimum monthly cost to report on new Marketplace products.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
