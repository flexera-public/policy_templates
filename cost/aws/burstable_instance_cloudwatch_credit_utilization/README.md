## AWS Burstable Instance CloudWatch Utilization Policy

### What it does

This Policy Template gathers AWS CloudWatch data for instances on 30 day intervals. Information on Burst Credits can be found [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-monitoring-cpu-credits.html). This policy will then take the appropriate actions based on which check fails and resize the instance.

### Cloud Management Required Permissions/AWS Required Permissions
- Cloud Management - The `credential_viewer`,`observer` roles
- Cloud Management - The `policy_designer`, `policy_manager` & `policy_publisher` roles
- AWS - The `CloudWatchReadOnlyAccess` AWS IAM Policy

### Functional Details

- This policy identifies all instances reporting performance metrics to CloudWatch whose CPU, Burst Credit Balance, Surplus Burst Credit Balance meet specified thresholds set forth in the parameters.
- The **Exclusion Tag** parameter is a string value. If the exclusion tag is used on an Instance, that Instance is presumed to be exempt from this policy.
-  If you get an **N/A** in a field you will need to install the [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) on the instance to get those metrics. 

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Number of Surplus Credits to alert on* - Number of CPU Surplus Credits to report on, Set to -1 to ignore cpu burst credits
- *Enable checking burst credit balance against max* - checks burst credit balance against max_earnable_credits, if they are equal it will report. 
- *Exclusion Tag* - An AWS native instance tag to ignore instances that you don't want to consider for resizing. 
- *Cooldown Days* - Days to cooldown between checks of same instance

### AWS Required Permissions

This policy requires permissions to list Metrics and Get Metric Statistics from the AWS Cloudwatch API.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

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


### Supported Clouds

- Amazon

### Cost

This Policy Template does not incur any cloud costs.