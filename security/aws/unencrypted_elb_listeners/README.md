## AWS Elastic Load Balancer Encryption Check Policy Template

### What it does

Checks for unecrypted listeners on Classic, Network, and Application ELBs. If a listener is using an unecrypted protocol (eg: NOT HTTPS, SSL, or TLS) an incident report will show for the ELB listener and an email will be sent to the user-specified email address.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Required Permissions

This policy requires permissions to describe Classic, Network, and Appplication Elastic Load Balancers.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
{
  "Version": "2012-06-01",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "elasticloadbalancing:DescribeLoadBalancers"
      ],
      "Resource": "*"
    }
  ]
}

{
  "Version": "2015-12-01",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "elasticloadbalancing:DescribeLoadBalancers",
		"elasticloadbalancing:DescribeListeners"
      ],
      "Resource": "*"
    }
  ]
}
```

### Supported Clouds

- AWS

### Cost

This Policy Template does not incur any cloud costs.
