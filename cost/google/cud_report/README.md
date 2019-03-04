## Google Committed Use Discount (CUD) Report
 
### What it does
This policy identifies all CUDs that exist in a given GCP project and provides a report listing them all. It can optionally report on all CUDs, or only those that are active or expired.
 
### Functional Details
 
Uses the GCP API to get a list of all CUDs and report on them.
 
#### Input Parameters
 
- *CUD Status* - Allow the user to choose from "Active", "Expired", or "All"
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
 
### Required RightScale Roles
 
- policy_manager
 
### Supported Clouds
 
- Google
 
### Cost
 
This Policy Template does not incur any cloud costs.