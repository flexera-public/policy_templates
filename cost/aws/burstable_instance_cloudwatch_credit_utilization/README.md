# AWS Burstable Instance CloudWatch Utilization Policy

## What it does

This Policy Template gathers AWS CloudWatch data for instances on 30 day intervals. Information on Burst Credits can be found [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-monitoring-cpu-credits.html). This policy will then take the appropriate actions based on which check fails and resize the instance.

## Functional Details

- This policy identifies all instances reporting performance metrics to CloudWatch whose CPU, Burst Credit Balance, Surplus Burst Credit Balance meet specified thresholds set forth in the parameters.
- The **Exclusion Tag** parameter is a string value. If the exclusion tag is used on an Instance, that Instance is presumed to be exempt from this policy.
- If you get an **N/A** in a field you will need to install the [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) on the instance to get those metrics.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Number of Surplus Credits to alert on* - Number of CPU Surplus Credits to report on, Set to -1 to ignore cpu burst credits
- *Enable checking burst credit balance against max* - checks burst credit balance against max_earnable_credits
- *Exclusion Tag* - Cloud native tag key to ignore instances. Format: Key:Value
- *Cooldown Days* - Days to cooldown between checks of same instance

## Policy Actions

- Sends an email notification.
- Resizing instances after approval.

## Prerequisites

This policy requires the AWS IAM or AWS STS Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *AWS* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## AWS Required Permissions

This policy requires permissions to list Metrics and Get Metric Statistics from the AWS Cloudwatch API.
The credentials will require the following permissions:

```javascript
{
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
   ]
}
```

```javascript
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances"
            ],
            "Resource": "arn:aws:ec2:*:*:instance/*",
        },
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeInstances",
            "Resource": "*"
        }
    ]
}
```

## Supported Clouds

- Amazon

## Cost

This Policy Template does not incur any cloud costs.
