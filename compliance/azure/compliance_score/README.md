# Azure Regulatory Compliance

## What it does

This Policy Template will provide an overview for the various Regulatory Compliance controls and compliance scores. The policy will generate an email notification.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Pre-requisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Supported Clouds

- Azure

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
