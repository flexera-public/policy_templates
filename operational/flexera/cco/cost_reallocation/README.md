# Cost Reallocation

## What It Does

This policy template provides a flexible way to reallocate costs from one scope (Origin) to another scope (Destination) using various reallocation strategies.

## How it Works

The policy template uses Flexera's "Common Bill Ingest" (CBI) capability to negate the original costs with negative cost line items and write the reallocated portions as new line items.

For example, you can use this template to:

- Reallocate centralized costs like AWS Support to individual AWS accounts based on their total spend
- Redistribute shared service costs (like CloudTrail, Security Hub, etc.) to the accounts consuming them
- Reallocate costs from one resource group to others based on custom allocation rules

### Example Scenarios

#### Tag Based Reallocation

To reallocate costs from a shared services resources to application resources using tags:

```json
{
  // Any costs from resources tagged with tag_shared_service_logging=provider will be reallocated
  "Origin Filter": {
    "dimension": "tag_shared_service_logging",
    "type": "equal",
    "value": "provider"
  },
  // The costs will be reallocated to resources tagged with tag_shared_service_logging=consumer
  "param_destination_filter": {
    "dimension": "tag_shared_service_logging",
    "type": "equal",
    "value": "consumer"
  },
  // The costs will be split across all vendor_accounts and resource groups in the destination filter based on the RG's % of total spend
  "Destination Group": ["vendor_account","resource_group"],
  "Destination Method": "Percent of Total Spend"
}
```

#### AWS Support Cost Reallocation

To reallocate AWS Support costs from the master payer account (`999888777666`) to all other AWS Accounts under the organization:

```json
{
  // Any AWS Support costs from the master payer account 999888777666 will be reallocated
  "param_origin_filter": {
    "type": "and",
    "expressions": [
      {
        "dimension": "vendor_account",
        "type": "equal",
        "value": "999888777666"
      },
      {
        "dimension": "service",
        "type": "equal",
        "value": "AWSSupportEnterprise"
      }
    ]
  },
  // The AWS Support costs will be reallocated to all AWS accounts under the master payer account (999888777666) except the master payer account itself
  "param_destination_filter": {
    "type": "and",
    "expressions": [
      {
        "type": "not",
        "expressions": [
          {
            "dimension": "vendor_account",
            "type": "equal",
            "value": "999888777666"
          }
        ]
      },
      {
        "dimension": "bill_source",
        "type": "equal",
        "value": "aws-999888777666"
      }
    ]
  },
  // Each AWS account will be reallocated a % of the AWS Support costs based on the account's % total spend
  "param_destination_group": ["vendor_account"],
  "param_destination_method": "Percent of Total Spend"
}
```

#### CloudTrail Cost Distribution

To distribute CloudTrail costs from all AWS Organization accounts to an account owned by the security and IT Team (`004567890123`) who mandates that all accounts must have CloudTrail enabled:

```json
{
  // All CloudTrail costs from all AWS accounts (except the 004567890123 account) will be reallocated
  "param_origin_filter": {
    "type": "and",
    "expressions": [
      {
        "type": "not",
        "expressions": [
          {
            "dimension": "vendor_account",
            "type": "equal",
            "value": "004567890123"
          }
        ]
      },
      {
        "dimension": "service",
        "type": "equal",
        "value": "CloudTrail"
      }
    ]
  },
  // The CloudTrail costs will be reallocated to the 004567890123 account
  // In this example this potentially is an account owned by IT or Security persona who has mandated CloudTrail to be enabled on all accounts
  "param_destination_filter": {
    "dimension": "vendor_account",
    "type": "equal",
    "value": "004567890123"
  },
  // There is only one destination AWS account in this example and no Resource Groups on AWS, so these params won't have any effect
  "param_destination_group": ["vendor_account"],
  "param_destination_method": "Percent of Total Spend"
}
```

## Input Parameters

- *Bill Connect ID* - Bill Connect ID to use for reallocating costs. Should be changed to identify the use-case for the reallocation.  Example: `cbi-oi-optima-costreallocation-centralizedlogging`

  This policy requires a Bill Connect ID. By default it will use `cbi-oi-optima-costreallocation-default` but you should specify a custom ID. The Bill Connect will be created if it does not already exist.

- *Origin Filter* - JSON filter to scope the origin costs that will be reallocated. The filter should be structured as:

    ```json
    {
      "dimension": "<dimension_name>",
      "type": "equal",
      "value": "<dimension_value>"
    }
    ```

- *Destination Filter* - Optional JSON filter to scope which destinations can receive reallocated costs. Uses the same format as Origin Filter. Leave empty to allow all destinations.

- *Destination Group* - How to group the destination costs for reallocation. Supports:
  - `vendor_account` - Group by cloud vendor account
  - `resource_group` - Group by resource group

- *Destination Method* - How to reallocate the costs to destinations:
  - `Percent of Total Spend` - Allocate based on each destination's percentage of total spend
  - `Equal Portions` - Split costs equally across all destinations

- *Billing Period* - Billing Period this applied policy will update. Allowed values:
  - `Previous Month`
  - `Current Month`
  - `Specific Month` (requires Billing Period - Specific Month parameter)

- *Billing Period - Specific Month* - If "Specific Month" is selected for Billing Period, specify the month in `YYYY-MM` format (e.g. 2024-01)

- *Reallocated Cost Granularity* - Granularity for the new line items:
  - `Day` - Daily line items (preferred)
  - `Month` - Monthly line items (use for very large environments to prevent timeouts)

    When using "Day" granularity (default and preferred):
    - Costs are allocated per day, providing more detailed cost distribution
    - May take longer to process in very large environments

    When using "Month" granularity:
    - Costs are summarized monthly into fewer line items
    - Recommended only for very large environments to prevent timeouts
    - Trade-off between processing speed and granularity of cost allocation

## Policy Actions

- Creates Common Bill Ingest Bill Connect if not exists
- Uploads reallocated cost line items to the Common Bill Ingest Bill Connect

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer` - Required for accessing cost data
  - `org_owner` - Required only if the Bill Connect needs to be created. Not required if the Bill Connect already exists.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS
- Azure
- Google Cloud
- Any cloud provider supported by Flexera

## Cost

This Policy Template does not incur any cloud costs.
