# AWS Rightsize EBS Volumes

## What it does

This policy checks for all cost inefficient volumes an AWS Account. In this first iteration, this includes finding GP2 volume types and recommending them for upgrade for GP3 if this provides cost savings. A Policy Incident will be created with all of volumes that fall into these criteria.

## Functional Details

- The policy leverages the AWS API to retrieve a list of all volumes in an AWS Account
- The policy identifies all GP2 volumes and uses the AWS Pricing API to retrieve the current cost, and the cost of the volume if it were a GP3 volume type.
- If there is a cost savings associated with moving the volume type from GP2 to GP3, this will provide a recommendation.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is upgraded. The AWS Pricing API is used to retrieve and calculate the estimated savings which is the expected GP3 cost subtracted from the estimated current GP2 cost of the volume. The incident message detail includes the sum of each resource *Estimated Monthly Savings from moving to gp3* as *Total Estimated Monthly Savings*.

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allowed/Denied Regions* - Whether to treat regions parameter as allow or deny list.
- *Regions* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tag Key:Value* - Cloud native tag to ignore instances that you don't want to consider for downsizing or termination. Format: Key:Value

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeVolumes`
  - `ec2:DescribeRegions`
  - `pricing:GetProducts`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeVolumes",
                  "ec2:DescribeRegions",
                  "pricing:GetProducts"
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

This Policy Template does not incur any cloud costs.
