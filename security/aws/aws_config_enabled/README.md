# AWS Ensure AWS Config Enabled In All Regions

## What It Does

This policy template reports any AWS regions that do not have Config enabled or sufficiently configured. Optionally, this report can be emailed.

## Functional Details

The AWS Config API is used to gather the AWS Config information for all regions. When a region is found that has no AWS Config settings, or the AWS Config recordingGroup has `allSupported` or `includeGlobalResourceTypes` set to 'false', that region and these settings are added to a list. An incident is raised if this list contains any regions.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
          "EC2:DescribeRegions",
          "config:DescribeConfigurationRecorderStatus"
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
