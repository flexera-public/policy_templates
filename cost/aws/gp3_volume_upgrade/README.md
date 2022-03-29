# AWS GP3 Upgradeable Volumes

## What it does

This Policy finds GP2, IO1, or IO2 volumes in the given account and recommends them for upgrade to GP3 if that would provide savings. A Policy Incident will be created with all of volumes that fall into these criteria.

Optionally, the user can specify one or more tags that if found on a volume will exclude the volume from the list.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is Upgraded. It uses the AWS Pricing API to calculate the estimated savings along with the AWS Enterprise Discount Program percentage that is calculated from costs in Optima. You can also set the *AWS EDP Percentage* parameter to a non-negative number to use for the discount percentage instead. The savings are displayed in the *Estimated Monthly Savings* column. The incident detail message includes the sum of each resource *Estimated Monthly Savings* as *Total Estimated Monthly Savings*.

If the AWS bill for the AWS account is registered in Optima in a different Flexera One org than the project where the policy template is applied, the *Flexera One Org ID for Optima* parameter can be set to the org where the AWS account is registered in Optima. Leaving this parameter set to `current` will result in using the same org as the project where the policy template is applied querying for Optima cost data.

If the user does not have the minimum required role of `billing_center_viewer` or if there is not enough data received from Optima to calculate savings, an appropriate message is displayed in the incident detail message and the *AWS EDP Percentage* will be calculated as 0% unless the *AWS EDP Percentage* parameter is set to a non-negative number.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses* - A list of email addresses to notify
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Exclude Tags.* - A list of tags used to excluded volumes from the incident.
- *AWS EDP Percentage* - The AWS Enterprise Discount Program percentage, by default this is calculated from Flexera Optima costs
- *Flexera One Org ID for Optima* - The Flexera One org ID for Optima queries used to determine estimated costs, by default the current org is used.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

- This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.
- billing_center_viewer (note: this role must be applied at the Organization level)

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

The following AWS permissions must be allowed for the policy to run.

```json
{
  "Version": "2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Action":[
        "ec2:DescribeVolumes",
        "ec2:DescribeRegions",
        "pricing:GetProducts"
      ],
      "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
