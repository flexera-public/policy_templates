# Cloud Bill Processing Error Notification

## What It Does

This policy template reports on any Flexera Cloud Cost Optimization bill connections that are in an error state or have not successfully processed a bill for the user-specified number of hours. Optionally, this report can be emailed.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify if bill processing errors are found.
- *Processing Time (Hours)* - Amount of time in hours to consider a bill connection in an error state if it has failed to complete processing of a bill.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `ca_user`
  - `csm_bill_upload_admin`
  - `enterprise_manager`
  - `observer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This Policy Template does not incur any cloud costs.
