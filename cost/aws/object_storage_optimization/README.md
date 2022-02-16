# AWS Object Storage Optimization

## What it does

This Policy checks S3 buckets for older objects and can move old object to 'glacier' or 'deep archive' after a given period of time. The user can choose to delete old object by enabling 'delete action' option as mentioned in Enable delete action section below.

## Functional Details

- This policy identifies all S3 objects last updated outside of the specified timeframe
- For all objects identified as old, the user can choose to move the object to Glacier or Glacier Deep Archive after the specified timeframe.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Days since last modified to move to Glacier* - Move to glacier after days last modified - leave blank to skip moving
- *Days since last modified to move to Deep Archive* - Move to glacier deep archive after days last modified- leave blank to skip moving
- *Exclude Tag* - List of tags that will exclude s3 objects from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Update S3 Object Class" action while applying the policy, all the objects that didn't satisfy the policy condition will be updated.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

```json
{
  "Version": "2006-03-01",
  "Statement":[
    {
      "Effect":"Allow",
      "Action":[
        "s3:ListAllMyBuckets",
        "s3:GetBucketLocation",
        "s3:ListBucket",
        "s3:GetObject",
        "s3:GetObjectTagging",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource":"*"
    }
  ]
}
```

Note: To get the list and modify S3-objects present in the S3 bucket, user must have READ and Write access to the bucket.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
