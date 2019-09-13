# AWS Idle Compute Instances Policy

## What it does

This Policy Template checks for idle instance in AWS EC2 and then terminates them upon approval.

## Functional Details

- This policy identifies all instances reporting performance metrics to CloudWatch whose CPU or Memory utilization is below the thresholds set in the **Average used memory percentage** and **Average used CPU percentage** parameters. These thresholds are what you would consider to be and idle instance.
- The **Exclusion Tag Key:Value** parameter is a string value. If the exclusion tag is used on an Instance, that Instance is presumed to be exempt from this policy.
- This policy can terminate instances after approval for instances that match the criteria.
- If you get an **N/A** in a field you will need to install the [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) on the instance to get those metrics.
- This policy only pulls running instances, as it is unable to get correct monitoring metrics from instances in other states.

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
}
```

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Average used memory percentage* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Average used CPU percentage* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Exclusion Tag Key:Value* - Cloud native tag to ignore instances. Format: Key:Value

### Cloud Management Required Permissions/AWS Required Permissions

- Cloud Management - The `credential_viewer`,`observer` roles
- AWS - The `CloudWatchReadOnlyAccess` AWS IAM Policy

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

### Supported Clouds

- Amazon

### Cost

This Policy Template does not incur any cloud costs.
