# AWS Expiring Savings Plans

## What it does

This Policy Template leverages the Savings Plan API for savings plan information. It will notify only if expiration is within the timeframe specified in `Number of days to prior to expiration date to trigger incident` field. It will email the user specified in `Email addresses of the recipients you wish to notify`.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Number of days to prior to expiration date to trigger incident* - enter the number of days you want before the Reserved Instance expires.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Required AWS Roles

{
  "Version": "2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Action":["savingsplans"],
      "Resource":"*",
      "Condition":{
        "Bool":{
          "aws:SecureTransport":"true"
        }
      }
    }
  ]
}

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
