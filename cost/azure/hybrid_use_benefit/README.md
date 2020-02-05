# Azure Hybrid Use Benefit Policy

## What it does

This Policy Template is used to automatically apply the Azure Hybrid Use Benefit (AHUB) to all eligible VMs in an Azure Subscription.

## Functional Details

_ The policy identifies all Windows server instances that are not currently using [Azure Hybrid Use Benefit] (https://azure.microsoft.com/en-us/pricing/hybrid-benefit/). It raises an incident for all applicable VMs not currently using AHUB, which once approved, will enable AHUB on all identified instances.
- The Exclusion Tag parameter is a string value.  Supply the Tag Key only.  Tag Values are not analyzed and therefore are not need.  If the exclusion tag key is used on an Instance, that Instance is presumed to be exempt from this policy.
- This policy does not track licenses or availability. It is your responsibility to ensure you are not under licensed.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Exclusion Tag Key* - an Azure-native instance tag to ignore instances that you don't want AHUB applied to. Only supply the tag key
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Azure Required Permissions

- Microsoft.Compute/virtualMachines/read
- Microsoft.Compute/virtualMachines/write

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.