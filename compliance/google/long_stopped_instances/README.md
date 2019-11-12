# Google Long-Stopped Instances

## What it does

This policy checks all Google instances that are stopped and reports on any that have been stopped for more than a specified period of time. The user is given the option to Terminate the instance after approval.

## Functional Details

The policy leverages the Google API to check all instances that have been stopped for longer than the specified period. If the action is approved, the instance is terminated.

### Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Stopped days* - Number of days an instance is stopped before it is added to the report
- *Google Cloud Project* -Google cloud project name

### Required RightScale Roles

- credential_viewer

### Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete all instances after approval

### Supported Clouds

- Google

### Cost

This Policy Template does not incur any cloud costs.