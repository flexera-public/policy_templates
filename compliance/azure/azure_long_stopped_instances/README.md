## Azure Long-Stopped Instances
 
### What it does
This policy is for Azure only.  This checks all instances that are stopped and reports on any that have been stopped for more than a specified period of time. The user is given the option to Terminate the instance after approval.
 
### Functional Details
 
The policy leverages the Azure API to check all instances that have been stopped for longer than the specified period. If the action is approved, the instance is terminated.
 
#### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Stopped days* - Number of days an instance is stopped before it is added to the report
 
### Required RightScale Roles
 
- policy_manager
 
### Supported Clouds
 
- Azure
 
### Cost
 
This Policy Template does not incur any cloud costs.