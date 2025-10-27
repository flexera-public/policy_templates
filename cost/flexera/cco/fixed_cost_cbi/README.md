# Fixed Cost Common Bill Ingestion

## What It Does

This policy template injects a fixed cost with the user-specified metadata into the Flexera Cloud Cost Optimization (CCO) platform. The user specifies the amount to inject as a monthly cost. Optionally, an email is sent indicating that this has happened.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when billing data is uploaded
- *Cost Amount (Monthly)* - The monthly amount of the fixed cost to inject in the currency that the Flexera organization is configured to use.
- *Billing Month* - Month to insert fixed cost into. Select `Specific Month` to specify a month.
- *Specific Month* - Month to insert fixed cost into in YYYY-MM format. Only relevant if `Specific Month` is selected for the Billing Month parameter.
- *CBI (Common Bill Ingestion) Endpoint ID* - The ID of CBI endpoint to create/use when injecting the fixed cost. Leave blank to have this generated and managed automatically. Ex: cbi-oi-optima-laborcosts
- *Amortization* - Whether or not to amortize the fixed cost across the month. If the "Amortize" option is selected, the fixed cost will be divided by the number of days in the month and then each day will receive that cost. Otherwise, a simple fixed cost for the total amount will be applied for the 1st of the month.
- *Cloud Vendor* - The value the fixed cost should have for the `Cloud Vendor` dimension in Flexera CBI. Only has an effect when the CBI endpoint is first created. This is because the `Cloud Vendor` dimension isn't based on billing data but is configured for the CBI endpoint itself.
- *Cloud Vendor Account* - The value the fixed cost should have for the `Cloud Vendor Account` dimension in Flexera CBI. Leave blank to have no value for this dimension.
- *Cloud Vendor Account Name* - The value the fixed cost should have for the `Cloud Vendor Account Name` dimension in Flexera CBI. Leave blank to have no value for this dimension.
- *Category* - The value the fixed cost should have for the `Category` dimension in Flexera CBI. Leave blank to have no value for this dimension.
- *Service* - The value the fixed cost should have for the `Service` dimension in Flexera CBI. Leave blank to have no value for this dimension.
- *Region* - The value the fixed cost should have for the `Region` dimension in Flexera CBI. Leave blank to have no value for this dimension.
- *Resource Type* - The value the fixed cost should have for the `Resource Type` dimension in Flexera CBI. Leave blank to have no value for this dimension.
- *Instance Type* - The value the fixed cost should have for the `Instance Type` dimension in Flexera CBI. Leave blank to have no value for this dimension.
- *Line Item Type* - The value the fixed cost should have for the `Line Item Type` dimension in Flexera CBI. `Usage` is recommended for most cases.
- *Tags* - Tag values to attach to the line items in the Flexera platform in Key=Value format. Leave blank to not include any tag values.

## Policy Actions

- Uploads fixed cost billing data to Flexera CCO
- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `csm_bill_upload_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All

## Cost

This Policy Template does not incur any cloud costs
