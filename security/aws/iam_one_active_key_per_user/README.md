# AWS Ensure One Active Key Per IAM User

## What it does

This policy checks all of the IAM users on an AWS account to ensure none of them have more than one active access key. If any users do, an incident is raised.

## Functional Details

The policy leverages the AWS IAM API to obtain a list of users and their access keys. A count is produced of how many active keys each user has, and an incident is raised if any users have more than one active key. An email action is triggered automatically to notify the specified users of the incident. This email report contains a list of affected users.

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
              "iam:ListUsers",
              "iam:ListAccessKeys"
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
