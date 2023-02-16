# Azure Long Running Instances

## What It Does

This policy checks for running instances that have been running longer than the `Days Old` parameter. It will then take the appropriate action(Stop/Terminate) on the instance.

## Functional Description

- This policy identifies all instances that have been running longer than the `Days Old` parameter.

## Input Parameters

This policy template has the following Input parameters which require value before
the policy can be applied.

- *Email notify list* - Email addresses of the recipients you wish to notify.
- *Days Old* - Number of days to be running before included in list.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Stop Instances" action while applying the policy, all the instances that didn't satisfy the policy condition will be stopped.

## Policy Actions

Policy actions may include automation to alert or remediate violations found in the
Policy Incident. Actions that destroy or terminate a resource generally require
approval from the Policy Approver. This policy includes the following actions.

- Sends an email notification
- Stop the instance
- Terminate the instance

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm)
for connecting to the cloud -- in order to apply this policy you must have a
credential registered in the system that is compatible with this policy. If
there are no credentials listed when you apply the policy, please contact your
cloud admin and ask them to register a credential that is compatible with this
policy. The information below should be consulted when creating the credential.

## Supported Clouds

This policy template supports the following clouds:

- Azure

## Costs

This Policy Template does not incur any cloud costs.
