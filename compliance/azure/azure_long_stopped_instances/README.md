# Azure Long-Stopped Instances

## What it does

This policy checks all Azure instances that have been stopped for more than a specified period of time and Terminates them after approval.

## Functional Details

The policy leverages the Azure API to check all instances that have been stopped for longer than the specified period. If the action is approved, the instance is terminated.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Stopped days* - Number of days an instance is stopped before it is added to the report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider: 
- Microsoft.Compute/virtualMachines/read
- Microsoft.Compute/virtualMachines/delete

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
