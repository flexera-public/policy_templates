# Azure Idle Compute Instances

## What it does

This policy checks all the instances in the Azure Subscription for the average CPU usage over the last 30 days. If the usage is less than the user provided CPU percentage threshold then the virtual machines are recommended for deletion, and the user is emailed.

## Functional Details

The policy leverages the Azure API to check all instances and then checks the instance average CPU utilization over the past 30 days, finally recommending the low ones for deletion after approval.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. Optima is used to receive the estimated savings which is the product of the most recent full day's cost of the resource * 30. The savings is displayed in the Estimated Monthly Savings column. If the resource can not be found in Optima the value is N/A. The incident message detail includes the sum of each resource Estimated Monthly Savings as Total Estimated Monthly Savings.
If the user does not have the minimum required role of `billing_center_viewer` or if there is no enough data received from Optima to calculate savings, appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as N/A in the incident table.

## Input Parameters

- *Email addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *CPU Threshold* - Average CPU threshold at which to trigger a decommission.
- *Exclusion Tag Key* - An Azure-native instance tag key to ignore instances that you don't want to consider for downsizing. Example: exclude_utilization.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Subscription Whitelist* - Whitelisted Subscriptions, if empty, all subscriptions will be checked

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Prerequisites

- This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.
- billing_center_viewer (note: this role must be applied at the Organization level).

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
