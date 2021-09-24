# AWS IAM Ensure Credentials Unused For >45 days Are Disabled

## What it does

AWS IAM users can access AWS resources using different types of credentials, such as passwords or access keys. It is recommended that all credentials that have been unused in 45 or greater days be deactivated or removed, and this policy checks for unused credentials.

## Functional Details

The policy leverages the AWS IAM API to generate and examine a credential report. When user credentials are found that have not been used for 45 days or longer, an email action is triggered automatically to notify the specified users of the incident. This email report contains a list of affected user accounts.

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
              "iam:GenerateCredentialReport",
              "iam:GetCredentialReport"
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
