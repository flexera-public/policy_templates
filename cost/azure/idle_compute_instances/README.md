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

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Compute/virtualMachines/read
- Microsoft.Compute/virtualMachines/write

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
