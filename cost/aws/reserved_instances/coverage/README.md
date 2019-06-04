## Reserved Instances Coverage Policy Template

### What it does

This Policy Template leverages the Reserved Instance Coverage report. Retrieves the reservation coverage for your account.
It will email the user specified in `Email addresses of the recipients you wish to notify`

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Number of days in the past to view Reserved Instance Coverage* - allowed values 7,14,30,90,180,365
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Supported Clouds

- AWS

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
