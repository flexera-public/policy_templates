# ServiceNow Inactive Approvers

## What it does

This policy will identify approver users in ServiceNow that have not approved any requests in the past **n** days.

## Functional Description

This policy integrates with the ServiceNow API to retrieve approval history. Therefore the following are prerequisites for this policy to execute:

- ServiceNow implementation
- ServiceNow user with the appropriate permissions to read approval history (sysapproval_approver table)
- The ServiceNow user credentials must then be stored as RightScale Credentials in the account in which this policy will be applied. The credentials must be named `SERVICENOW_USERNAME` and `SERVICENOW_PASSWORD`.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *ServiceNow Instance Name* - Name of the instance in your ServiceNow url (e.g. "contoso" if your ServiceNow instance is contoso.service-now.com)
- *Number of Days* - Number of days without an approval action executed in ServiceNow
- *Email addresses to notify* - Email addresses of the recipients you wish to notify

## Policy Actions

- Sends an email notification

## Required Permissions

- admin or credential_viewer in CMP
