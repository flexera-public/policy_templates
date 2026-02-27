# Policy API List Generator

A script that extracts and catalogs all REST API calls made by Policy Templates across the repository. This generates a comprehensive dataset of API endpoints, methods, and services used by each policy.

## Overview

The Policy API List Generator parses all Policy Template (`.pt`) files and extracts:

- API endpoints and their methods (GET, POST, etc.)
- Which service each API call targets (AWS, Azure, GCP, Flexera, etc.)
- Fields extracted from API responses
- Policy metadata (name, version, file path)

The output provides visibility into all external API dependencies across the entire policy catalog.

## Usage

Run the script from the `tools/policy_api_list_generation` directory:

```sh
cd tools/policy_api_list_generation
python3 policy_api_list_generator.py
```

Or from the repository root:

```sh
python3 tools/policy_api_list_generation/policy_api_list_generator.py
```

The script will:

1. Read the active policy list from `data/active_policy_list/active_policy_list.json`
2. Parse each policy template to extract API calls
3. Generate output files in `data/policy_api_list/`:
   - `policy_api_list.json` - Complete dataset in JSON format
   - `policy_api_list.csv` - Complete dataset in CSV format

## Output Format

### Fields

Each API call record contains the following fields:

- `policy_name` - Name of the policy template
- `policy_file` - Path to the policy template file
- `policy_version` - Version of the policy template
- `datasource_name` - Name of the datasource making the request (e.g., `ds_org_accounts`)
- `api_service` - Which service the API targets (AWS, Azure, Flexera, GCP, etc.)
- `method` - HTTP method (GET, POST, PUT, DELETE, PATCH)
- `endpoint` - Full API endpoint URL with variable placeholders
- `operation` - Human-readable operation name extracted from the endpoint and method
- `field` - Field extracted from the API response (if any)

### Operation Field

The `operation` field provides a human-readable description of what operation is being performed. It is extracted from:

**AWS**: X-Amz-Target header or URL path

- `ListAccounts` - from `X-Amz-Target: AWSOrganizationsV20161128.ListAccounts`
- `ListPolicies` - from `X-Amz-Target: AWSOrganizationsV20161128.ListPolicies`

**Azure**: Resource type from URL path + HTTP method

- `List Virtual Network Gateways` - from GET `/providers/Microsoft.Network/virtualNetworkGateways`
- `List Virtual Machines` - from GET `/providers/Microsoft.Compute/virtualMachines`
- `List Subscriptions` - from GET `/subscriptions`

**Flexera**: Resource from URL path + HTTP method

- `List Applied Policies` - from GET `/policy/v1/.../applied-policies`
- `Get Billing Centers` - from GET `/analytics/.../billing_centers`

**GCP**: Operation from URL path (often uses `:operation` pattern)

- `Search` - from `/v3/projects:search`
- `List Projects` - from GET `/v3/projects`

**Other services**: Resource name extracted from URL path combined with HTTP method

The operation name uses proper capitalization and handles camelCase, snake_case, and kebab-case resource names.

### Endpoint Format

Endpoints use curly braces `{}` to denote variables and placeholders:

- Policy language constructs: `{rs_optima_host}`, `{rs_governance_host}`, `{flexera_api_host}`
- Path variables: `{org}`, `{project}`, `{subscription}`, `{id}`
- Dynamic segments: `{dynamic}`

**Example endpoints:**

```text
https://{rs_optima_host}/analytics/orgs/{org}/billing_centers
https://{flexera_api_host}/policy/v1/orgs/{org}/projects/{project}/applied-policies
https://management.azure.com/subscriptions/{subscription}/providers/Microsoft.Compute/...
https://ec2.us-east-1.amazonaws.com/
```

## Supported Services

The script automatically detects and categorizes API calls to:

- **Flexera** - Flexera platform APIs (Optima, Governance, Policy, FlexNet Manager)
- **AWS** - Amazon Web Services APIs
- **Azure** - Microsoft Azure APIs (including Storage)
- **GCP** - Google Cloud Platform APIs
- **GitHub** - GitHub APIs and raw content
- **Oracle** - Oracle Cloud Infrastructure APIs
- **Turbonomic** - Turbonomic (IBM) APIs
- **Microsoft Graph** - Microsoft Graph API
- **ServiceNow** - ServiceNow APIs
- **Okta** - Okta identity APIs
- **Spot by NetApp** - Spot optimization APIs
- **Unknown** - Dynamic or placeholder endpoints

## Automated Workflow

There is an [automated workflow](https://github.com/flexera-public/policy_templates/actions/workflows/generate-policy-api-list.yaml) that runs every time a push to the default branch is made. Whenever there are changes resulting from running the script, a new PR is created and can be approved by the Policy Template Maintainers.

## Requirements

- Python 3.x
- No additional dependencies required (uses Python standard library)

## Technical Details

The script:

1. Parses policy template datasources with `request` blocks
1. Extracts host, path, query parameters, and body parameters
1. Handles JavaScript request scripts for dynamic endpoint construction
1. Resolves parameter references and variable patterns
1. Identifies API services based on hostname patterns
1. Formats endpoints with standardized variable placeholders
1. Deduplicates and organizes output by policy

The parser handles complex patterns including:

- Multiple nested datasources
- JavaScript-based request construction
- Dynamic host resolution (e.g., `val($ds_flexera_api_hosts, "flexera")`)
- Parameter references and variable substitution
- Array and object access patterns in scripts
