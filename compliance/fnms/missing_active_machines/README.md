# ITAM Missing Active Machines

## What it does

This policy uses the ITAM Inventories API to look up machines, when it finds a machine that is active we compare it's `lastInventoryDate` to the current time and
if it has not reported in during that time period an incident is triggered.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Days missing while active* - Number of missing for a machine to be reported
- *Email addresses of the recipients you wish to notify* - A list of email addresse(s) to notify

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

## Cost

This Policy Template does not incur any additional cloud costs.
