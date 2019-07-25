## Inactive Users - Okta

**As a best practice, this policy should only be applied to the Master Account, and not to each individual RightScale Account.**

### What it does

This Policy Template leverages the [Okta Users API](https://developer.okta.com/docs/reference/api/users/#list-users) to identify users that have no logged in for an extended period of time, and optionally will deactivate those users upon approval.  

### Prerequesites

- This Policy Template requires an Okta API Token to authenticate with the Okta API.  [This tutorial](https://developer.okta.com/docs/guides/create-an-api-token/overview/) describes how to create a new Token.
- The Okta API Token must then be stored as a RightScale Credential in the account in which this policy will be applied. The credential must be named `OKTA_API_KEY`.

### Functional Details

- This policy will target a specific Okta organization

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Okta Organization Name* - The name of your Okta Organization.  For example, if you navigate to https://contoso.okta.com to login to Okta, the value in this parameter would be `contoso`.
- *Number of Days Since Last Login* - The number of days that a user has not logged in to Okta, which should raise an incident.
- *Email addresses to notify* - A list of email addresses to notify

### Required RightScale Roles

- policy_manager
- policy_approver - to approve the escalation to deactivate the inactive Okta users

### Supported Services

- Okta

### Cost

This Policy Template does not incur any cloud costs.
