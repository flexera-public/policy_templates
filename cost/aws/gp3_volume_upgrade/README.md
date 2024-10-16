# AWS GP3 Upgradeable Volumes

## Deprecated

This policy is no longer being updated. The [AWS Rightsize EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ebs_volumes/) policy should be used for these recommendations instead.

Note that the above policy does not report on IO1 or IO2 volumes. These volumes are high performance volumes, so changing them to GP3 will result in a performance downgrade and may cause issues for workloads that rely on this performance.

## What It Does

This Policy finds GP2, IO1, or IO2 volumes in the given account and recommends them for upgrade to GP3 if that would provide savings. A Policy Incident will be created with all of volumes that fall into these criteria.

Optionally, the user can specify one or more tags that if found on a volume will exclude the volume from the list.

### Policy Savings Details

The policy includes the estimated savings. The estimated savings is recognized if the resource is Upgraded. It uses the AWS Pricing API to calculate the estimated savings along with the AWS Enterprise Discount Program percentage that is calculated from costs in Optima. You can also set the *AWS EDP Percentage* parameter to a non-negative number to use for the discount percentage instead. The savings are displayed in the *Estimated Monthly Savings* column. The incident detail message includes the sum of each resource *Estimated Monthly Savings* as *Total Estimated Monthly Savings*.

If the AWS bill for the AWS account is registered in Optima in a different Flexera One org than the project where the policy template is applied, the *Flexera One Org ID for Optima* parameter can be set to the org where the AWS account is registered in Optima. Leaving this parameter set to `current` will result in using the same org as the project where the policy template is applied querying for Optima cost data.

If the user does not have the minimum required role of `billing_center_viewer` or if there is not enough data received from Optima to calculate savings, an appropriate message is displayed in the incident detail message and the *AWS EDP Percentage* will be calculated as 0% unless the *AWS EDP Percentage* parameter is set to a non-negative number.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

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

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed/Denied Regions* - Whether to treat regions parameter as allow or deny list.
- *Regions* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses* - A list of email addresses to notify
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Exclude Tags.* - A list of tags used to excluded volumes from the incident.
- *AWS EDP Percentage* - The AWS Enterprise Discount Program percentage, by default this is calculated from Flexera Optima costs
- *Flexera One Org ID for Optima* - The Flexera One org ID for Optima queries used to determine estimated costs, by default the current org is used.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
