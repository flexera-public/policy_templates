## Reserved Instances Report by Billing Center

**As a best practice, this policy should only be applied to the Master Account, and not to each individual RightScale Account.**

### What it does

This Policy Template generates a custom Reserved Instances report.  The Policy will index all Reserved Instances and then report on only the Reserved Instances that exist within an AWS Account that has been allocated to a specific Billing Center. Currently, only top-level Billing Centers are supported.

**Note:** For the most reliable data, target Billing Centers that are configured with account-based Allocation Rules only.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Billing Center Name* - enter the Billing Center Name to run the report agains
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Required RightScale Roles
 
- Cloud Management - Actor
- Cloud Management - Observer
- Cloud Management - credential_viewer

### Supported Clouds

- AWS

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
