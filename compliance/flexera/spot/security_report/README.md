# Spot Security - Compliance Report

## What It Does

This policy template retrieves and reports on compliance findings from Spot Security.

## How It Works

- The policy retrieves compliance findings from Spot Security.
- It processes and organizes the findings by severity, cloud provider, and service.
- The policy generates a detailed report with the findings.
- An email notification is sent with the report.

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - Email addresses to notify.
- *Allow/Deny Spot Accounts* - Allow or Deny entered Spot Accounts.
- *Allow/Deny Spot Accounts List* - A list of allowed or denied Spot Accounts.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report with compliance findings.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Spot Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=spotinst*) which has the following permission policies:
  - `Account Viewer` on the Spot account(s) to be used.
  OR
  - `Spot Security Full Access` on the Spot account(s) to be used.
  OR
  - `Organization Admin`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `policy_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Spot Security

## Cost

This policy template does not incur any cloud costs.
