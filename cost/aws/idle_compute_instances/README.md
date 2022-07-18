# AWS Idle Compute Instances Policy

## What it does

This Policy Template checks for idle instance in AWS EC2 and then terminates them upon approval.

## Functional Details

- This policy identifies all instances reporting performance metrics to CloudWatch whose CPU or Memory utilization is below the thresholds set in the **Average used memory percentage** and **Average used CPU percentage** parameters. These thresholds are what you would consider to be and idle instance.
- The **Exclusion Tag Key:Value** parameter is a string value. If the exclusion tag is used on an Instance, that Instance is presumed to be exempt from this policy.
- This policy can terminate instances after approval for instances that match the criteria.
- If you get an **N/A** in a field you will need to install the [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) on the instance to get those metrics.
- This policy only pulls running instances, as it is unable to get correct monitoring metrics from instances in other states.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. Optima is used to receive the estimated savings which is the product of the most recent full day's cost of the resource * 30. The savings is displayed in the Estimated Monthly Savings column. If the resource can not be found in Optima the value is 0.0. The incident detail message includes the sum of each resource Estimated Monthly Savings as Total Estimated Monthly Savings. The savings value is rounded off to 3 decimal places.
If the user is not having the minimum required role of `billing_center_viewer` or if there is no enough data received from Optima to calculate savings, appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as 0.0 in the incident table.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Average used memory percentage* - Set to -1 to ignore memory utilization
- *Average used CPU percentage* - Set to -1 to ignore CPU utilization
- *Idle for both CPU/Memory or either* - Set to Both CPU and Memory to consider an instance idle only if it is below both the CPU and memory utilization parameters. Set to Either CPU or Memory to consider an instance idle if either CPU or memory are below the parameter values. Has no effect if either of the utilization parameters are set to -1.
- *Exclusion Tag Key:Value* - Cloud native tag to ignore instances. Format: Key:Value
- *CloudWatch API Wait Time* - The amount of time in seconds to wait between requests to the CloudWatch API to avoid being throttled by AWS. Default is recommended.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

- Sends an email notification
- Terminates instances after approval

## Prerequisites

- This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.
- billing_center_viewer (note: this role must be applied at the Organization level)

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

```javascript
{
  "Version": "2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Action":[
        "cloudwatch:GetMetricStatistics",
        "cloudwatch:ListMetrics"
      ],
      "Resource":"*",
      "Condition":{
        "Bool":{
          "aws:SecureTransport":"true"
        }
      }
    },
    {
      "Effect":"Allow",
      "Action":[
        "ec2:DescribeInstances",
        "ec2:DescribeTags",
        "ec2:DescribeRegions"
      ],
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

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
