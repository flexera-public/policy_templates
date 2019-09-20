## Google Committed Use Discount (CUD)

### What it does
This policy identifies all CUDs that exist in a given GCP project and provides a report listing them all. It can optionally report on all CUDs or only those that are active or expired.

### Functional Details

- Uses the GCP API to get a list of all CUDs and report on them.
- Create a service account (if not exists) with owner role under Google-cloud platform (IAM & admin -> service accounts). Generate key, a JSON file will get downloaded in which you can find 'client email' and 'private key' which has to be added as credentials in RightScale cloud management Design -> Credentials with name 'GC_SA_CLIENT_EMAIL' and 'GC_SA_PRIVATE_KEY' respectively.  

#### Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Google Cloud Project* - Google cloud project Id where CUD's exist.
- *CUD Status* - Allow the user to choose from "All", "Active" or "Expired"

### Required RightScale Roles

- policy_manager

### Supported Clouds

- Google

### Cost

This Policy Template does not incur any cloud costs.

### Prerequisite to apply this policy

- Add New credentials (GC_SA_CLIENT_EMAIL and GC_SA_PRIVATE_KEY) *if does not exists* under RightScale cloud management Design -> Credentials.
- The value for credentials can be found in IAM & admin -> service accounts under Google-cloud platform.

Note: The Service Account in GCP should have *owner role*
