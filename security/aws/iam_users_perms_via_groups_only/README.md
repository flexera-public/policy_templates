# AWS Ensure IAM Users Receive Permissions Only Through Groups

## What it does

This policy checks all of the IAM users on an AWS account to ensure none of them have any policies assigned directly rather than through groups they are members of. If any such users are found, an incident is raised.

## Functional Details

The AWS IAM API is used to gather a list of IAM users, along with a list of their inline policies and attached policies. If either list (or both) contains any items, an incident is raised; the incident contains a list of affected users with the user id, user name, user arn, and the number of both inline and attached policies.

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
              "iam:ListUserPolicies",
              "iam:ListAttachedUserPolicies"
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
