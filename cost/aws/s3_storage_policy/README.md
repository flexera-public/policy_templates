# AWS S3 Buckets Without Intelligent Tiering

## What It Does

This Policy Template scans all S3 buckets in your AWS account and identifies buckets that don't have [S3 Intelligent Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html) enabled. An incident is created listing all non-compliant buckets, with the option to enable Intelligent Tiering after approval, or automatically for any non-compliant buckets.

**S3 Intelligent Tiering** automatically moves your data between different storage tiers based on access patterns, optimizing costs without performance impact. This feature is ideal for data with unpredictable access patterns and can provide significant cost savings with zero operational overhead.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized for non-compliant buckets if Intelligent Tiering is enabled.

- The policy gets `TimedStorage-ByteHrs` usage costs per bucket from the past 24 hours (as tracked in Flexera CCO)
- The monthly cost per bucket is calculated by multiplying the amortized cost for 1 day (from Flexera CCO) by 30.44, which is the average number of days in a month.
- A conservative **30%** savings estimate is applied based on AWS published Intelligent Tiering benefits ([based on up to 40% for infrequent access and up to 68% for archive access](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)).
- If the bucket cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident details will include individual bucket `Estimated Monthly Savings` and the summed `Potential Monthly Savings`.
- All savings values are reported in the currency of the Flexera organization where the policy is applied.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy template will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter buckets containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Enable Intelligent Tiering" action while applying the policy template, all the buckets that didn't satisfy the policy condition will have Intelligent Tiering enabled.

## Policy Actions

The following policy actions can be taken on any resources found to be out of compliance.

- Sends an email notification
- Enable Intelligent Tiering on S3 buckets

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `sts:GetCallerIdentity`
  - `s3:ListAllMyBuckets`
  - `s3:GetBucketLocation`
  - `s3:GetBucketTagging`
  - `s3:GetIntelligentTieringConfiguration`
  - `s3:PutLifecycleConfiguration`*

  \* Only required for taking action (Enable Intelligent Tiering); the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "s3:ListAllMyBuckets",
                  "s3:GetBucketLocation",
                  "s3:GetBucketTagging",
                  "s3:GetIntelligentTieringConfiguration",
                  "sts:GetCallerIdentity",
                  "s3:PutLifecycleConfiguration"
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
