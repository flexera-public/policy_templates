# AWS S3 Buckets Without Intelligent Tiering

## What It Does

This Policy Template scans all S3 buckets in your AWS account and identifies buckets that don't have [S3 Intelligent Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html) enabled. An incident is created listing all non-compliant buckets, with the option to enable Intelligent Tiering after approval, or automatically for any non-compliant buckets.

**S3 Intelligent Tiering** automatically moves your data between different storage tiers based on access patterns, optimizing costs without performance impact. This feature is ideal for data with unpredictable access patterns and can provide significant cost savings with zero operational overhead.

### Policy Savings Details

This policy calculates estimated monthly savings based on your actual storage costs and AWS's published Intelligent Tiering savings rates.

**How savings are calculated:**

- We analyze your actual `TimedStorage-ByteHrs` usage costs from the past 24 hours (as tracked in Flexera CCO)
- Project this to monthly costs using 30.4375 days per month (accounting for leap years)
- Apply a conservative 30% savings estimate based on [AWS's published Intelligent Tiering benefits](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/): up to 40% savings for infrequent access and 68% for archive access
- All cost calculations include any Flexera adjustment rules or cloud provider discounts in your organization

**Important notes:**

- If a resource isn't found in Flexera CCO, the estimated savings will show as $0
- The incident email shows both individual bucket savings and total estimated savings across all buckets
- Savings amounts are displayed in your organization's configured currency
- Actual savings may be higher depending on your specific data access patterns

## Input Parameters

- **Email Addresses** - Email addresses to receive incident notifications when non-compliant buckets are found.
- **Account Number** - AWS account number for cross-account role access. Leave blank when using standard AWS IAM credentials. Only needed when scanning an AWS account different from the one associated with your Flexera credential. [More details](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- **Allow/Deny Regions** - Choose whether the region list below should include or exclude specific regions from scanning.
- **Allow/Deny Regions List** - Specific AWS regions to include or exclude. Use region codes (e.g., us-east-1, eu-west-1). Leave empty to scan all regions. Note: If using Service Control Policies (SCPs), enter only enabled regions to avoid policy failures.
- **Exclusion Tags** - Skip buckets with specific tags. Useful for excluding buckets that shouldn't use Intelligent Tiering (e.g., high-frequency access buckets). Supported formats:
  - `Environment` - Exclude all buckets with this tag key (any value)
  - `Environment==Production` - Exclude buckets with this exact tag key and value
  - `Environment!=Production` - Exclude buckets that don't have this tag or have different values
  - `Environment=~/Prod.*/` - Exclude buckets where the tag value matches this pattern
  - `Environment!~/Prod.*/` - Exclude buckets where the tag value doesn't match this pattern
- **Exclusion Tags: Any / All** - When multiple exclusion tags are specified, choose whether a bucket needs to match ANY tag (more restrictive) or ALL tags (less restrictive) to be excluded.
- **Automatic Actions** - When set to "Enable Intelligent Tiering", the policy will automatically implement Intelligent Tiering on all identified buckets without requiring manual approval for each action.

**Note about Automatic Actions:** When "Enable Intelligent Tiering" is selected, the policy will automatically configure lifecycle rules on all non-compliant buckets immediately after the incident is created. Leave this blank if you prefer to review and manually approve each action.

## Policy Actions

When S3 buckets without Intelligent Tiering are discovered, this policy can:

- **Send an email report** - Always enabled. Provides a detailed list of all non-compliant buckets with estimated savings potential
- **Enable Intelligent Tiering automatically** - Optional. When selected, the policy will automatically configure Intelligent Tiering on all identified buckets after approval (or immediately if automatic actions are enabled)

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
