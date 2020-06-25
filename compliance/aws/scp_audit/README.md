# AWS Service Control Policy Audit

## What it does

This policy audits whether a named policy is applied across all AWS Accounts in the organization

## Functional Details

- The policy leverages the AWS API to check that all accounts have a named Service Control Policy applied.
- When an account is detected without the Service Control Policy attached, an email action is triggered automatically to notify the specified users of the incident.

## Input Parameters

- *Email addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Service Control Policy Name* - The name of the Service Control Policy to check for.

## Policy Actions

- Sends an email notification.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

```javascript
{
  "Version": "2016-11-15",
  "Statement":[{
  "Effect":"Allow",
  "Action":[
    "organizations:List*"
    ],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
