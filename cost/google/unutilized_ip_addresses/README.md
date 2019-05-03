## Google Unutilized IP Addresses Policy

### What it does

Checks Google for Unutilized IP Addresses.

### Cloud Management Required Permissions/Google Required Permissions
- Cloud Management - The `credential_viewer`,`observer` roles
- Cloud Management - The `policy_designer`, `policy_manager` & `policy_publisher` roles
- Google - The `compute.addresses.list`, `compute.addresses.get` IAM Permissions

### Functional Details

- This policy uses Google Cloud to get a list of addresses not in use. 

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Google Cloud Project* - a Google Cloud Project name

### Supported Clouds

- Google

### Cost

This Policy Template does not incur any cloud costs.