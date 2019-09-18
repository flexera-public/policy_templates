# Google Unused CloudSQL Instances

## What it does

This Policy Template checks for idle CloudSQL instance in Google Compute Engine and then terminates them upon approval.

## Functional Details

- This policy identifies all CloudSQL reporting performance metrics to Google StackDriver and delivers a report, for instances whose connections are below the thresholds set in the **Number of connections to consider idle** parameters. These thresholds are what you would consider to be and idle instance.
- This policy can terminate instances after approval for instances that match the criteria.
- This policy only pulls running CloudSQL instances, as it is unable to get correct monitoring metrics from instances in other states

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Number of connections to consider idle* - Number of database connections to consider a db is unused.
- *Google Cloud Project* - a Google Cloud Project name
- *Exclusion label Key:Value* - Cloud native label to ignore instances. Format: Key:Value

### Cloud Management Required Permissions/Google Required Permissions

- Cloud Management - The `credential_viewer`,`observer` roles
- Google - The `Monitoring Viewer` Role, and the `sqlservice.admin` permissions

### Supported Clouds

- Google

### Cost

This Policy Template does not incur any cloud costs.
