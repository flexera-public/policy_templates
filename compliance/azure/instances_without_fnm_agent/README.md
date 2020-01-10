# Azure Instances not running FlexNet Inventory Agent

## What it does

This policy checks all instances running in Azure to determine if the FlexNet Inventory Agent is running on the instance and reports on any that are missing the agent.
The policy is a recommendation only policy, no action is taken during the Policy Escalation.

## Functional Details

The policy leverages the cloud API to get all current instances and the FlexNet Manager report (Custom view) API to get all azure cloud instances with agent. It cross-checks the two lists to determine if any instances are running on the cloud that aren't known to FlexNet Manager.  The policy matches the ComputerName from FlexNet Manager System and the VirtualMachine.name from Azure.

Current limitations:

- Output is limited to max 100000 rows.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Exclusion Tag Key* - Azure-native Virtual machines tag to ignore VM's which has FNMS inventory agent running. Only supply the tag key. The policy assumes that the tag value is irrelevant.
- *Azure AD Tenant ID* - The Azure AD Tenant ID used for the Azure API Authentication.
- *Azure Subscription ID* - The Azure Subscription ID used for the Azure API.
- *FNMS Report URL* - Full FlexNet URL (e.g. <https://demo.flexnetmanager.com/Suite> )
- *FNMS Report ID* - FlexNet manager Custom View ID.

## Policy Actions

- Send an email report

## Prerequisites

- FlexNet Manager.
    __Note:__ If FlexNet Manager Suite is not accessible from the Internet, you will need to setup a wstunnel to provide a secure connection into the FlexNet manager system.
    For more details on wstunnel please refer to this: [https://github.com/rightscale/wstunnel](https://github.com/rightscale/wstunnel)
- This policy requires the Azure Resource Manager Credential, Flexera FNMS Token Credential and Flexera FNMS NTLM Credential. When applying the policy select the appropriate credentials from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.
- The credential must contain the value *Azure RM*, *Flexera FNMS*, *Flexera FNMS NTLM* in the Provider field. Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## Azure Required Permissions

- `Reader`

## Installation

### How to retrieve Azure `AZURE_APPLICATION_ID`, `AZURE_APPLICATION_KEY` and `Azure AD Tenant ID`

1. Follow steps to [Create an Azure Active Directory Application](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#create-an-azure-active-directory-application)
1. Grant the Azure AD Application access to the necessary subscription(s)
1. [Retrieve the Application ID & Authentication Key](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-application-id-and-authentication-key)
1. Create RightScale Credentials with values that match the Application ID (Credential name: `AZURE_APPLICATION_ID`) & Authentication Key (Credential name: `AZURE_APPLICATION_KEY`)
1. [Retrieve your Azure AD Tenant ID](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-tenant-id)

### How to setup FlexNet Manager Custom View for this policy

1. Create a custom view in FlexNet manager that could look like this: ![Alt text][FNMSReport]

Click on Preview and filter.
Select `Microsoft Azure` under `Inventory device` > `Hosted in` ![Alt text][FilterFNMSReport]

Once saved, note the report number in thr URL field : ![Alt text][ReportNumber] you need it when activating the Policy for 'FNMS Report ID'.

1. Setup the API Token in FlexNet Manager System:
    1. On the Account page - Select Create Account -> Service Account and fill in the form ![Alt text][CreateServeceAccount]
    1. IMPORTANT: When you hit save you will see a API Token.. This is the only time you will see it so you need to save it at this point ![Alt text][APIToken]
    1. Add the new account to the Role ___Webservice___ ![Alt text][WebServiceRole]
1. Set Up user for FlexNet manager on-premise:
    1. In your user management add the new user and assign it a password.
    1. On the Account page - Select Create Account -> Service Account ![Alt text][CreateServeceAccount]
    1. in the Account field; select the newly created account and fill in the form.
    1. Add the new account to the Role ___Webservice___ ![Alt text][WebServiceRole]

__NOTE__: You can use a normal interactive user for the API credentials, but it is recommended to add a special service user for the API connection.

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