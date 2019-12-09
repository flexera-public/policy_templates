# Azure Idle Compute Instances

## What it does

This policy checks all the instances in the Azure Subscription for the average CPU usage over the last 30 days.  If the usage is less than the user provided CPU percentage threshold then the virtual machines are recommended for deletion, and the user is emailed.

## Functional Details

The policy leverages the Azure API to check all instances and then checks the instance average CPU utilization over the past 30 days, finally recommending the low ones for deletion after approval.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *CPU Threshold* - Percentage of CPU utilization
- *Exclusion Tag Key* - An Azure-native instance tag to ignore instances that you don't want to consider for downsizing. Only supply the tag key

## Prerequisites

This policy requires the Azure Resource Manager Credential.  When applying the policy select the appropriate credentials
from the list for your tenant.  If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *Azure RM* in the Provider field.  
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

### Azure Required Permissions

The following Azure permissions must be allowed for the policy to run.

- Microsoft.Compute/virtualMachines/read
- Microsoft.Compute/virtualMachines/write

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
