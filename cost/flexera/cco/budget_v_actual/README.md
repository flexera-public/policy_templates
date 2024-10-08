# Monthly Actual v. Budgeted Spend Report

## Deprecated

This policy is no longer being updated.

## What It Does

This policy allows you to set up scheduled reports that will provide monthly actual v. budgeted cloud cost across all resources in the Billing Center(s) you specify, delivered to any email addresses you specify.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## How It Works

The policy will provide a report with a bar chart of actual v. budgeted spend for the current month. We recommend running this policy on a weekly cadence and applying it to your master account.

IMPORTANT: The monthly budget inputs are compared against the current month's actual cloud costs of the applied policy. As a best practice, reapply this policy on an annual basis to reflect the current year's monthly budgeted cloud costs.

_Note 1: The last 3 days of data in the current week or month will contain incomplete data._
_Note 2: The account you apply the policy to is unimportant as Optima metrics are scoped to the Org._

## Cost Metrics

There are four cost metrics to choose from.

- Unamortized Unblended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Amortized Unblended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Unamortized Blended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.
- Amortized Blended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email list* - Email addresses of the recipients you wish to notify
- *Billing Center List* - List of top level Billing Center names you want to report on. Names must be exactly as shown in Optima. Leave the field blank to report on all top level Billing Centers.
- *Cost Metric* - See Cost Metrics above for details on selection.
- *January Budgeted Cost* - January budgeted cost for corresponding Billing Center
- *February Budgeted Cost* - February budgeted cost for corresponding Billing Center
- *March Budgeted Cost* - March budgeted cost for corresponding Billing Center
- *April Budgeted Cost* - April budgeted cost for corresponding Billing Center
- *May Budgeted Cost* - May budgeted cost for corresponding Billing Center
- *June Budgeted Cost* - June budgeted cost for corresponding Billing Center
- *July Budgeted Cost* - July budgeted cost for corresponding Billing Center
- *August Budgeted Cost* - August budgeted cost for corresponding Billing Center
- *September Budgeted Cost* - September budgeted cost for corresponding Billing Center
- *October Budgeted Cost* - October budgeted cost for corresponding Billing Center
- *November Budgeted Cost* - November budgeted cost for corresponding Billing Center
- *December Budgeted Cost* - December budgeted cost for corresponding Billing Center

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
