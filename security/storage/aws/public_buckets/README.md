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

This policy requires the AWS IAM User Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *AWS* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## Slack Channel Notification Support

The policy includes optional support to send a notification to a slack channel when an anomaly is detected.
The policy accepts two optional input parameters to support this capability:

- `Slack Channel Name`: This is the slack channel name, e.g. #policy_alerts
- `RightScale Credential for Slack Channel Webhook`: This is the name of a RightScale credential in the account that contains the Slack webhook URL.

## AWS Required Permissions

This policy requires permissions to describe AWS S3 ListAllMyBuckets, GetBucketLocation and GetBucketAcl.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

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

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
