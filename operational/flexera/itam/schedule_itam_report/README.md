# Schedule ITAM Report

## What It Does

This policy template uses the [Flexera ITAM Cloud REST APIs](https://docs.flexera.com/FlexeraOneAPI/ITAMDataAPI/#api-Reports-reportsExecute) to run a report (Custom View) and email it. [View an example email.](https://raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/operational/flexera/itam/schedule_itam_report/images/email_output.png)

NOTE: Only the first 100,000 rows of the report will be included. This is due to email size limitations.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to send the report to.
- *Flexera ITAM Report ID* - The ID of the Flexera ITAM Custom View Report in Flexera One.
- *Report Title* - The title of the report. This will also be the subject of the report email.
- *Show Full Date/Time* - Whether to show dates with full ISO-8601 formatting in the report. Set to 'No' to just show the date without the time or ISO-8601 formatting.
  - "Yes" Example: 2023-07-02T06:25:36.436Z
  - "No" Example: 2023-07-02

## Policy Actions

- Emails the ITAM report.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `fnms_user`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### Configure ITAM Custom View

You must configure a [Custom View](https://raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/operational/flexera/itam/schedule_itam_report/images/itam_cv_report.png) for the ITAM report that you'd like to email. The report number will be visible in your browser's address bar:

![Report Number](https://raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/operational/flexera/itam/schedule_itam_report/images/report_number.png)

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.
