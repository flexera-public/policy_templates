## Google Committed Use Discount (CUD) Expiration Report
 
####  As a best practice, this policy should only be applied to the Master Account.
 
### What it does
This policy identifies all active CUDs that exist in a given GCP project that will be expiring in a set number of days.
 
### Functional Details
 
- Uses the GCP API to get a list of all CUDs and report on them.
- Create a service account (if none exist) with `owner` role under Google-cloud platform (IAM & admin -> service accounts). Generate key, a JSON file will get downloaded in which you can find 'client email' and 'private key' which has to be added as credentials in RightScale cloud management Design -> Credentials with name 'GC_SA_CLIENT_EMAIL' and 'GC_SA_PRIVATE_KEY' respectively.  
 
#### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Google Cloud Project* - Google cloud project Id where CUD's exist.
- *Identify CUDs that are expiring in the given number of days* - Number of days before a CUD expires to alert on
 
### Required RightScale Roles
 
- credential_viewer
 
### Supported Clouds
 
- Google
 
### Cost
 
This Policy Template does not incur any cloud costs.

### Prerequisite to apply this policy

- Add New credentials (GC_SA_CLIENT_EMAIL and GC_SA_PRIVATE_KEY) *if does not exists* under RightScale cloud management Design -> Credentials. 
- The value for credentials can be found in IAM & admin -> service accounts under Google-cloud platform.
