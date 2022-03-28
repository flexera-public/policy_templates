# FlexNet Manager VMs Missing Host ID

## What it does

This policy uses the FlexNet Manager Inventories API to look up virtual machines and raises an incident if any are found without a Host ID assigned to them. The incident provides a detailed list of the affected machines.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email address(es) to notify

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

## Cost

This Policy Template does not incur any additional cloud costs.
