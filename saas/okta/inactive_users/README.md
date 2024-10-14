# Okta Inactive Users

## What It Does

This policy template reports any Okta users that have not logged in for a user-specified number of days. Optionally, this report can be emailed and the inactive users can be deactivated.

## How It Works

The [Okta Users API](https://developer.okta.com/docs/reference/api/users/#list-users) is used to obtain a list of Okta users and their most recent login date.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify
- *Okta Organization Name* - Name of the Okta organization. For example, if you navigate to *myorg.okta.com* to log into Okta, the organization name would be *myorg*.
- *Days Since Last Login* - The number of days a user needs to go without logging in to be considered inactive.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Deactivate Inactive Users" action while applying the policy, all the users that didn't satisfy the policy condition will be deactivated.

## Policy Actions

- Send an email report
- Deactivate inactive users after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Okta Credential**](https://docs.flexera.com/flexera/EN/Automation/GenericCredentials.htm#automationadmin_3335267112_1121389) (*provider=okta*) which has the following permissions:
  - `READ_ONLY_ADMIN`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Okta

## Cost

This policy template does not incur any cloud costs.
