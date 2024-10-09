# AWS Object Storage Optimization

## What It Does

This policy checks S3 buckets for objects to move to the 'Glacier' or 'Deep Archive' storage classes based on object age. The user can opt to either delete the objects or move them to the recommended storage class.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Bucket List* - A list of S3 buckets to assess objects in. Leave blank to assess all buckets.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Buckets not in an allowed region will be ignored and their objects will not be assessed.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore S3 objects that you don't want to produce recommendations for. Use Key:Value format for specific tag key/value pairs, and Key:\* format to match any object with a particular key, regardless of value. Examples: env:production, DO_NOT_DELETE:\*
- *New Storage Class* - Whether to move objects to Glacier or Deep Archive if they meet the specified age thresholds. Select 'Both' to consider moving objects to either one based on the specified age thresholds.
- *Glacier Age Threshold (Days)* - Time in days since object was last modified to change storage class to Glacier. Not applicable if 'Deep Archive' is selected for New Storage Class.
- *Deep Archive Age Threshold (Days)* - Time in days since object was last modified to change storage class to Deep Archive. Not applicable if 'Glacier' is selected for New Storage Class.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action. For example if a user selects the "Delete S3 Objects" action while applying the policy, all of the S3 objects that didn't satisfy the policy condition will be deleted.

## Policy Actions

- Send an email report
- Change storage class of S3 object after approval
- Delete S3 object after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `sts:GetCallerIdentity`
  - `s3:ListAllMyBuckets`
  - `s3:GetBucketLocation`
  - `s3:ListBucket`
  - `s3:GetObject`
  - `s3:GetObjectTagging`
  - `s3:PutObject`*
  - `s3:DeleteObject`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sts:GetCallerIdentity",
                  "s3:ListAllMyBuckets",
                  "s3:GetBucketLocation",
                  "s3:ListBucket",
                  "s3:GetObject",
                  "s3:GetObjectTagging",
                  "s3:PutObject",
                  "s3:DeleteObject"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
