# Percentage Cost Common Bill Ingestion

## What It Does

This policy template injects a percentage of all spend as a cost into the Flexera Cloud Cost Optimization (CCO) platform. The user specifies the percentage of monthly spend to inject. Optionally, an email is sent indicating that this has happened.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when billing data is uploaded
- *Percentage* - The percentage of spend to insert as a cost into the Flexera CCO platform. Ex: 5.5.
- *Billing Month* - Month to insert fixed cost into. Select `Specific Month` to specify a month.
- *Specific Month* - Month to insert fixed cost into in YYYY-MM format. Only relevant if `Specific Month` is selected for the Billing Month parameter.
- *CBI (Common Bill Ingestion) Endpoint ID* - The ID of CBI endpoint to create/use when injecting the fixed cost. Leave blank to have this generated and managed automatically. Ex: cbi-oi-optima-laborcosts
- *Monthly Spend Filters* - Filters to apply to the monthly spend when calculating the percentage in Dimension=Value format. Only monthly spend that matches all filters will be used in the calculation. Leave blank to use all monthly send. Ex: Cloud Vendor=AWS
- *Monthly Spend Amortization* - Whether to use amortized or unamortized cloud spend when calculating the percentage.
- *Injected Cost Amortization* - Whether or not to amortize the percentage cost across the month. If the "Amortize" option is selected, the cost will be divided by the number of days in the month and then each day will receive that cost. Otherwise, a single cost for the total amount will be applied for the 1st of the month.
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

- Uploads percentage cost billing data to Flexera CCO
- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `csm_bill_upload_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All

## Cost

This Policy Template does not incur any cloud costs
