# AWS Service Control Policy Audit

## What it does

This policy audits whether a named policy is applied across all AWS Accounts in the organization

> *NOTE: This Policy Template must be appled to the **AWS Organization Master Payer** account.*

## Functional Details

- The policy leverages the AWS API to check that all accounts have a named Service Control Policy applied.
- When an account is detected without the Service Control Policy attached, an email action is triggered automatically to notify the specified users of the incident.

## Input Parameters

- *Email addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Service Control Policy Name* - The name of the Service Control Policy to check for.

## Policy Actions

- Sends an email notification.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

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
