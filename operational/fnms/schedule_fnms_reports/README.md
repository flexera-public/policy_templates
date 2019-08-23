# Schedule FNMS report
This policy will run a FNMS report and send the result via email.
The policy is a report only policy, no action is taken during the Policy Escalation

The report / Mail output looks like this:
![Alt text][emailoutput]

# How to setup FNMS Report for this policy:

1. Create a report in FlexNet manager that could look like this:
![Alt text][FNMSCloudInstanceReport]
Once saved note the report number in thr URL field :
![Alt text][ReportNumber] you need it when activating the Policy

1. Setup the API Token in FNMS:
    1. On the Account page - Select Create Account -> Service Account and fill in the form

        ![Alt text][CreateServeceAccount]
    1. IMPORTANT: When you hit save you will see a API Token.. This is the only time you will see it so you need to save it at this point
    
        ![Alt text][APIToken]
    1. Add the new account to the Role ___Webservice___

        ![Alt text][WebServiceRole]

1. In CMP Define the Credential: ___FNMS_API_Token___ to contain the Token value from above: 
    ![Alt text][CMPToken]


<!-- Image referances -->
[emailoutput]: images/MailOutput_FNMSLicense.png "email output"
[APIToken]: images/APIToken.png "APIToken"
[CreateServeceAccount]: images/CreateServeceAccount.png "Create Service Account"
[FNMSCloudInstanceReport]: images/FNMSCloudInstanceReport.png "FNMS Cloud Instance Report"
[ReportNumber]: images/ReportNumber.png "ReportNumber"
[WebServiceRole]: images/WebServiceRole.png "WebServiceRole"
[CMPToken]: images/CMP_NewToken.png "CMP Token"
