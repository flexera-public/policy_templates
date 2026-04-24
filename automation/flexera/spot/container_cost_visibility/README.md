# Container Cost Visibility Setup

## What It Does

This policy template automates the setup of the Flexera One and Spot Ocean integration for Container Cost Visibility (CCV). It performs the following steps to enable Kubernetes cost visibility within Flexera Cloud Cost Optimization:

1. Creates a CBI (Common Bill Ingestion) bill connect for Spot Ocean to ingest container cost data into Flexera One.
1. Creates a Container Cost Visibility Dashboard in the Flexera CCO UI for viewing Kubernetes costs by cluster, namespace, and pod.
1. Creates Kubernetes tag dimensions for cost analysis, exposing context such as cluster, namespace, pod, controller, and node from Container Cost Visibility bill data.
1. Optionally hides Container Cost Visibility estimated costs from general CCO reports via a -100% adjustment rule. Flexera Container Cost Visibility estimated **currently** based on public market rates, not actual customer rates — hiding them avoids confusion in chargeback and other reports. The CCV Dashboard still shows these costs using raw (pre-adjustment) values.  "Actual costs" breakdowns for Containers (cost reconciliation with Cloud Bill Data) is committed for general available in 2026.
1. Checks Spot CCO Export status and provides setup instructions if it is not yet configured.
1. Optionally applies the "Kubernetes - Rightsizing Recommendations" published policy template from the Flexera catalog if it is not already applied in the current project.

__NOTE: This *Container Cost Visibility Setup* policy template only needs to execute once to perform the above tasks. It is recommended that the applied policy be terminated after execution completes.__

## How It Works

- The policy creates or updates a CBI bill connect (`cbi-oi-ocean-org-{spot_org_id}`) via the Flexera FinOps Onboarding API. This bill connect is the data pipeline from Spot Ocean to Flexera One, ingesting container cost data in the CBI format.
- The Container Cost Visibility Dashboard is created from the public `policy_templates` repository and created via the Flexera Bill Analysis Dashboards API. The dashboard filters on `bill_source` matching the `cbi-oi-ocean-` prefix and uses the `adjustment_name: Raw Cost` metric to show pre-adjustment container costs.
- Kubernetes Dimensions (e.g. `Kubernetes Namespace`, `Kubernetes Cluster`, `Kubernetes Controller`, `Kubernetes Node`, etc.) are created. These dimensions allow Kubernetes context to appear in cost analysis views alongside standard cloud dimensions.
- When the "Hide CCV Costs" option is enabled, the policy applies a cost adjustment rule with `cost_multiplier: -1` on the CCV `bill_source`. This zeroes out CCV estimated costs from general CCO reports (e.g. chargeback, trending) while preserving them on the dedicated CCV Dashboard.
- The policy checks the Spot CCO Export integration status by querying the Spot API ([`/ccoUsageExporter/flexeraIntegration`](https://spec.dev.spot.io/#tag/Flexera-CCO-Integration)). If the integration is not configured, the incident report includes pre-filled `curl` and PowerShell commands with the correct bill connect ID, Flexera org ID, and zone — requiring only a Flexera refresh token and Spot API token to complete the setup.
- When the "Apply Rightsizing Recommendations" option is enabled, the policy checks the Flexera catalog for the "Kubernetes - Rightsizing Recommendations" published template and lists the project's applied policies. If the template is not already applied, the policy automatically applies it with auto-detected credentials and the template's default schedule.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when the setup is complete.
- *Spot Ocean Organization ID* - The Spot Ocean Organization ID to integrate with Flexera. This is used to create the CBI bill connect and configure the Spot CCO export.
- *Create Dashboard* - Whether to create the Container Cost Visibility Dashboard in the Flexera One CCO UI. The dashboard provides visibility into Kubernetes costs by cluster, namespace, and pod.
- *Create Tag Dimensions* - Whether to create Kubernetes tag dimensions in Flexera One CCO. These dimensions expose Kubernetes context (cluster, namespace, pod, etc.) from CCV bill data for cost analysis.
- *Hide CCV Costs* - Whether to hide Container Cost Visibility estimated costs from general CCO reports via a -100% adjustment rule. CCV costs are estimated based on public market rates, not actual customer rates. Hiding them avoids confusion in chargeback and other reports. The CCV Dashboard still shows these costs.
- *Apply Rightsizing Recommendations* - Whether to apply the "Kubernetes - Rightsizing Recommendations" published policy template if it is not already applied in this project. This template provides container rightsizing recommendations based on CCV data.

## Policy Actions

- Creates or updates a CBI bill connect for Spot Ocean container cost data
- Creates a Container Cost Visibility Dashboard in Flexera One CCO
- Creates Kubernetes tag dimensions for cost analysis
- Applies adjustment rules to hide CCV estimated costs from general CCO reports
- Applies the "Kubernetes - Rightsizing Recommendations" policy template from the Flexera catalog
- Sends an email notification with the setup status and Spot CCO Export instructions

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `csm_bill_upload_admin`
  - `policy_manager`

- [**Spot Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#spot) (*provider=spotinst*) which has the following permission policies:
  - `Account Viewer` on the Spot account(s) to be used.

Additionally, the manual Spot CCO Export step (Step 5) requires:

- A **Flexera refresh token** — see [Generate a Refresh Token](https://docs.flexera.com/flexera-one/flexera-api/working-with-the-flexera-one-api/generating-a-refresh-token) for instructions.
- A **Spot API permanent token** — see [Create an API Token](https://docs.flexera.com/spot/administration/api/create-api-token) for instructions.

For more information on the Spot Ocean integration, see the [Spot Ocean bill connect documentation](https://docs.flexera.com/flexera-one/administration/cloud-settings/bill-data-connections/bill-connect-configurations/spot-ocean/).

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera
- Spot by Flexera

## Cost

This policy template does not incur any cloud costs.
