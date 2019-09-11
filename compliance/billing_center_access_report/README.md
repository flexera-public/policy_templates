## Billing Center Access Report

**As a best practice, this policy should only be applied to the Master Account, and not to each individual RightScale Account.**

### What it does

This Policy Template can target either all Billing Centers in an Organization or target a specific Billing Center.  Child Billing Centers are supported as well.  The resulting incident is a report of all users that have access to the target Billing Center(s).  If RightScale Groups have been granted access to a Billing Center, the report will indicate which Group has delegated access to a particular user. 

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *All Billing Centers?* - report on all Billing centers, true or false.
- *Billing Center Name* - If not reporting on all Billing Centers, provide the name of a specific Billing Center
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report


### Pre-reqs

- Required roles:
  - `billing_center_admin` or `billing_center_viewer`
  - `enterprise_manager`

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
