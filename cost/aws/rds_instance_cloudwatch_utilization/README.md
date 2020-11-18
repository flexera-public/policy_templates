# AWS Rightsize RDS Instances

## What it does

This Policy Template gathers AWS CloudWatch data for RDS Instances on 30 day intervals and provides rightsizing recommendations.  Once recommendations are generated, instances can be rightsized in an automated manner or after approval.

## Functional Details

- This policy identifies all RDS instances reporting performance metrics to CloudWatch whose CPU utilization is below the thresholds set in the **Average used CPU % - Downsize Threshold** and **Average used CPU % - Upsize Threshold** parameters.
- The **Exclusion Tag Key:Value** parameter is a string value.  Supply the Tag Key & Value.  If the exclusion tag is used on an RDS Instance, that Instance is presumed to be exempt from this policy.
- The rightsizing escalation can be automated, executed after approval, or skipped.
- After the policy escalation has executed the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) method on the recommended resources, the RDS Instance will continue to use its original Instance Class until the next Maintenance Window set on the RDS Instance in AWS.  During the next Maintenance Window, the pending Instance Class change will take effect.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. Click [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) to check regions in AWS and enter the region code. If this field is left empty, then the policy will throw an error.
- *Email addresses to notify* - A list of email addresses to notify
- *Average used CPU % - Upsize threshold* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Average used CPU % - Downsize Threshold* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Exclusion Tag Key:Value* - An AWS-native instance tag to ignore instances that you don't want to consider for resizing. Only supply the tag key
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Resize Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be resized.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Resizes RDS Instances after approval.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

- Read access to CloudWatch & RDS

```javascript
{
  "Version": "2012-10-17",
  "Statement":[{
  "Effect":"Allow",
  "Action":["ec2:DescribeRegions"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
