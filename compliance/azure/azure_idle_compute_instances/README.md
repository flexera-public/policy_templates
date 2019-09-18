# Azure Idle Compute Instances

## What it does

This policy checks all the instances in the Azure Subscription for the average CPU usage over the last hour.  If the usage is less than the user provided CPU percentage threshold then the virtual machines are recommended for deletion, and the user is emailed.

## Functional Details

The policy leverages the Azure API to check all instances and then checks the instance average CPU utilization over the past hour, finally recommending the low ones for deletion after approval.

### Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *CPU Threshold* - Percentage of CPU utilization
- *Azure Subscription ID* - Your Azure Subscription ID.  You can find it by following this guide: [Subscription ID](https://blogs.msdn.microsoft.com/mschray/2016/03/18/getting-your-azure-subscription-guid-new-portal/)
- *Azure Tenant ID* - Your Azure tenant ID.  You can find it by following this guide: [Tenant ID](https://docs.microsoft.com/en-us/onedrive/find-your-office-365-tenant-id)

### Required RightScale Roles

- `credential_viewer`

### Azure Required Permissions

- `Virtual Machine Contributor`

### Supported Clouds

- Azure

### Cost

This Policy Template does not incur any cloud costs.
