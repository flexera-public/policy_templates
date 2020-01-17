# AWS Open Buckets

## What it does

This Policy Template will check your account for Amazon S3 buckets with public permission.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *param_email* - Email addresses of the recipients you wish to notify
- *param_slack_channel* - (Optional) Slack channel name including the \"#\"
- *param_slack_webhook_cred* - (Optional) Name of RightScale credential that contains the Slack webhook credential

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

```javascript
{
    "Version": "2006-03-01",
    "Statement": [
        {
            "Sid": "ListObjectsInBucket",
            "Effect": "Allow",
            "Action": ["s3:ListAllMyBuckets",
                       "s3:GetBucketLocation",
                       "s3:GetBucketAcl"],
            "Resource": ["arn:aws:s3:::bucket-name"]
        }
    ]
}
```

## Slack Channel Notification Support

The policy includes optional support to send a notification to a slack channel when an anomaly is detected.
The policy accepts two optional input parameters to support this capability:

- `Slack Channel Name`: This is the slack channel name, e.g. #policy_alerts
- `RightScale Credential for Slack Channel Webhook`: This is the name of a RightScale credential in the account that contains the Slack webhook URL.

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
