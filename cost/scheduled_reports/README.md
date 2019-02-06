# Scheduled Report

This policy allows you to set up scheduled reports that will provide summaries of cloud cost across all resources in the billing centers you specify, delivered to any email addresses you specify. The policy will report the following:

Daily average cost across the last week and last month
Total cost during previous full week (Monday-Sunday) and previous full month
Total cost during current (incomplete) week and month

Please note that the last 3 days of data in the current week or month will contain incomplete data.

We recommend running this policy on a weekly cadence.

## Cost Metrics

There are four cost metrics to choose from.

- Unamortized Unblended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Amortized Unblended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Unamortized Blended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.
- Amortized Blended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email list* - Email addresses of the recipients you wish to notify
- *Billing Center List* - List of top level Billing Center names you want to report on.  Names must be exactly as shown in Optima.  
Leave the field blank to report on all top level Billing Centers.
- *Cost Metric* -  See Cost Metrics above for details on selection.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Required Permissions

This policy requires permissions to access RightScale resources (optima).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Optima - billing_center_viewer

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
