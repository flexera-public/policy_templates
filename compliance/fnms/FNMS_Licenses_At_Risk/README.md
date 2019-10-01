# FNMS Licenses at risk
This policy will look up the Licenses that are at risk, meaning that there is probably not enough entitlements for the consumed applications.
The policy is a report only policy, no action is taken during the Policy Escalation

The report / Mail output looks like this:
![Alt text][emailoutput]

In addition to the email, the Policy also lists the value in a Teams Channel and a Slack Channel


# How to setup FNMS Report for this policy:

1. Create the report in FlexNet manager to contain these fiels:
![Alt text][FNMSCloudInstanceReport]
Once saved note the report number in thr URL field 
![Alt text][ReportNumber] you need it when activating the Policy

1. Setup the API Token in FNMS:
    1. On the Accounds page - Select Create Account -> Service Account and fill in the form

        ![Alt text][CreateServeceAccount]
    1. IMPORTANT: When you hit save you will see a API Token.. This is the only time you will see it so you need to save it at this point
    
        ![Alt text][APIToken]
    1. Add the new account to the Role ___Webservice___

        ![Alt text][CreateServeceAccount]
1. In CMP Define the Credential: ___FNMS_API_Token___ to contain the Token value from above 


<!-- Image referances -->
[emailoutput]: images/MailOutput_FNMSLicense.png "email output"
[APIToken]: images/APIToken.png "APIToken"
[CreateServeceAccount]: images/CreateServeceAccount.png "Create Service Account"
[FNMSCloudInstanceReport]: images/FNMSCloudInstanceReport.png "FNMS Cloud Instance Report"
[ReportNumber]: images/ReportNumber.png "ReportNumber"
[WebServiceRole]: images/WebServiceRole.png "WebServiceRole"
