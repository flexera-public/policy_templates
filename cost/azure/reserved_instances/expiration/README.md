## Azure Reserved Instances Expiration Report

**As a best practice, this policy should only be applied to the Master Account, and not to each individual RightScale Account.**

### What it does

his policy identifies all active reserved instances that will be expiring in a set number of days.

It will email the user specified in `Email addresses of the recipients you wish to notify`

### Prerequesites

- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to manage resources in the target tenant
- The following RightScale Credentials
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Azure AD Tenant ID* - the Azure AD Tenant ID used for the Azure API Authentication
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Identify RIs that are expiring in the given number of days* - Number of days before a RI expires to alert on

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Supported Clouds

- Azure

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
