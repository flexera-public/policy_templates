# Azure Publicly Accessible SQL Managed Instances

## What it does

This policy checks all Azure SQL Managed instances and reports on any that are publicly accessible. When such an instance is detected, the user can choose to disable public data endpoint or delete it. For deleting the user needs to enable 'delete action' option as mentioned in "To enable delete action" section below.

## Functional Details

When a publicly accessible Azure SQL Managed Instance is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have multiple actions that they are able to take after approval:

- *delete* - deletes the Azure SQL managed instance
- *Note: by default *delete* action has been disabled, the user can follow the steps mentioned in "To enable delete action" section above to enable delete action.*
- *disable public data endpoint* - modifies the configuration of virtual network of the particular SQL managed instance that allows public accessibility.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Exclusion Tag Key* - Azure SQL Managed instance tag to ignore instance that are with public data endpoint enabled. Only supply the tag key. The policy assumes that the tag value is irrelevant.

## Prerequesites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

## To enable delete action

Perform below steps to enable delete action.

- Edit the file [Check_for_publicly_accessible_Azure_SQL_Managed_Instance](https://github.com/flexera/policy_templates/tree/master/security/azure/sql_publicly_accessible_managed_instance)
- uncomment the line which conatins 'escalate $esc_delete_Managed_instances_approval' and save the changes.
- upload the modified file and apply the policy.

## Azure Required Permissions

- Microsoft.Sql/managedInstances/*

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.