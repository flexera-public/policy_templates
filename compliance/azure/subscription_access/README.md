## Azure Subscription Access

### What it does
This policy checks all users who have Owner or Contributor access to a given Azure subscription and creates an incident whenever that user list changes.

### Functional Details
The policy leverages the Azure RBAC API to get all the users with the given role(s) on the given subscription.
When the list of users that match the criteria changes, an incident is created and the details are reported via email. 

#### Input Parameters
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Roles to report on* - Can choose to report on Owner, Contributor, or Both 

### Required RightScale Roles
- policy_manager

### Supported Clouds
- Azure

### Cost
This Policy Template does not incur any cloud costs.