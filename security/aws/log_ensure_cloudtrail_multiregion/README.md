# AWS Ensure CloudTrail Enabled In All Regions

## What it does

AWS CloudTrail is a web service that records AWS API calls for your account and delivers log files to you. It is considered good practice to enable CloudTrail across all regions and this policy will raise an incident if there is not at least one multiregion CloudTrail that meets the requirements.

## Functional Details

The policy leverages the AWS CloudTrail API to obtain a list of trails. Each trail is checked to see if IsMultiRegionTrail is set to "true", IsLogging set to "true", and if the trail has at least one Event Selector with IncludeManagementEvents set to "true" and ReadWriteType set to "All". If no trails are found that meet these criteria, an incident is raised.

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
        "cloudtrail:GetTrailStatus",
        "cloudtrail:GetEventSelectors",
        "cloudtrail:DescribeTrails"
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
