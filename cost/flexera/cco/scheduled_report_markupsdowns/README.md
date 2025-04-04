# Scheduled Report with Markups and Markdowns

## What It Does

This Policy Template leverages the the Flexera Cloud Cost Optimization APIs to import Cloud vendor services import service costs and add a markup or markdown by category.

For a detailed explanation regarding categories and their mapping to the different cloud service please check the following link: [Flexera Cloud Cost Optimization categories](https://docs.flexera.com/flexera/EN/Optima/costdimcat.htm#optimabilling_2682776915_1151644)

## Cost Metrics

There are four cost metrics to choose from.

- Unamortized Unblended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Amortized Unblended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Unamortized Blended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.
- Amortized Blended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email list* - Email addresses of the recipients you wish to notify
- *Billing Center List* - List of top level Billing Center names you want to report on.  Names must be exactly as shown in Flexera Cloud Cost Optimization. Leave the field blank to report on all top level Billing Centers.
- *Cost Metric* - See cost metrics above for details on selection.
- *Compute markup or markdown percentage* - markup for the compute category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Application Service markup or markdown percentage* - markup for the Application service category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Database markup or markdown percentage* - markup for the Database category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Network markup or markdown percentage* - markup for the Network category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Storage markup or markdown percentage* - markup for the Storage category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Reserved Instances markup or markdown percentage* - markup for the Reserved Instances category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *General markup or markdown percentage* - general markup for the rest of the categories in number value (20 being 20% markup -20 being a 20% markdown). Any category that has 0 as a markup percentage will have this value as a markup/markdown
- *Admin markup or Markdown percentage* - markup for the Admin category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Artificial Intelligence markup or markdown percentage* - markup for the Artificial Intelligence category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Application markup or markdown percentage* - markup for the Artificial Intelligence category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Marketplace markup or markdown percentage* - markup for the Marketplace category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Streaming markup or markdown percentage* - markup for the Streaming category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Support markup or markdown percentage* - markup for the support category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *IOT markup or markdown percentage* - markup for the IOT category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Other markup or markdown percentage* - markup for the Other category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This policy template does not incur any cloud costs.
