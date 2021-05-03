# Azure Hybrid Use Benefit Policy for SQL

## What it does

This Policy Template is used to automatically apply the Azure Hybrid Use Benefit (AHUB) to all eligible SQL instances in an Azure Subscription.

## Functional Details

- The policy identifies all SQL databases in Azure that are not currently using [Azure Hybrid Use Benefit](https://azure.microsoft.com/en-us/pricing/hybrid-benefit/). These can be SQL Virtual Machines, SQL Databases or SQL Managed Instances. It raises an incident for all applicable instances not currently using AHUB, which once approved, will enable AHUB on all identified instances.
- The Exclusion Tag parameter is a string value. Supply the Tag Key only. Tag Values are not analyzed and therefore are not need. If the exclusion tag key is used on an Instance, that Instance is presumed to be exempt from this policy.
- This policy does not track licenses or availability. It is your responsibility to ensure you are not under licensed.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Exclusion Tag Key* - an Azure-native instance tag to ignore instances that are not using AHUB. Only supply the tag key. The policy assumes that the tag value is irrelevant.
- *Email addresses* - A list of email addresses of the recipients you wish to notify
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action. For example, if a user selects the "Hybrid use benefit for SQL" action while applying the policy, hybrid use benefit will be applied to the eligible instances.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.SqlVirtualMachine/sqlVirtualMachines/read
- Microsoft.SqlVirtualMachine/sqlVirtualMachines/write
- Microsoft.Sql/servers/read
- Microsoft.Sql/servers/write
- Microsoft.Sql/managedInstances/read
- Microsoft.Sql/managedInstances/write

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
