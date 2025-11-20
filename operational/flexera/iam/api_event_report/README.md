# Flexera One API Event Report

## What It Does

This policy template reports Flexera API events going back the user-specified number of days. API requests can be filtered by URL. Optionally, this report can be emailed.

__NOTE: Only API requests made using the modern [Flexera One API](https://developer.flexera.com/) will be included in this report. As more Flexera APIs are moved into the Flexera One API by the Flexera engineering team, more request types will appear in the report.__

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Days Back* - How many days of API events to include in the report. All events from this many days back until today will be reported.
- *Allow/Deny URL Filters* - Allow or Deny requests whose URLs contain the listed strings. Only applicable if `Allow/Deny URL Filter List` isn't empty.
- *Allow/Deny URL Filter List* - A list of strings to allow or deny when filtering API requests by URL. For example, if */bill-connects* is specified here, any API calls with */bill-connects* in the URL will be filtered. This is useful for reporting on specific API endpoints instead of reporting on all API calls. Leave empty to not filter requests by URL.
- *Allow/Deny Email Filters* - Allow or Deny requests made by users with the specified email addresses. Only applicable if `Allow/Deny Email Filter List` isn't empty. Note that, if this is set to 'Allow' and email addresses are specified in the `Allow/Deny Email Filter List` parameter, requests without an associated user, such as requests made without proper authentication, will not be included in the results.
- *Allow/Deny Email Filter List* - A list of user email addresses to allow or deny when filtering API requests. Leave empty to not filter requests by user email address.
- *Response Filter* - Whether to include API calls that received a good (Code 2XX/3XX) response, a bad (Code 4XX/5XX) response, or both.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `iam_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.
