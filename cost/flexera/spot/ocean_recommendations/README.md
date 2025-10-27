# Kubernetes - Rightsizing Recommendations

## What It Does

This policy template provides rightsizing recommendations for Kubernetes clusters using utilization data collected by Spot Ocean. The recommendations aim to optimize resource usage and reduce costs by suggesting appropriate CPU and memory requests for containers.

## How It Works

- The policy retrieves Kubernetes cluster information and rightsizing suggestions from Spot Ocean.
- It filters the suggestions based on user-defined parameters, such as minimum savings threshold and whether to include recommendations with undefined requests.
- The policy calculates potential savings and generates a detailed report with recommendations.
- An email notification is sent with the report.

## Input Parameters

This policy template has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Include Recommendations with Request Undefined* - Whether to include recommendations where the requested CPU and Memory are not defined.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Allow/Deny Spot Accounts* - Allow or Deny entered Spot Accounts.
- *Allow/Deny Spot Accounts List* - A list of allowed or denied Spot Accounts.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report with rightsizing recommendations.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Spot Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=spotinst*) which has the following permission policies:
  - `Account Viewer` on the Spot account(s) to be used.
  OR
  - `Ocean Full Access` on the Spot account(s) to be used.
  OR
  - `Organization Admin`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `policy_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Kubernetes clusters managed by Spot Ocean

## Cost

This policy template does not incur any cloud costs.
