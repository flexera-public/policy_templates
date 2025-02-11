# Schedule ITAM Report

## What It Does

This policy uses the [REST version of the Flexera ITAM Cloud APIs](https://docs.flexera.com/FlexeraOneAPI/ITAMDataAPI/#api-Reports-reportsExecute), will run a report (Custom view), and send the result via email.

The policy is a report only policy, no action is taken during the Policy Escalation.

The report / Mail output looks like this:
![Alt text][emailoutput]

Current limitations:

- Report output is recommended to max 100,000 rows.  This is due to the limitation in e-mail body size.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Flexera ITAM Report ID* - ITAM Report ID. *Required*.
- *Report Title in the Mail* - Report header in the report result
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

- Send an email

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `fnms_user`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Configure ITAM Custom View

Create a custom view in ITAM that could look like this: ![Alt text][FNMSReport]

Once saved note the report number in the URL field : ![Alt text][ReportNumber] you need it when activating the policy template.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.

<!-- Image references -->
[emailoutput]: images/email_output.png "email output"
[APIToken]: images/APIToken.png "APIToken"
[CreateServeceAccount]: images/CreateServeceAccount.png "Create Service Account"
[FNMSReport]: images/FNMS_cv_Report.png "FNMS Cloud Instance Report"
[ReportNumber]: images/ReportNumber.png "ReportNumber"
[WebServiceRole]: images/WebServiceRole.png "WebServiceRole"
[CMPToken]: images/CMP_NewToken.png "CMP Token"
