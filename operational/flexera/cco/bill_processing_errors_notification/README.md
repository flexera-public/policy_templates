# Bill Processing Error Notification

## What it does

Analyzes all configured cloud bill connects and raises an incident for any in an error state.

## Functional Details

This policy collects all cloud bill connects, checks the state of each bill connect, and compares when the bill was downloaded to the policy execution time. If there is an error, or the processing time exceeds a user-specified number of hours for any cloud bill connects, an incident will be raised.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - A list of email addresses to notify if bill processing errors are found.
- *Processing Time (Hours)* - Amount of time (hours) to consider a bill connect in an error state if it has failed to complete processing of a bill.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance:

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - View Policies
  - Manage Organization

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- NA

## Cost

This Policy Template does not incur any cloud costs.
