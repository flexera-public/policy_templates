## Low Service Usage Policy

### What it does

This Policy Template reports on services with low usage. Low usage of a specific service in a region by an account is often indicative of tests or experiments by users, which often are forgotten and left running. Investigate this usage to determine if it should be terminated or potentially consolidated into a larger account/region for ease of management.

### Prerequesites
- The `billing_center_viewer` role
- The `policy_designer`, `policy_manager` & `policy_publisher` roles

### Functional Details

- This policy queries optima data to determine low account usage. 

#### Input Parameters

This policy has the following input parameters required when launching the policy.
- *Low Service Spend Threshold* - Estimated run-rate below which a service should be reviewed for wasted usage. Example: 100.0
- *Email addresses* - A list of email addresses to notify
- *Billing Center Name* - List of Billing Center Names to check
- *Minimum Savings Threshold* - Specify the minimum monthly savings value required for a recommendation to be issued, on a per resource basis. Note: this setting applies to all recommendations. Example: 1.00

### Supported Clouds

- Azure Resource Manager
- Azure CSP
- Google
- Amazon

### Cost

This Policy Template does not incur any cloud costs.