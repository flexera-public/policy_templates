# Schedule FlexNet Manager Report

## What it does

This policy uses the SOAP version of the FlexNet Manager Cloud APIs, will run a FlexNet Manager report (Custom view), and send the result via email.

The policy is a report only policy, no action is taken during the Policy Escalation.

The report / Mail output looks like this:
![Alt text][emailoutput]

Current limitations:

- Output is limited to max 100,000 rows.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `Web Service` or equivalent role in IT Asset Accounts (for calling ITAM SOAP APIs)

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## How to setup FlexNet Manager Custom View for this policy

Create a custom view in FlexNet Manager that could look like this: ![Alt text][FNMSReport]

Once saved note the report number in the URL field : ![Alt text][ReportNumber] you need it when activating the Policy

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *FlexNet Manager host* - Flexera One FlexNet Manager host.  *Required*. *Allowed Values: [`slo.app.flexera.com`, `slo.app.flexera.eu`, `slo.app.flexera.au`, `slo-uat.app.flexera.com`, `slo-uat.app.flexera.eu`, `slo-uat.app.flexera.au`]*
- *FlexNet Manager Report ID* - FlexNet Manager Report ID. *Required*.
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
