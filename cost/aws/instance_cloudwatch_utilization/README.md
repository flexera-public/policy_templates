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

This policy requires the AWS IAM or AWS STS Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *AWS* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify*
- A list of email addresses to notify- *Average used memory percentage*
- Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Average used CPU percentage* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Exclusion Tag Key* - An AWS-native instance tag to ignore instances that you don't want to consider for downsizing. Only supply the tag key

## Required Permissions

### AWS Required Permissions

This policy requires permissions to list Metrics and Get Metric Statistics from the AWS Cloudwatch API. The AWS credentials contained in those credentials will require the following permissions:
```javascript{
  "Version": "2012-10-17",
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
]}```

### Windows Support

To enable windows support you will need to add the following to your cloudwatch config.json and restart cloudwatch agent

```json
"metrics": {
  "append_dimensions": {
    "AutoScalingGroupName": "${aws:AutoScalingGroupName}",
    "ImageId": "${aws:ImageId}",
    "InstanceId": "${aws:InstanceId}",
    "InstanceType": "${aws:InstanceType}"
  }
}```

## Supported Clouds

- Amazon

## Observation Period

By default, this policy calculates utilization over a 30 day period.
To calculate over a different period of time, you can update the policy template.  Replace the `30` wherever you see `var start_date = new Date(new Date().setDate(new Date().getDate() - 30)).toISOString();` with the new number of days you want to use.
Depending on the number of days you choose to collect metrics for, you may need to update the `period` property.For 30 days, we use the value of `2592000`, which is 30 days in seconds.You will need to update the value wherever you see `'Period': "2592000",`.For more details, see the official [AWS CloudWatch API Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html).

## Cost

This Policy Template does not incur any cloud costs.