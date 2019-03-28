## AWS Unused  ELB (CLB) 
 
### What it does
This policy checks all  ELB (CLB) to determine if any are unused (have no healthy instances) and allows them to be deleted by the user after approval.
 
### Functional Details
 
The policy leverages the AWS EC2 API to determine if the  ELB (CLB) is in use.
 
When an unused  ELB (CLB) is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the  ELB (CLB) after manual approval if needed.
 
#### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* -  ELB (CLB) with any of these tags will be ignored 
 
### Required RightScale Roles
 
- policy_manager
 
### Supported Clouds
 
- AWS
 
### Cost
 
This Policy Template does not incur any cloud costs.