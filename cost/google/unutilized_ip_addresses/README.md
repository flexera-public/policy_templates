## Google Unutilized IP Addresses Policy

### What it does

Checks Google for Unutilized IP Addresses and deletes them after approval.

### Cloud Management Required Permissions/Google Required Permissions
- Cloud Management - The `credential_viewer`, `observer` roles
- Cloud Management - The `policy_designer`, `policy_manager` & `policy_publisher` roles
- Google - The `compute.addresses.list`, `compute.addresses.get`, and `compute.addresses.delete` IAM Permissions

### Functional Details

- This policy uses Google Cloud to get a list of IP addresses, internal and external, that are not in use. 
- Create a service account (if not exists) with the necessary permissions under Google-cloud platform (IAM & admin -> service accounts). Generate key, a JSON file will get downloaded in which you can find 'client email' and 'private key' which has to be added as credentials in RightScale cloud management Design -> Credentials with name 'GCE_PLUGIN_ACCOUNT' and 'GCE_PLUGIN_PRIVATE_KEY' respectively.  

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Google Cloud Project* - The Google Cloud Project name
- *Exclusion Label Key:Value* - A Google native label to ignore IP addresses that you don't want to consider for deletion

### Supported Clouds

- Google

### Cost

This Policy Template does not incur any cloud costs.