# Azure VMs Not Using Managed Disks

## What it does

This policy checks all Azure VMs and reports on any that are not using Managed Disks, which are the latest offering from Azure and are much easier to manage.

## Functional Details

When a VM that is using unmanaged disks is detected, VM location information as well as unmanaged disk information is reported to the specified users.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Exclusion Tag Key* - an Azure-native instance tag to ignore instances that match the disallowed instance type. Only supply the tag key.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Compute/virtualMachines/read

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
