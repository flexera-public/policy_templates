## Expired Reserved Instances Policy Template

**As a best practice, this policy should only be applied to the Master Account, and not to each individual RightScale Account.**

### What it does

This Policy Template leverages the RI report. It will notify only if expiration is within the timeframe specified in `Number of days to prior to expiration date to trigger incident` field. It will email the user specified in `Email addresses of the recipients you wish to notify`.  

This policy uses the Optima Bill Data for AWS Reserved Instance.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Number of days to prior to expiration date to trigger incident* - enter the number of days you want before the Reserved Instance expires.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Supported Clouds

- AWS

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
