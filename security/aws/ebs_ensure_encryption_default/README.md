# AWS Ensure EBS Encryption By Default

## What it does

Elastic Compute Cloud (EC2) supports encryption at rest when using the Elastic Block Store (EBS) service. It is possible and recommended to enable this by default for new EBS volumes for every active region. This policy checks the specified regions and raises an incident if any of them are not configured to encrypt new EBS volumes by default.

## Functional Details

When one or more of the provided regions does not have ebsEncryptionByDefault set to "true", this policy raises an incident with a list of the affected regions.

## Input Parameters

- *Allowed/Denied Regions* - Whether to treat regions parameter as allow or deny list.
- *Regions* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

```javascript
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "EC2:DescribeRegions",
                "EC2:GetEbsEncryptionByDefault"
            ],
            "Resource": "*"
        }
    ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
