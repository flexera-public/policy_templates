# Azure Long-Stopped Instances

## What it does

This policy checks all Azure instances that have been stopped for more than a specified period of time and Terminates them after approval.

## Functional Details

The policy leverages the Azure API to check all instances that have been stopped for longer than the specified period. If the action is approved, the instance is terminated.

### Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Stopped days* - Number of days an instance is stopped before it is added to the report
- *Azure AD Tenant ID* - the Azure AD Tenant ID used for the Azure API Authentication
- *Azure Subscription ID* - the Azure Subscription ID used for the Azure API Authentication

### Required RightScale Roles

- Cloud Management - credential_viewer

### Azure Required Permissions

- Microsoft.Compute/virtualMachines/read
- Microsoft.Compute/virtualMachines/delete

### Supported Clouds

- Azure

### Cost

This Policy Template does not incur any cloud costs.
