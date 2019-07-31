## Cheaper Regions Policy

### What it does

This Policy Template determines which regions have cheaper alternatives by specifying the expensive region name and the cheaper region name for analysis

### Prerequesites
- The `billing_center_viewer` role
- The `policy_designer`, `policy_manager` & `policy_publisher` roles

### Functional Details

- This policy uses a hash to determine existing regions and newer compatible cheaper regions. It checks the billing center and reports on cheaper regions.
- *Estimated Savings* - is not a reflection of what you will actually save by moving the instance. It is the total cost of the instances in the current region. You will need to take into account any RI Purchases and the cost of running the instance in the new region. *You have been warned!!!*

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Billing Center Name* - The list of Billing centers to check against
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Supported Clouds

- Azure Resource Manager
- Azure CSP
- Google
- Amazon

### Cost

This Policy Template does not incur any cloud costs.
