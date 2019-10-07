## FlexNet Manager Licenses At Risk.

### What it does
This policy looks up all FlexNet Manager Licenses that are at risk and lists them. A License at Risk is a License that is unable to cover the current license consumption.

The report / Mail output looks like this:
![Alt text][emailoutput]

Current limitations:
- This policy currently only works with the FlexNet Manager Cloud.
- Output is limited to max 100000 rows.

### Installation

#### How to setup FlexNet Manager for this policy

1. Create a report in FlexNet manager that contains these fields:
![Alt text][FNMSCloudInstanceReport]
Once saved, note the report number in thr URL field:
![Alt text][ReportNumber] you need it when activating the Policy.

1. Setup the API Token in FlexNet Manager:
    1. On the Account page - Select Create Account -> Service Account and fill in the form

        ![Alt text][CreateServeceAccount]
    1. IMPORTANT: When you hit save you will see a API Token. This is the only time you will see it, so you need to save it at this point.

        ![Alt text][APIToken]
    1. Add the new account to the Role ___Webservice___

        ![Alt text][WebServiceRole]

#### Cloud manager

1. Create RightScale Credentials with values that match the FlexNet Manager API Token (Credential name: `FNMS_API_Token`).

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *FNMS Report URL* - Full FlexNet URL (e.g. https://demo.flexnetmanager.com/Suite )
- *FNMS Report ID* - FlexNet manager Custom View ID
- *Email addresses of the recipients you wish to notify* - A list of email addresse(s) to notify

### Policy Actions
No actions

### Cost
This Policy Template does not incur any additional cloud costs.

<!-- Image referances -->
[emailoutput]: images/MailOutput_FNMSLicense.png "email output"
[APIToken]: images/APIToken.png "APIToken"
[CreateServeceAccount]: images/CreateServeceAccount.png "Create Service Account"
[FNMSCloudInstanceReport]: images/FNMSCloudInstanceReport.png "FNMS Cloud Instance Report"
[ReportNumber]: images/ReportNumber.png "ReportNumber"
[WebServiceRole]: images/WebServiceRole.png "WebServiceRole"

