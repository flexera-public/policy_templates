# Schedule Flexnet Manager Report - On Premise

## What it does

This policy runs on the Flexnet Manager On Premise instance and will run a FlexNet Manager report (Custom view) and send the result via email.
The policy is a report only policy, no action is taken during the Policy Escalation.

The report / Mail output looks like this:
![Alt text][emailoutput]

Current limitations:

- Output is limited to max 100.000 rows.

## Prerequisites

This policy requires the Flexnet Manager NTLM Credential. When applying the policy select the
appropriate credentials from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value **flexera_fnms_ntlm** in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

If FlexNet Manager Suite is not accessible from the Internet, you will need to setup a wstunnel to
provide a secure connection into the FlexNet manager system.  For more details on wstunnel
please refer to this: [https://github.com/rightscale/wstunnel](https://github.com/rightscale/wstunnel)

## Installation

### How to setup FlexNet Manager Custom View for this policy

1. Create a custom view in FlexNet manager that could look like this: ![Alt text][FNMSReport] Once saved note the report number in the URL field : ![Alt text][ReportNumber] you need it when activating the Policy
1. Set Up user for FlexNet manager on-premise:
    1. In your user management add the new user and assign it a password.
    1. On the Account page - Select Create Account -> Service Account ![Alt text][CreateServeceAccount]
    1. in the Account field; select the newly created account and fill in the form.
    1. Add the new account to the Role ___Webservice___ ![Alt text][WebServiceRole]

__NOTE__: You can use a normal interactive user for the API credentials, but it is recommended to add a
special service user for the API connection.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *FNMS Report URL* - Full FlexNet URL (e.g. [https://demo.flexnetmanager.com/Suite](https://demo.flexnetmanager.com/Suite) )
- *FNMS Report ID* - FlexNet manager Custom View ID
- *Report Title in the Mail* - Report header in the report result
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

- send an email

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.

<!-- Image references -->
[emailoutput]: images/email_output.png "email output"
[APIToken]: images/APIToken.png "APIToken"
[CreateServeceAccount]: images/CreateServeceAccount.png "Create Service Account"
[FNMSReport]: images/FNMS_cv_Report.png "FNMS Cloud Instance Report"
[ReportNumber]: images/ReportNumber.png "ReportNumber"
[WebServiceRole]: images/WebServiceRole.png "WebServiceRole"
[CMPToken]: images/CMP_NewToken.png "CMP Token"
