# Azure Publicly Accessible SQL Managed Instances

## What it does

This policy checks all Azure SQL Managed instances and reports on any that are publicly accessible. When such an instance is detected, the user can choose to disable public data endpoint or delete it.

## Functional Details

When a publicly accessible Azure SQL Managed Instance is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have multiple actions that they are able to take after approval:

- *delete* - deletes the Azure SQL managed instance
- *disable public data endpoint* - modifies the configuration of virtual network of the particular SQL managed instance that allows public accessibility.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Exclusion Tag Key* - Azure SQL Managed instance tag to ignore instance that are with public data endpoint enabled. Only supply the tag key. The policy assumes that the tag value is irrelevant.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Disable Public endpoint" action while applying the policy, the public data endpoint would be deleted for the identified instances.

## Prerequesites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Sql/managedInstances/*

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
