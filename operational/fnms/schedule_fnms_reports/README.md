# Schedule FNMS report
This policy will run a FNMS report (Custom view) and send the result via email.
The policy is a report only policy, no action is taken during the Policy Escalation.

The report / Mail output looks like this:
![Alt text][emailoutput]

Current limitations:
- This only works with the FNMS Cloud
- Output is limited to max 100.000 rows.


# How to setup FNMS Report for this policy:

1. Create a custom view in FlexNet manager that could look like this:
![Alt text][FNMSReport]
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
[emailoutput]: images/email_output.png "email output"
[APIToken]: images/APIToken.png "APIToken"
[CreateServeceAccount]: images/CreateServeceAccount.png "Create Service Account"
[FNMSReport]: images/FNMS_cv_Report.png "FNMS Cloud Instance Report"
[ReportNumber]: images/ReportNumber.png "ReportNumber"
[WebServiceRole]: images/WebServiceRole.png "WebServiceRole"
[CMPToken]: images/CMP_NewToken.png "CMP Token"
