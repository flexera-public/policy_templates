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


### Azure Required Permissions
- Microsoft Graph > Directory.Read.All
- (Application)[https://docs.microsoft.com/en-us/graph/api/user-get?view=graph-rest-1.0&tabs=http#permissions] > User.Read.All, User.ReadWrite.All, Directory.Read.All, Directory.ReadWrite.All

### Supported Clouds
- Azure

### Cost
This Policy Template does not incur any cloud costs.