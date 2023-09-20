# Azure Instances not running FlexNet Inventory Agent

## What it does

This policy uses the SOAP version of the FlexNet Manager Cloud APIs, checks all instances running in Azure to determine if the FlexNet Inventory Agent is running on the instance, and reports on any that are missing the agent.

The policy is a recommendation only policy, no action is taken during the Policy Escalation.

## Functional Details

The policy leverages the cloud API to get all current instances and the FlexNet Manager report (Custom view) API to get all azure cloud instances with agent. It cross-checks the two lists to determine if any instances are running on the cloud that aren't known to FlexNet Manager.  The policy matches the ComputerName from FlexNet Manager System and the VirtualMachine.name from Azure.

Current limitations:

- Output is limited to max 100000 rows.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked
- *Exclusion Tag Key* - Azure-native Virtual machines tag to ignore VM's which has FNMS inventory agent running. Only supply the tag key. The policy assumes that the tag value is irrelevant.
- *FlexNet Manager host* - Flexera One FlexNet Manager host.  *Required*. *Allowed Values: [`slo.app.flexera.com`, `slo.app.flexera.eu`, `slo.app.flexera.au`, `slo-uat.app.flexera.com`, `slo-uat.app.flexera.eu`, `slo-uat.app.flexera.au`]*
- *FlexNet Manager Report ID* - FlexNet Manager Report ID. *Required*.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `Web Service` or equivalent role in IT Asset Accounts (for calling ITAM SOAP APIs)

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## How to setup FlexNet Manager Custom View for this policy

Create a custom view in FlexNet manager that could look like this: ![Alt text][FNMSReport]

Click on Preview and filter.
Select `Microsoft Azure` under `Inventory device` > `Hosted in` ![Alt text][FilterFNMSReport]

Once saved, note the report number in the URL field : ![Alt text][ReportNumber] you need it when activating the Policy for 'FNMS Report ID'.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.

<!-- Image referances -->
[APIToken]: images/APIToken.png "APIToken"
[CreateServeceAccount]: images/CreateServeceAccount.png "Create Service Account"
[FNMSReport]: images/FNMS_cv_Report.png "FNMS Cloud Instance Report"
[FilterFNMSReport]: images/Filter_FNMS_Report.PNG "FNMS Microsoft Azure Instance Report"
[ReportNumber]: images/ReportNumber.png "ReportNumber"
[WebServiceRole]: images/WebServiceRole.png "WebServiceRole"
[CMPToken]: images/CMP_NewToken.png "CMP Token"
