# Dynamic Dashboards

## What It Does

This policy template creates dynamic dashboards based on cost data aggregated by user-specified dimensions over the previous 12 months. For each unique value of the selected dashboard dimension, the policy creates a dashboard showcasing the top N widget dimension values by cost. This enables automatic creation of focused cost dashboards for different organizational segments (vendors, regions, services, etc.).

## How It Works

- The policy retrieves cost data for the previous 12 months from Flexera's Cost API
- Costs are aggregated by the user-specified dashboard dimension (e.g., Cloud Vendor, Region, Service)
- For each unique dashboard dimension value, the policy identifies the top N widget dimension values by cost
- A comprehensive dashboard is created for each dashboard dimension value, featuring interactive visualizations of cost data
- Created dashboards are public and accessible at Dashboards -> Cloud in Flexera One
- Dashboards use the modern Flexera dashboard format with interactive filters and multiple visualization components

## Input Parameters

- *Cost Metric* - Select the cost metric for your report. Options: Amortized, Unamortized.
- *Dashboard Prefix* - Prefix to use for dynamic dashboard names. Will have a space appended to end if not included.
- *Dashboard Dimension* - The dimension to aggregate costs by for dashboard creation.
- *Filter Dashboard Dimension Value List* - List of values to create a dashboard for the selected filter dimension. Leave blank to include all values.
- *Allow/Deny Filter Dashboard Dimension Value List* - Allow or Deny entered Filter Dashboard Dimension Value List.
- *Widget Dimension* - The dimension to aggregate costs by for widget creation.
- *Widget Count* - Number of top widgets to display in each dashboard (1-20).
- *Filter Widget Dimension Value List* - List of values to create a widget for the selected filter dimension. Leave blank to include all values.
- *Allow/Deny Filter Widget Dimension Value List* - Allow or Deny entered Filter Widget Dimension Value List.
- *Allow/Deny Include Marketplace Charges* - Allow or Deny inclusion of marketplace charges in the widget.

## Policy Actions

- Creates/updates dynamic dashboards based on cost dimension analysis
- Deletes dynamic dashboards

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `csm_dashboard_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.
