## Scheduled Report with Markups 

### What it does

This Policy Template leverages the the Righscale cost API's to import Cloud vendor services import service costs and add a markup or Mardown by category.   

### Prerequesites

- As this policy invoques the Rightscale API´s, the user invoquing the policy must have access to the Optima module and and copmponents.

### Categories 
For a detailed explanation regarding catgories and their mapping to the different cloud service please check the following link:
https://helpnet.flexerasoftware.com/Optima/#helplibrary/RightScale_generated_Cost_Dimension__Category.htm#optimabilling_3089684038_1151644%3FTocPath%3DOptima%2520Billing%2520Centers%2520Guide%7CCost%2520Dimensions%7CRightScale-generated%2520Cost%2520Dimension%253A%2520Category%7C_____0

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
- *Cost Metric* -  See Cost Metrics above for details on selection.
- *Compute mark up or Mark Down percentage* - mark up for the Compute category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *Application Service mark up or Mark Down percentage* - mark up for the Application service category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *Database mark up or Mark Down percentage* - mark up for the Database category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *Network mark up or Mark Down percentage* - mark up for the Network category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *Storage mark up or Mark Down percentage* - mark up for the Storage category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *Reserved Instances mark up or Mark Down percentage* - mark up for the Reserved Instances category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *GENERAL MARKUP OR MARKDOWN PERCENTAGE* - general markup for the rest of the categories in number value (20 being 20% markup -20 being a 20% markdown). Any category that has 0 as a markup percentage will have this value as a Markup/down
- *Admin mark up or Mark Down percentage* - mark up for the Admin category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *Artificial Intelligence mark up or Mark Down percentage* - mark up for the Artificial Intelligence category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *Application mark up or Mark Down percentage* - mark up for the Artificial Intelligence category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *Marketplace mark up or Mark Down percentage* - mark up for the Marketplace category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *Streaming mark up or Mark Down percentage* - mark up for the Streaming category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *Support mark up or Mark Down percentage* - mark up for the support category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *IOT mark up or Mark Down percentage* - mark up for the IOT category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).
- *Other mark up or Mark Down percentage* - mark up for the Other category in number value (20 being 20% markup -20 being a 20% markdown. Leave 0 to apply the general markUp).


### Required Permissions

This policy requires permissions to access RightScale resources (Optima).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Optima - billing_center_viewer

### Supported Clouds


- AWS
- Azure
- Google

### Cost

This Policy Template does not incur any cloud costs.
