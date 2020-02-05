# Azure - Ensure AHUB Utilization with Manual Entry

## What it does

This policy checks all instances in Azure to determine how many are using AHUB and report when that number falls outside or inside the specified license number.

## Functional Details

The policy leverages the cloud API to get data for all instances and compares that to the allowed AHUB number specified by the user.
Each license is good for one VM with up to 16 cores or two VM's with up to 8 cores. The policy will report on the instances that are missing AHUB license and show which instance have the potential for the AHUB license.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Allowed AHUB licenses* - Number of AHUB licenses that are allowed to be run on Azure
- *Exclusion Tag Key* - Azure VMs instance tag to ignore instance that are with AHUB enabled. Only supply the tag key. The policy assumes that the tag value is irrelevant.

## Prerequesites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Azure Required Permissions

The following Azure permissions must be allowed for the policy to run.

- Microsoft.Compute/virtualMachines/read
- Microsoft.Compute/locations/vmSizes/read

## Supported Clouds

- Azure

## Cost

This policy does not incur any cloud costs.


