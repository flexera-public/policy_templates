# AWS Hardware MFA

## What it does

Multi-factor authentication (MFA) increases account security by requiring the user have access to another device in order to log into the account in addition to their username and password. Hardware MFA uses a hardware tool, such as a physical key, to authenticate. It is recommended that MFA be enabled on all accounts, and in some cases, hardware MFA is preferred. This policy checks the root account to verify that hardware MFA is enabled.

## Functional Details

When the root account does not have hardware MFA enabled, an email action is triggered automatically to notify the specified users of the incident.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

```javascript
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:GetCallerIdentity",
                "iam:GetAccountSummary",
                "iam:ListVirtualMFADevices"

            ],
            "Resource": "*"
        }
    ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
