# FlexNet Manager Low Available Licenses

## What it does

This policy uses a FlexNet Manger Cloud and looks up all FlexNet Manager Licenses that has lower than user provided percentage.

The report / Mail output looks like this:
![Alt text][emailoutput]

Current limitations:

- Output is limited to max 100000 rows.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *FNMS Report URL* - Full FlexNet URL (e.g. <https://demo.flexnetmanager.com/Suite> or WStunnel tunnel URL <https://wstunnel1-1.rightscale.com/_token/<token>/> )
- *FNMS Report ID* - FlexNet manager Custom View ID
- *Email addresses of the recipients you wish to notify* - A list of email addresse(s) to notify
- *Percentage Available* - Percentage threshold of available licenses

## Policy Actions

- Send an email report

## Prerequisites

For On Premise If FlexNet Manager Suite is not accessible from the Internet, you will need to setup a wstunnel to provide a secure connection into the FlexNet manager system.For more details on wstunnel please refer to this: [https://github.com/rightscale/wstunnel](https://github.com/rightscale/wstunnel)

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

 For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

- Credential type:

  - *API Key* - For FNMS Cloud  -  (*Location*:header, *Type*: Bearer)

  or
  - *NTLM* - For On Premise FNMS

- Provider : *flexera_fnms*

## Installation

### How to setup FlexNet Manager for this policy

a. Cloud

1. Create a report in FlexNet manager that contains these fields:![Alt text][FNMSReport]Once saved, note the report number in the URL field:![Alt text][ReportNumber] you need it when activating the Policy.
1. Retrieve the API Token in FlexNet Manager (Cloud):
    1. On the Account page - Select Create Account -> Service Account and fill in the form ![Alt text][CreateServeceAccount]
    1. IMPORTANT: When you hit save you will see a API Token. This is the only time you will see it, so you need to save it at this point. ![Alt text][APIToken]

1. Ensure that the Account used has the Role ___Webservice___ assigned! [Alt text][WebServiceRole]

b. On Premise

1. Create a custom view in FlexNet manager that could look like this: ![Alt text][FNMSReport]

Click on Preview and filter.
Select `Amazon Web Services` under `Inventory device` > `Hosted in` ![Alt text][FilterFNMSReport]

Once saved, note the report number in the URL field : ![Alt text][ReportNumber] you need it when activating the Policy for 'FlexNet Manager System Report ID'.

1. Set Up user for FlexNet manager on-premise:
    1. In your user management add the new user and assign it a password.
    1. On the Account page - Select Create Account -> Service Account ![Alt text][CreateServeceAccount]
    1. in the Account field; select the newly created account and fill in the form.
    1. Add the new account to the Role ___Webservice___ ![Alt text][WebServiceRole]

__NOTE__: You can use a normal interactive user for the API credentials, but it is recommended to add a special service user for the API connection.

## Cost

This Policy Template does not incur any additional cloud costs.

<!-- Image referances -->
[APIToken]: images/APIToken.png "APIToken"
[CreateServeceAccount]: images/CreateServeceAccount.png "Create Service Account"
[FNMSReport]: images/FNMS_cv_Report.png "FNMS Cloud Instance Report"
[ReportNumber]: images/ReportNumber.png "ReportNumber"
[WebServiceRole]: images/WebServiceRole.png "WebServiceRole"