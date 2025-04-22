# Cloud Bill Processing Error Notification

## What It Does

This policy template reports on any Flexera Cloud Cost Optimization bill connections that are in an error state, have not successfully processed a bill for the user-specified number of hours or optionally have no bills (disabled by default). This report can be emailed if desired.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify if bill processing errors are found.
- *Processing Time (Hours)* - Amount of time in hours to consider a bill connection in an error state if it has failed to complete processing of a bill.
- *Bill Connection Ignore List* - A list of Bill Connection IDs to never check for errors or report on. Leave blank to check all Bill Connections.
- *Report Connection With Zero Bills* - Whether or not to report any connections that have no available bills to process since this can sometimes indicate an error.

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

This policy template does not incur any cloud costs.
