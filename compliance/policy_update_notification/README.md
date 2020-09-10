# Policy Update Notification

## What it does

Identifies the current version of applied policy and that of respective policy in catalog and creates an incident with the date of policy updation.

## Functional Details

- This policy identifies the version of all the policies that are applied in an account and compares them to the version of respective policy in catalog. It further creates an incident providing details on when the policy was last updated in catalog and the link to README and CHANGELOG files.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify

## Policy Actions

- Sends an email notification

## Prerequisites

### Credential configuration

Required permissions in the provider:

- Policy Manager must have Enterprise_manager, admin or policy_manager permissions in the org or all accounts in question.

## Cost

This Policy Template does not incur any cloud costs.
