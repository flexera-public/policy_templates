# Azure Long-Stopped Instances

## What it does

This policy checks all Azure instances that have been stopped for more than a specified period of time and Terminates them after approval.

## Functional Details

The policy leverages the Azure API to check all instances that have been stopped for longer than the specified period. If the action is approved, the instance is terminated.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Stopped days* - Number of days an instance is stopped before it is added to the report

## Prerequisites

This policy requires the Azure Resource Manager Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *Azure RM* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## Azure Required Permissions

- Microsoft.Compute/virtualMachines/read
- Microsoft.Compute/virtualMachines/delete

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
