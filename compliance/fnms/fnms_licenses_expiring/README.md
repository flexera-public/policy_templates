# ITAM Expiring Licenses

## What it does

This policy uses the ITAM API to look up Active IT Asset Manager Licenses Expiring within set Time Period and sends the result as an email.

The report / Mail output looks like this:
ITAM Expiring Licenses

licenseId publisher licenseName version edition licenseStatus licenseDuration licenseType expiryDate
12345 Adobe Acrobat Pro 2022 Professional [Active]  [Subscription]  [Named User]  2022-03-31T00:00:00Z
54321 Microsoft Visio Pro 2019 Professional [Active] [Subscription]  [Named User] 2021-08-31T00:00:00Z

Current limitations:

- Output is limited to max 100000 rows.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Time Period of Expiration* - Time Period, in days, to find licenses expiring within
- *Email addresses of the recipients you wish to notify* - A list of email address(es) to notify

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

## Cost

This Policy Template does not incur any additional cloud costs.
