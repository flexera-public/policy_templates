## Azure Reserved Instances Utilization Policy Template

**As a best practice, this policy should only be applied to the Master Account, and not to each individual RightScale Account.**

### What it does

This Policy Template leverages the [Azure EA API for Reserved Instance Utilization](https://docs.microsoft.com/en-us/rest/api/billing/enterprise/billing-enterprise-api-reserved-instance-usage#request-for--reserved-instance-usage-summary). It will notify only if utilization of a RI falls below the value specified in the `Show RI's with utilization below this value` field. It examines the RI utilization for the prior 7 days (starting from 2 days ago) in making this determination.

It will email the user specified in `Email addresses of the recipients you wish to notify`

### Prerequesites

- The following RightScale Credentials
  - `AZURE_EA_KEY` - the Azure EA key for the enrollment being checked

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Enrollment ID* - the Azure EA enrollment ID
- *Show RI's with utilization below this value*
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Required RightScale Roles

- Cloud Management - Actor
- Cloud Management - Observer
- Cloud Management - credential_viewer

### Azure Required Permissions

- Microsoft.Consumption/reservationSummaries/read

### Supported Clouds

- Azure

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
