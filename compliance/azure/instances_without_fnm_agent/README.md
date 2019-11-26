# Azure Instances not running FlexNet Inventory Agent

## What it does

This policy checks all instances running in Azure to determine if the FlexNet Inventory Agent is running on the instance and reports on any that are missing the agent.
The policy is a recommendation only policy, no action is taken during the Policy Escalation.

## Functional Details

The policy leverages the cloud API to get all current instances and the FlexNet Manager report (Custom view) API to get all azure cloud instances with agent. It cross-checks the two lists to determine if any instances are running on the cloud that aren't known to FNM.  The policy matches the ComputerName from FNMS and the VirtualMachine.name from Azure.

## Prerequisites

- FlexNet Manager
- The following RightScale Credentials
  - 'FNMS_API_Token'
- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to manage resources in the target subscription
- The following RightScale Credentials
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`

## Installation

### How to retrieve Azure `AZURE_APPLICATION_ID`, `AZURE_APPLICATION_KEY` and `Azure AD Tenant ID`:

1. Follow steps to [Create an Azure Active Directory Application](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#create-an-azure-active-directory-application)
1. Grant the Azure AD Application access to the necessary subscription(s)
1. [Retrieve the Application ID & Authentication Key](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-application-id-and-authentication-key)
1. Create RightScale Credentials with values that match the Application ID (Credential name: `AZURE_APPLICATION_ID`) & Authentication Key (Credential name: `AZURE_APPLICATION_KEY`)
1. [Retrieve your Azure AD Tenant ID](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-tenant-id)

#### How to setup FlexNet Manager Custom View for this policy:

1. Create a custom view in FlexNet manager that could look like this:
![Alt text][FNMSReport]

Click on Preview and filter.
Select `Microsoft Azure` under `Inventory device` > `Hosted in`

![Alt text][FilterFNMSReport]

Once saved, note the report number in thr URL field :
![Alt text][ReportNumber] you need it when activating the Policy for 'FNMS Report ID'.

1. Setup the API Token in FNMS:
    1. On the Account page - Select Create Account -> Service Account and fill in the form

        ![Alt text][CreateServeceAccount]
    1. IMPORTANT: When you hit save you will see a API Token.. This is the only time you will see it so you need to save it at this point

        ![Alt text][APIToken]
    1. Add the new account to the Role ___Webservice___

        ![Alt text][WebServiceRole]

#### Cloud manager

1. Create RightScale Credentials with values that match the FlexNet Manager API Token (Credential name: `FNMS_API_Token`)

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Exclusion Tag Key* - Azure-native Virtual machines tag to ignore VM's which has FNMS inventory agent running. Only supply the tag key. The policy assumes that the tag value is irrelevant.
- *Azure AD Tenant ID* - The Azure AD Tenant ID used for the Azure API Authentication.
- *Azure Subscription ID* - The Azure Subscription ID used for the Azure API.
- *FNMS Report ID* - FlexNet manager Custom View ID.

## Required RightScale Roles

- `policy_manager`
- `credential_viewer`

### Azure Required Permissions

- `Reader`

## Supported Clouds

- Azure

## Policy Actions

- Send an email report

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
