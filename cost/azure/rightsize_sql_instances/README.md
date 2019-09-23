# Azure Rightsize SQL Instances

## What it does

This policy will look at Utilization of Azure SQL instances and recommend up or down sizing.

## Functional Details

This policy checks all the Azure SQL instances for a Azure Subscription. It does a Average CPU usage over the last 30 days. It then checks if the Utilization is Lower than the Downsize Threshold or higher that Upsize Threshold. Finally it display the found data and the recommendations.

### Input Parameters

- *Azure Tenant ID* - Your Azure tenant ID.  You can find it by following this guide: [Tenant ID](https://docs.microsoft.com/en-us/onedrive/find-your-office-365-tenant-id)
- *Azure Subscription ID* - Your Azure Subscription ID.  You can find it by following this guide: [Subscription ID](https://blogs.msdn.microsoft.com/mschray/2016/03/18/getting-your-azure-subscription-guid-new-portal/)
- *Average used CPU % - Upsize threshold* - Percentage of CPU utilization to identify an Upsize is recommended
- *Average used CPU % - Downsize Threshold* - Percentage of CPU utilization to identify an Downsize is recommended
- *Exclusion Tag Key* - To Identify any instances that should be excluded from the recommendations
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Required Rightsize Roles

- `credential_viewer`

### Azure Required Permissions

- `Reader`

### Supported Clouds

- Azure

### Cost

This Policy Template does not incur any cloud costs.