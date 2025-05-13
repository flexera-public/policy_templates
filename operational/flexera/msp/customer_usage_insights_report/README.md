# MSP Customer Usage Insights Report

## What It Does

This policy generates a comprehensive report on the usage of MSP Customer Organizations. It provides operational capabilities related to managing MSP Customer Organizations, including cost analysis and user activity metrics.

## How It Works

- The applied policy retrieves a list of MSP Customer Organizations.
- It gathers cost data for each organization, broken down by billing source (e.g., AWS, Azure, GCP, Oracle).
- It calculates user activity metrics, including the number of active and inactive users.
- The applied policy generates a detailed markdown report summarizing the costs and user activity for each organization.
- It estimates 12-month costs using the most recent 3 months of costs.
- It identifies organizations with 100% inactive users and includes their total costs in the report.
- It allows excluding organizations with total costs below a specified threshold.
- It allows excluding certain costs from the net cost calculations and reports excluded costs separately.

## Input Parameters

This policy has the following input parameters required when applying the policy template:

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Allow/Deny Child Orgs* - Determines whether the Allow/Deny Child Orgs List parameter functions as an allow list (only providing results for the listed organizations) or a deny list (providing results for all organizations except for the listed organizations).
- *Allow/Deny Child Orgs List* - A list of allowed or denied Child Organizations to include in the report.
- *Prefix String* - Prefix to indicate the Group should be synced. This is the first part of the string that needs to be in the description.
- *Excluded User Regex* - A list of email regex patterns to exclude from the active/inactive user counts. We generally recommend always including `.*@flexera.com` to exclude Flexera employees from the counts. Add any other regex patterns for "internal" users that should be excluded from the active/inactive user counts.
- *Included User Regex* - A list of email regex patterns to include in the active/inactive user counts. This is useful for specifically including certain users, especially when using exclusions. Default is `.*` which includes all users not explicitly excluded.
- *Active Days Threshold* - The number of days to consider a user as active. Default is 30 days.
- *Processed Spend Threshold* - The minimum total processed spend for an organization to be included in the report. Default is -1 which disables the threshold and shows all Orgs.
- *Billing Period* - The billing period to report on. Options are "Previous Month", "Previous 12 Months", or "Specific Month".
- *Specific Period* - If "Specific Month" is selected for Billing Period, specify the month in YYYY-MM format.
- *Contractual Exclusions* - A list of cost types to exclude from invoiceable processed spend calculations. Options include "Tax" and "Marketplace". These exclusions are typically only for legacy agreements.
- *Get Customer Org Processed Spend from MSP Parent Org* - Select whether to get customer org processed spend from the MSP parent org or from customer orgs directly. Default is "No" which gets costs from both the parent org and customer orgs.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `org_owner`*

  \* `org_owner` role in the MSP Parent Org always required. If parameter `Get Customer Org Costs from MSP Parent Org` is set to `true`, then the `org_owner` must be granted to the identity in all Child Orgs in addition to MSP Parent Org.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All Clouds

## Cost

This policy template does not incur any cloud costs.
