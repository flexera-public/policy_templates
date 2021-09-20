# AWS Restrict Reusing Passwords

## What it does

IAM password policies can prevent the reuse of a given password by the same user. It is recommended that the password policy prevent the reuse of passwords, and this policy checks if the password policy has been configured to disallow reusing passwords and to store at least 24 previous passwords for ensuring this.

## Functional Details

The policy leverages the AWS IAM API to examine the password policy. When there is no password policy, the policy does not restrict reusing passwords, or the policy stores fewer than 24 previous passwords, an email action is triggered automatically to notify the specified users of the incident.

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
              "iam:GetAccountPasswordPolicy",
              "sts:GetCallerIdentity"
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
