## Scheduled Report with Markups 

### What it does

This Policy Template leverages the the RightScale cost APIs to import Cloud vendor services import service costs and add a markup or markdown by category.   

### Prerequisites

- As this policy invokes the RightScale APIs, the user invoking the policy must have access to the Optima module and and components.

### Categories 
For a detailed explanation regarding categories and their mapping to the different cloud service please check the following link: [RightScale categories](https://helpnet.flexerasoftware.com/Optima/#helplibrary/RightScale_generated_Cost_Dimension__Category.htm#)

### Cost Metrics

There are four cost metrics to choose from.

- Unamortized Unblended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Amortized Unblended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Unamortized Blended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.
- Amortized Blended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.

#### Input Parameters

This policy has the following input parameters required when launching the policy.
- *Email list* - Email addresses of the recipients you wish to notify
- *Billing Center List* - List of top level Billing Center names you want to report on.  Names must be exactly as shown in Optima.  
Leave the field blank to report on all top level Billing Centers.
- *Cost Metric* - See cost metrics above for details on selection.
- *Compute markup or markdown percentage* - markup for the compute category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Application Service markup or markdown percentage* - markup for the Application service category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Database markup or markdown percentage* - markup for the Database category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Network markup or markdown percentage* - markup for the Network category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Storage markup or markdown percentage* - markup for the Storage category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Reserved Instances markup or markdown percentage* - markup for the Reserved Instances category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *GENERAL MARKUP OR MARKDOWN PERCENTAGE* - general markup for the rest of the categories in number value (20 being 20% markup -20 being a 20% markdown). Any category that has 0 as a markup percentage will have this value as a markup/markdown
- *Admin markup or Markdown percentage* - markup for the Admin category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Artificial Intelligence markup or markdown percentage* - markup for the Artificial Intelligence category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Application markup or markdown percentage* - markup for the Artificial Intelligence category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Marketplace markup or markdown percentage* - markup for the Marketplace category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Streaming markup or Markdown percentage* - markup for the Streaming category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Support markup or markdown percentage* - markup for the support category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *IOT markup or markdown percentage* - markup for the IOT category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).
- *Other markup or markdown percentage* - markup for the Other category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markup).

### Required Permissions

This policy requires permissions to access RightScale resources (Optima).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Optima - billing_center_viewer

### Supported Clouds

- AWS
- Azure
- Google

### Cost

This Policy Template does not incur any cloud costs.


