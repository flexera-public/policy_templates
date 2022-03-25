# FNMS Overused Licenses

## What it does

This policy uses the ITAM Inventories API to look up software licenses and raise an incident if more instances of any licenses are used than are actually available. The incident provides a detailed list of the affected licenses.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email address(es) to notify

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

## Cost

This Policy Template does not incur any additional cloud costs.
