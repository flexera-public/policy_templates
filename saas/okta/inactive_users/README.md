# Inactive Users - Okta

## Functional Details

- This policy will target a specific Okta organization

## What it does

This Policy Template leverages the [Okta Users API](https://developer.okta.com/docs/reference/api/users/#list-users) to identify users that have not logged in for an extended period of time, and optionally will deactivate those users upon approval.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Okta Organization Name* - The name of your Okta Organization.  For example, if you navigate to <https://contoso.okta.com> to login to Okta, the value in this parameter would be `contoso`.
- *Number of Days Since Last Login* - The number of days that a user has not logged in to Okta, which should raise an incident.
- *Email addresses to notify* - A list of email addresses to notify
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Deactivate Users" action while applying the policy, all the users that didn't satisfy the policy condition will be deactivated.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html)
for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no
credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed: 

Provider tag value to match this policy: `okta`

Required permissions in the provider:

This policy requires permissions to access Okta.com API as the Owner of the Organization(s).

## Supported Services

- Okta

## Cost

This Policy Template does not incur any cloud costs.
