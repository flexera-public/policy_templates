# AWS Untagged Resources

## What It Does

This policy template checks for AWS resources missing the user-specified tags. An incident is raised containing the untagged resources, and the user has the option to tag them.

## Functional Details

- The policy leverages the AWS Tagging API to retrieve a list of all resources in the AWS estate.
- The policy then filters that list based on user-specified parameters.
- The policy then identifies the resources in the filtered list that are missing the tags specified by the user.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Tags* - The policy will report resources missing the specified tags. The following formats are supported:
  - `Key` - Find all resources missing the specified tag key.
  - `Key==Value` - Find all resources missing the specified tag key:value pair and all resources missing the specified tag key.
  - `Key!=Value` - Find all resources that have the specified tag key:value pair.
  - `Key=~/Regex/` - Find all resources where the value for the specified key does not match the specified regex string and all resources missing the specified tag key.
  - `Key!~/Regex/` - Find all resources where the value for the specified key matches the specified regex string.
- *Any / All* - Whether to report on instances missing any of the specified tags or all of them. Only applicable if more than one value is entered in the `Tags` field.
- *Consider Tag Dimensions* - Exclude results when a resource is tagged with a tag key that is normalized by a Tag Dimension.
  - Considers resource tags which are normalized under tag dimensions and excludes those matching from the missing tags results.
  - Mitigates/prevents seeing resources that are tagged using some tag key which is normalized under a matching Tag Dimension.
  - `Tags` parameter value must match a Tag Dimension Name ("Cost Center") or Tag Dimension ID ("tag_cost_center") for the lookup to occur

  For example,
   - A resource tagged `app=prod-cluster`
   - A Tag Dimension named "Application" (tag_application) which normalizes tag resource tag keys `app`, `Application`, `App`, `application`, etc...

  If Exclude Tag Dimensions is enabled and `Tags=["Application"]` the example resource would be considered to **not** be missing the `Application` tag, because it has the `app` tag which is normalized under the "Application" tag dimension

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Sends an email notification
- Tag AWS resource after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `sts:GetCallerIdentity`
  - `config:TagResource`
  - `ec2:DescribeRegions`
  - `tag:GetResources`
  - `ec2:CreateTags`*
  - `tag:TagResources`*
  - `rds:AddTagsToResources`*

  \* Only required for taking action (adding tags); the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sts:GetCallerIdentity",
                  "config:TagResource",
                  "ec2:DescribeRegions",
                  "tag:GetResources",
                  "ec2:CreateTags",
                  "tag:TagResources",
                  "rds:AddTagsToResource"
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

This Policy Template does not launch any instances, and so does not incur any cloud costs.
