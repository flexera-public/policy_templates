## AWS Reserved Instances Utilization Policy Template

**As a best practice, this policy should only be applied to the Master Account, and not to each individual RightScale Account.**

### What it does

This Policy Template leverages the AWS RI report. It will notify only if utilization of a RI falls below the value specified in the `Show RI's with utilization below this value` field. It will email the user specified in `Email addresses of the recipients you wish to notify`

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Show RI's with utilization below this value*
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Supported Clouds

- AWS

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
