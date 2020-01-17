# AWS Inefficient Instance Utilization using CloudWatch

## What it does

This Policy Template gathers AWS instances with inefficient utilization using CloudWatch CPU and Memory Metrics over a 30 day average and downsized after approval.

## Functional Details

This policy identifies all running instances reporting performance metrics to CloudWatch whose CPU or Memory utilization is below the thresholds set in the **Average used memory percentage** and **Average used CPU percentage** parameters.

The **Exclusion Tag Key** parameter is a string value.  Supply the Tag Key only.  Tag Values are not analyzed and therefore are not need.  If the exclusion tag key is used on an Instance, that Instance is presumed to be exempt from this policy.

Inefficient Instances are resized to the next smaller size within the same class.  If the instance is already on the smallest size for the class it will not be resized. Resize only occurs after approval

If you get an **N/A** in a field you will need to install the [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) on the instance to get those metrics.

## Policy Actions

- Sends an email notification
- Downsizes instances after approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

```javascript
{
  "Version":"2012-10-17",
  "Statement":[{
    "Effect":"Allow",
    "Action":["cloudwatch:GetMetricStatistics","cloudwatch:ListMetrics"],
    "Resource":"*",
    "Condition":{
      "Bool":{
              "aws:SecureTransport":"true" 
             }
      }
    }
  ]
}
```

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Average used memory percentage* - Set to -1 to ignore memory utilization
- *Average used CPU percentage* - Set to -1 to ignore CPU utilization
- *Exclusion Tag Key:Value* - Cloud native tag key to ignore instances. Format: Key:Value

## Windows Support

To enable windows support you will need to add the following to your cloudwatch config.json and restart cloudwatch agent

```json
"metrics": {
  "append_dimensions": {
    "AutoScalingGroupName": "${aws:AutoScalingGroupName}",
    "ImageId": "${aws:ImageId}",
    "InstanceId": "${aws:InstanceId}",
    "InstanceType": "${aws:InstanceType}"
  }
}
```

## Supported Clouds

- Amazon

## Observation Period

By default, this policy calculates utilization over a 30 day period.
To calculate over a different period of time, you can update the policy template.  Replace the `30` wherever you see `var start_date = new Date(new Date().setDate(new Date().getDate() - 30)).toISOString();` with the new number of days you want to use.
Depending on the number of days you choose to collect metrics for, you may need to update the `period` property.For 30 days, we use the value of `2592000`, which is 30 days in seconds.You will need to update the value wherever you see `'Period': "2592000",`.For more details, see the official [AWS CloudWatch API Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html).

## Cost

This Policy Template does not incur any cloud costs.
