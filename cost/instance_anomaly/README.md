## Running Instance Count Anomaly

### What it does
This policy checks whether the number of running instances in a given account has crossed a threshold of change compared to the prior period.

### Functional Details

The policy uses CMP to determine changes in running instance count by comparing the last 30 days to the previous 30 days.  When the percentage of changes reaches the specified threshold an incident is created.
  
#### Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Threshold* - percentage of change allowed before sending report
- *Threshold check* - whether to check for increases, decreases, or both

### Required Flexera Roles

- policy_manager
- observer

### Supported Clouds

- All

### Cost

This policy does not incur any cloud costs.