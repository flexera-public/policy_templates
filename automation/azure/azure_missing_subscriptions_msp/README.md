# MSP Report: Azure Missing Subscriptions

## What It Does

This policy template gathers all of the "Azure Missing Subscriptions" incident data from the various child organizations of an MSP organization and provides a consolidated report. This policy template assumes that all of the child organizations have the [Azure Missing Subscriptions](https://github.com/flexera-public/policy_templates/tree/master/automation/azure/azure_missing_subscriptions/azure_missing_subscriptions.pt) policy template running and working as intended.

## How To Use

1. Upload and apply the [Azure Missing Subscriptions](https://github.com/flexera-public/policy_templates/tree/master/automation/azure/azure_missing_subscriptions/azure_missing_subscriptions.pt) policy template to your child organizations with the parameters set to their default values. It is recommended that you make this part of your normal onboarding automation.
2. Upload and apply the [MSP Report: Azure Missing Subscriptions](https://github.com/flexera-public/policy_templates/tree/master/automation/azure/azure_missing_subscriptions_msp/azure_missing_subscriptions_msp.pt) policy template in the parent organization. It will scrape the incidents produced by the above and raise an incident (and, optionally, email this incident) with a consolidated report.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `iam_admin`
  - `billing_center_viewer`
  - `policy_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### MSP Requirements

The Flexera Credential listed above must be for a Flexera user that has the listed roles for all child organizations. Your MSP automation should ensure such a user exists and is added with the appropriate roles to every child organization you wish to monitor.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
