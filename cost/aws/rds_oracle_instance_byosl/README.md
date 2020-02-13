# AWS RDS BYOSL

## What it does

Check for Oracle RDS database instances that are set to the "License Included" license model. Remediation will update the license model to "Bring Your Own License" and reduce the per minute AWS rate for the Oracle instance since it's covered by a seperate Oracle agreement.

## Functional Details

- This policy identifies all Oracle RDS instances that are set to the "License Included" license model.
- This policy pulls the corresponding CloudWatch CPU utilization metrics for the Oracle RDS database instances.
- The **Exclusion Tag Key:Value** parameter is a string value. Supply the Tag Key & Value. If the exclusion tag is used on an Oracle RDS Instance, that Instance is presumed to be exempt from this policy.
- The license update escalation can be automated, executed after approval, or skipped.
- After the policy escalation has executed the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) method on the recommended resources, the RDS Instance will continue to use its original license model until the next Maintenance Window set on the RDS Instance in AWS. During the next Maintenance Window, the pending license model change will take effect.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - A list of email addresses to notify
- *Exclusion Tag Key:Value* - An AWS-native instance tag to ignore instances that you don't want to consider for license model update.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report.
- Update Oracle RDS license model to "Bring Your Own License" after approval.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

```javascript
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rds:ListTagsForResource",
                "rds:DescribeDBInstances",
                "rds:ModifyDBInstance",
                "cloudwatch:GetMetricStatistics"
            ],
            "Resource": "*"
        }
    ]
}
```

## Supported Clouds

- Amazon

## Cost

This Policy Template does not incur any cloud costs.
