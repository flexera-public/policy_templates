# Cost Reallocation - Google Cloud Logging

## What It Does

This policy template reallocates Google Cloud Logging costs from centralized logging project(s) to the projects where the logs originated from. Costs are allocated to each project based on their actual Cloud Logging usage (bytes ingested) during the billing period.

To reallocate the costs, the policy template uses Flexera's "Common Bill Ingest" (CBI) capability to negate the original cost allocated to the centralized logging project(s) with negative cost line items, and write the reallocated portions as new line items.

For example, if you are paying $10,000 per month for Cloud Logging in your centralized logging project (example ID `gcp-logging-nonprod`), those costs are being charged to that project. This policy template would push new line items in - first a negative cost line item for -$10,000 allocated to `gcp-logging-nonprod`, and then N number of line items that sum up to positive +$10,000 distributed across all projects based on their logging usage.

### Example Scenario

#### Before Reallocation

Let's assume you have a centralized logging setup with:

- **Central Logging Project** (ID: `gcp-logging-nonprod`)
- **Project A** (ID: `project-a-123`)
- **Project B** (ID: `project-b-456`)
- **Project C** (ID: `project-c-789`)

In the current billing setup, the entire Cloud Logging cost of $10,000 is allocated to the Central Logging Project (`gcp-logging-nonprod`).

#### After Reallocation

After applying this policy, the Cloud Logging costs are reallocated based on each project's actual logging usage:

- **Project A** ingested 50% of the total logs (500GB)
- **Project B** ingested 30% of the total logs (300GB)
- **Project C** ingested 20% of the total logs (200GB)

The reallocated costs would be:

- **Central Logging Project**: -$10,000 (negative cost line item)
- **Project A**: +$5,000 (50% of $10,000)
- **Project B**: +$3,000 (30% of $10,000)
- **Project C**: +$2,000 (20% of $10,000)

### Positive Business Outcomes

- **Accurate Cost Allocation**: Ensures that each project is charged accurately based on their actual Cloud Logging usage, promoting accountability and cost transparency.
- **Simplified Billing**: Reduces the complexity of internal chargeback and financial reporting by automating the reallocation process.
- **Cost Optimization**: Encourages projects to optimize their logging configuration and reduce unnecessary logs, as they are directly accountable for their share of the logging costs.

## Input Parameters

- *Bill Connect ID* - Bill Connect ID to use for reallocating costs. Usually does not need to be changed, will be created if not exists.

- *Centralized Logging Projects* - List of centralized logging projects to reallocate costs from. Costs will be reallocated to the project where the logs were sourced from. At least 1 project is required. Can be specified using Project Name or Project ID.

- *Billing Period* - Billing Period this applied policy will update. Allowed values: *"Previous Month"*, *"Current Month"*, *"Specific Month"*. If *"Specific Month"* is selected, use the *"Billing Period - Specific Month"* parameter to specify the month in \"YYYY-MM\" format.

- *Billing Period - Specific Month* - If *"Specific Month"* is selected for Billing Period, use this parameter to specify the month in `YYYY-MM` format. Example: 2024-01. This is intended to be used for backfilling/reprocessing reallocation for previous months.

- *Reallocated Cost Granularity* - Reallocated Cost Granularity configures the granularity for the new line items. Typically "Day" is preferred. For some extremely large environments, you may need to change this to 'Month' to prevent Policy Engine timeouts.

## Policy Actions

- Creates Common Bill Ingest Bill Connect if not exists.
- Uploads reallocated cost line items to the Common Bill Ingest Bill Connect.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `org_owner`*

  \* The `org_owner` role is only required if the Bill Connect does not already exist. If the Bill Connect already exists, the `org_owner` role is not required.

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `cloudresourcemanager.projects.get`
  - `cloudresourcemanager.projects.list`
  - `compute.regions.list`
  - `monitoring.timeSeries.list`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google Cloud

## Cost

This Policy Template does not incur any cloud costs.
