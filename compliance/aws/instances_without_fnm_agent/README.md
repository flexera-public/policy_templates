# AWS EC2 Instances not running FlexNet Inventory Agent

## What it does

This policy checks all EC2 instances running in AWS to determine if the FlexNet Inventory Agent is running on the instance and reports on any that are missing the agent.
The policy is a recommendation only policy, no action is taken during the Policy Escalation.

## Functional Description

The policy leverages the cloud API to get all current EC2 instances and the FlexNet Manager report (Custom view) API to get all AWS cloud instances with agent. It cross-checks the two lists to determine if any instances are running on the cloud that aren't known to FlexNet Manager.  The policy matches the InstanceCloudID from FlexNet Manager System and the instanceId from AWS.

## Prerequisites

- FlexNet Manager
- The following RightScale Credentials
- 'FNMS_API_Token'

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Tags to ignore* - List of tags that will exclude EC2 instance from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'.
- *FNMS Report ID* - FlexNet Manager System Custom View ID.

## Policy Actions

- Send an email report

## Required Permissions

### Required RightScale Roles

- `policy_manager`
- `credential_viewer`

### AWS Required Permissions

This policy requires permissions to describe EBS volumes.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
 {
    "Version": "2016-11-15",
    "Statement":[{
                  "Effect":"Allow",
                  "Action":["ec2:DescribeInstances"],
                  "Resource":"*"
                }]
 }
```

## Installation

### How to setup FlexNet Manager Custom View for this policy

1. Create a custom view in FlexNet manager that could look like this:

![Alt text][FNMSReport]

Click on Preview and filter.
Select `Amazon Web Services` under `Inventory device` > `Hosted in`

![Alt text][FilterFNMSReport]

Once saved, note the report number in thr URL field :
![Alt text][ReportNumber] you need it when activating the Policy for 'FlexNet Manager System Report ID'.

1. Setup the API Token in FlexNet Manager System:

    1. On the Account page - Select Create Account -> Service Account and fill in the form

        ![Alt text][CreateServeceAccount]
    1. IMPORTANT: When you hit save you will see a API Token.. This is the only time you will see it so you need to save it at this point

        ![Alt text][APIToken]
    1. Add the new account to the Role ___Webservice___

        ![Alt text][WebServiceRole]

### Cloud manager

1. Create RightScale Credentials with values that match the FlexNet Manager API Token (Credential name: `FNMS_API_Token`)

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.

<!-- Image referances -->
[APIToken]: images/APIToken.png "APIToken"
[CreateServeceAccount]: images/CreateServeceAccount.png "Create Service Account"
[FNMSReport]: images/FNMS_cv_Report.png "FNMS Cloud Instance Report"
[FilterFNMSReport]: images/Filter_FNMS_Report.PNG "FNMS Amazon Web Services Instance Report"
[ReportNumber]: images/ReportNumber.png "Report Number"
[WebServiceRole]: images/WebServiceRole.png "WebServiceRole"
[CMPToken]: images/CMP_NewToken.png "CMP Token"
