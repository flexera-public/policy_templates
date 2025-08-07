# Generic Meta Parent Policy

## What It Does

This generic meta parent policy template dynamically creates and manages child policies based on cost dimensions from the Flexera Bill Analysis API. Unlike traditional meta parent policies that are pre-compiled for specific child policy templates, this policy uses parameters to determine:

1. **Which policy template** to deploy as children
1. **How to map cost dimensions** to child policy parameters
1. **Which cost dimensions** to use for grouping child policies

The policy automatically creates, updates, and deletes child policies as cost dimension values change over time, providing a flexible solution for managing policies across multiple accounts, subscriptions, regions, or other dimensions.

**Important Note:** **Manual Cleanup of Child Policies is required**: Child policies require manual cleanup, and they will not cleanup themselves when the Meta Parent is terminated like the compiled Meta Parent Policy Templates do.

## How It Works

1. **Query Cost Data:** The policy queries the Flexera Bill Analysis API using the specified dimension mappings and filters
1. **Generate Combinations:** Creates unique combinations of dimension values based on the mappings provided
1. **Compare with Existing:** Compares required child policies with existing child policies managed by this meta parent
1. **Take Actions:** Automatically creates new child policies, and optionally deletes obsolete ones

## Input Parameters

### Policy Settings

- **Email Addresses** - Email addresses to notify when incidents are created
- **Child Policy Template Name** - Exact name of the policy template to deploy as children
- **Child Policy Template Source** - Whether to use Published Catalog Template or Uploaded Template

### Child Policy Settings

- **Cost Dimension to Parameter Mappings** - List of mappings from cost dimensions to child policy parameters (see *Cost Dimension to Parameter Mappings* section below)
- **Child Policy Schedule** - Frequency for child policy execution (daily, weekly, monthly)
- **Default Child Policy Options (JSON)** - Default options applied to all child policies

### Filters

- **Dimension Include Filters** - Filters to determine which dimension values to include
- **Dimension Exclude Filters** - Filters to determine which dimension values to exclude

### Cost Data Settings

- **Cost Data Lookback Period (Days)** - Number of days to look back when querying cost data

## Cost Dimension to Parameter Mappings

The core functionality uses mappings in the format: `"dimension_name::parameter_name"`

### Single Dimension Examples

- `vendor_account::param_aws_account_number` - Creates one child policy per AWS account
- `vendor_account::param_subscription_id` - Creates one child policy per Azure subscription
- `billing_center_id::param_billing_center_id` - Creates one child policy per billing center
- `region::param_region_list` - Creates one child policy per region

### Multiple Dimension Examples

When multiple mappings are provided, child policies are created for each unique combination:

- `["vendor_account::param_aws_account_number", "region::param_region_list"]` - Creates separate child policies for each AWS account + region combination
- `["billing_center_id::param_billing_center_id", "service::param_service_list"]` - Creates child policies for each billing center + service combination

### Available Dimensions

Any Flexera cost dimensions can be used including the Default Dimensions, and Custom Dimensions (RBD, Tag)

See the [Bill Analysis API Documentation](https://reference.rightscale.com/bill_analysis/) for the complete list.

## Default Child Policy Options

The **Default Child Policy Options** parameter accepts a JSON object with default parameter values for all child policies.

**Parameters specified in the dimension mappings will override these defaults.**

### Example

```json
{
  "param_email": ["admin@company.com"],
  "param_automatic_action": [],
  "param_log_to_cm_audit_entries": "No",
  "param_min_savings": 100
}
```

## Filter Examples

### Include Filters

- `vendor=AWS` - Only include AWS accounts
- `region=us-east-1` - Only include us-east-1 region
- `billing_center_name=~Production` - Only include billing centers containing "Production"

### Exclude Filters

- `vendor_account=123456789012` - Exclude specific AWS account
- `region=~test` - Exclude regions containing "test"
- `billing_center_name=Development` - Exclude Development billing center

## Policy Actions

The policy provides the following escalations:

- **Send Email** - Automatically sends email notifications about child policy changes
- **Create Child Policies** - Automatically creates new child policies for new dimension combinations
- **Delete Obsolete Child Policies** - Manual approval to delete child policies no longer needed

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All (This is a cloud-agnostic meta policy that can manage child policies for any cloud provider)

## Cost

This policy template does not incur any cloud costs. It only manages other policy templates within Flexera.

## Use Case Examples

### AWS Account-Based Policies

Deploy AWS EC2 Rightsizing policies across all AWS accounts:

```
Child Policy Template Name: AWS Rightsize EC2 Instances
Dimension Mappings: ["vendor_account::param_aws_account_number"]
Include Filters: ["vendor=AWS"]
```

### Azure Subscription

Deploy Azure VM policies across subscriptions and to a specific specific region:

```
Child Policy Template Name: Azure Rightsize Compute Instances
Dimension Mappings: ["vendor_account::param_subscription_id", "region::param_region_list"]
Include Filters: ["vendor=Azure", "region=East US"]
```

### Scheduled Reports delivered to each Cost Center Approver

Create a Scheduled Report for each Cost Center configured to deliver to each Cost Center Approver

```
Child Policy Template Name
Exclude Filter: ["rbd_cost_center=None","rbd_cost_center_approver=None"]'
Dimension Mappings: ["rbd_cost_center_approver::param_email::split","rbd_cost_center::param_dimension_filter::prefix:Cost Center="]
