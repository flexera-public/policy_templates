# Inactive Users - Okta

## Functional Details

- This policy will target a specific Okta organization

## What it does

This Policy Template leverages the [Okta Users API](https://developer.okta.com/docs/reference/api/users/#list-users) to identify users that have not logged in for an extended period of time, and optionally will deactivate those users upon approval.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Okta Organization Name* - The name of your Okta Organization.  For example, if you navigate to <https://demo.okta.com> to login to Okta, the value in this parameter would be `demo`.
- *Number of Days Since Last Login* - The number of days that a user has not logged in to Okta, which should raise an incident.
- *Email addresses to notify* - A list of email addresses to notify
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Deactivate Users" action while applying the policy, all the users that didn't satisfy the policy condition will be deactivated.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**ServiceNow Credential**](https://docs.flexera.com/flexera/EN/Automation/GenericCredentials.htm#automationadmin_3335267112_1121390) (*provider=servicenow*) which has the following permissions:
  - `user_admin`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- ServiceNow

## Cost

This Policy Template does not incur any cloud costs.
