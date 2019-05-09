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

- *Time Period* - Number of days to analyze
- *Cost Threshold* - All accounts below this budget will trigger an incident
- *Email addresses* - A list of email addresses to notify
- *Include Unallocated* - Boolean to include unallocated billing center. 

### Supported Clouds

- Azure Resource Manager
- Azure CSP
- Google
- Amazon

### Cost

This Policy Template does not incur any cloud costs.