# Reserved Instances Coverage

## What it does

This Policy Template leverages the Reserved Instance Coverage report. Retrieves the reservation coverage for your account.
It will email the user specified in `Email addresses of the recipients you wish to notify`

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Number of days in the past to view Reserved Instance Coverage* - allowed values 7,14,30,90,180,365
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy requires the AWS Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *AWS* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## AWS Required Permissions

This policy requires permissions to describe AWS Cost Explorer GetReservationCoverage.
The AWS credentials will require the following permissions:

```javascript
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ce:GetReservationCoverage",
            "Resource": "*"
        }
    ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
