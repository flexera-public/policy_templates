# Email Cost Optimization Recommendations

## What It Does

This policy obtains all of the cost optimization recommendations from the Flexera platform that meet the user-specified criteria and then emails them to a user-specified list of email addresses.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the action in the `Recommendation` field of the incident is taken. Please consult the README of the policy in the `Source Policy` field of the incident for more information on how savings is calculated.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - The email addresses to send recommendations to.
- *Always Email Incident* - Whether or not to always email the incident even if no new items were added to the recommendations since the policy's last execution.
- *Cloud Vendor List* - A list of cloud vendors to email recommendations for.
- *Allow/Deny Cloud Accounts* - Whether to treat `Allow/Deny Cloud Accounts List` parameter as allow or deny list. Has no effect if `Allow/Deny Cloud Accounts List` is left empty.
- *Allow/Deny Cloud Account List* - A list of allowed or denied cloud account IDs/names, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all cloud accounts.
- *Billing Center List* - A list of Billing Center names to email recommendations for. Leave blank to include recommendations for all Billing Centers.
- *Recommendation List* - The types of recommendations to include in the email.
- *Policy List* - A list of catalog policy names to include recommendations for. Leave blank to include recommendations for all policies.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template only makes requests to Flexera APIs and does not incur any cloud costs.
