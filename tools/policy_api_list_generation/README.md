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
- `api_service` - Which service the API targets (AWS, Azure, Flexera, GCP, etc.)
- `method` - HTTP method (GET, POST, PUT, DELETE, PATCH)
- `endpoint` - Full API endpoint URL with variable placeholders
- `field` - Field extracted from the API response (if any)

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

There is an automated workflow that runs every time a push to the default branch is made. Whenever there are changes resulting from running the script, a new PR is created and can be approved by the Policy Template Maintainers.

[![Generate Policy API List](https://github.com/flexera-public/policy_templates/actions/workflows/generate-policy-api-list.yaml/badge.svg?event=push)](https://github.com/flexera-public/policy_templates/actions/workflows/generate-policy-api-list.yaml)

Workflow defined in file [.github/workflows/generate-policy-api-list.yaml](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-policy-api-list.yaml)

## Requirements

- Python 3.x
- No additional dependencies required (uses Python standard library)

## Technical Details

The script:

1. Parses policy template datasources with `request` blocks
2. Extracts host, path, query parameters, and body parameters
3. Handles JavaScript request scripts for dynamic endpoint construction
4. Resolves parameter references and variable patterns
5. Identifies API services based on hostname patterns
6. Formats endpoints with standardized variable placeholders
7. Deduplicates and organizes output by policy

The parser handles complex patterns including:

- Multiple nested datasources
- JavaScript-based request construction
- Dynamic host resolution (e.g., `val($ds_flexera_api_hosts, "flexera")`)
- Parameter references and variable substitution
- Array and object access patterns in scripts
