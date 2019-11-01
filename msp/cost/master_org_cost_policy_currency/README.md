# Master Org Cost Policy with Currency Conversion

This policy allows you to set up cross organization scheduled reports that will provide summaries of cloud cost across all organizations you have access to, delivered to any email addresses you specify with all currencies converted to a single currency. The policy will report the following:

Chart of the previous 6 months of utilization based on whichever [Reporting Dimension](https://docs.rightscale.com/optima/reference/rightscale_dimensions.html) you select (only bill data and RightScale-generated dimensions are supported).  
Daily Average - Weekly: Daily average costs calculated from Monday of the previous week through today.
Daily Average - Monthly: Daily average costs calculated from the 1st of the previous month through today.
Previous - Weekly: Total costs during previous full week (Monday-Sunday).  
Previous - Monthly: Total costs during previous full month.  
Current - Weekly: Total costs during current (incomplete) week.  
Current - Monthly: Total costs during current (incomplete) month.  

We recommend running this policy on a weekly cadence and applying it to your master account.

_Note 1: The last 3 days of data in the current week or month will contain incomplete data._  
_Note 2: The account you apply the policy to is unimportant as Optima metrics are scoped to the Org._  
_Note 3: Exchange rates are calculated at execution time using [https://exchangeratesapi.io/](https://exchangeratesapi.io/)._  

## Cost Metrics

There are four cost metrics to choose from.

- Unamortized Unblended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Amortized Unblended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Unamortized Blended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.
- Amortized Blended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email list* - Email addresses of the recipients you wish to notify
- *Excluded Organizations* - Names of organizations to exclude
- *Cost Metric* -  See Cost Metrics above for details on selection.
- *Graph Dimension* - The cost dimension to break out the cost data in the embedded bar chart image
- *Currency* - Define what currency the final result should be in.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Required Permissions

This policy requires permissions to access RightScale resources (Optima).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html).

- Optima - billing_center_viewer

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.