## AWS Cloud Credentials Rotation Policy Template

### What it does

This Policy Template is used to automatically update the AWS IAM keys used to connect the RightScale account to the applicable AWS account.
When applied, the policy updates the credentials immediately and then updates the credentials thereafter every `X number of days` where X is specified by the user.

### Functional Details

This policy performs the following actions:
- Create a new set of security credentials in AWS for the IAM user account connected to RightScale.
- Update the RightScale AWS cloud connections to use the new keys.
- Deactivate the previously used IAM key.
- Update RightScale Credentials, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY with the new IAM user keys.

### Caveats and Prerequisites

The policy assumes the following to be true:
- The AWS IAM user used to connect to RightScale is DEDICATED to the RightScale connection. 
- The AWS IAM user used to connect RightScale to AWS has permissions to create and delete its keys.
If the AWS IAM user does not have proper permissions, you can create and apply the following policy to that user.

```javascript
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:*LoginProfile",
        "iam:*AccessKey*",
        "iam:*SSHPublicKey*"
      ],
      "Resource": "arn:aws:iam::account-id-without-hyphens:user/${aws:username}"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:ListAccount*",
        "iam:GetAccountSummary",
        "iam:GetAccountPasswordPolicy",
        "iam:ListUsers"
      ],
      "Resource": "*"
    }
  ]
}
```

- There are RightScale credentials defined in RightScale named AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY that contain the IAM user's currently active keys.
  - NOTE: These RightScale CREDENTIALs would have been automatically created by RightScale when originally connecting the AWS IAM user to RightScale.

If the policy detects two keys already exist for the IAM user, the policy will delete credentials as follows:
- If it finds an inactive key, it'll delete that key.
- If all keys are active, it'll delete the first key it finds that is NOT currently being used to connect RightScale to AWS.

### Supported Clouds

- AWS

### Cost

This Policy Template does not incur any cloud costs.
