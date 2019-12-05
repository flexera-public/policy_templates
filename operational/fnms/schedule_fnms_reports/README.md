# Schedule FlexNet Manager report

## What it does

This policy will run a FlexNet Manager report (Custom view) and send the result via email.
The policy is a report only policy, no action is taken during the Policy Escalation.

The report / Mail output looks like this:
![Alt text][emailoutput]

Current limitations:

- This only works with the FNMS Cloud or a onPrem installation available on the internet.

- Output is limited to max 100.000 rows.

## Pre-reqs

- FlexNet Manager
- The following RightScale Credentials
  - FlexNet Manager Cloud
    - 'FNMS_API_Token'

  - FlexNet Manager onPrem (on the internet)
    - 'FNMS_API_Username'
    - 'FNMS_API_Password'

## Installation

### How to setup FlexNet Manager Custom View for this policy:

1. Create a custom view in FlexNet manager that could look like this:
![Alt text][FNMSReport]
Once saved note the report number in thr URL field :
![Alt text][ReportNumber] you need it when activating the Policy

1. Setup the API Token in FNMS Cloud:
    1. On the Account page - Select Create Account -> Service Account and fill in the form

        ![Alt text][CreateServeceAccount]
    1. IMPORTANT: When you hit save you will see a API Token.. This is the only time you will see it so you need to save it at this point
        ![Alt text][APIToken]
    1. Add the new account to the Role ___Webservice___

        ![Alt text][WebServiceRole]

1. Set Up user for FNMS onPrem:
    You can use a normal interactive user for the API credentials, but it is recommended to add a special service user for the API connection.
    1. In your user management add the new user and assign it a password.
    1. On the Account page - Select Create Account -> Service Account
    ![Alt text][CreateServeceAccount]
    1. in the Account field; select the newly created account and fill in the form.
    1. Add the new account to the Role ___Webservice___

        ![Alt text][WebServiceRole]

### Cloud manager

1. Create RightScale Credentials with values that match the authentication method used.
    1. For FlexNet manager Cloud - Add the FlexNet Manager API Token (Credential name: `FNMS_API_Token`)
    1. For FlexNet Manager onPrem (on the internet) - Add two Credentials : (Credential name: `FNMS_API_Username` and Credential name: `FNMS_API_Password`)

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *FNMS Report URL* - Full FlexNet URL (e.g. https://demo.flexnetmanager.com/Suite )
- *FNMS Report ID* - FlexNet manager Custom View ID
- *Report Title in the Mail* - Report header in the report result
- *Email addresses of the recipients you wish to notify* - A list of email addresse(s) to notify

## Policy Actions

No actions

## Required RightScale Roles

- Cloud Management - Actor
- Cloud Management - Observer
- Cloud Management - credential_viewer

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
