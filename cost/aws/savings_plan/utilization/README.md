# AWS Savings Plan Utilization

## What it does

This Policy Template leverages the [AWS Savings Plans Utilization API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansUtilization.html). It will raise incidents if the Utilization of the Savings Plan (specified in the *Savings Plan ARN* parameter) is below the *Savings Plan Utilization Threshold* parameter in the policy. It will email the user specified in *Email addresses to notify*.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Look Back Period* - Specify the number of days of past usage to analyze.
- *Savings Plan ARN* - The unique Amazon Resource Name (ARN) for a particular Savings Plan
- *Savings Plan Utilization Threshold* - Specify the minimum Savings Plan Utilization threshold as a percentage that should result in an alert
- *Email addresses to notify* - A list of email addresses to notify

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

## Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

```javascript
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ce:*"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
