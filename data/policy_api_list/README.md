# Policy API List

This directory contains auto-generated files listing all API calls made by policy templates in the catalog. **Do not manually modify these files** — they are regenerated automatically.

- [policy_api_list.json](policy_api_list.json) - Complete dataset in JSON format (`{ "api_calls": [...] }`).
- [policy_api_list.csv](policy_api_list.csv) - Complete dataset in CSV format.

Each record contains: `policy_name`, `policy_file`, `policy_version`, `datasource_name`, `api_service`, `method`, `endpoint`, `operation`, `field`, `permission`.

## Generation

- [Generator Script](https://github.com/flexera-public/policy_templates/blob/master/tools/policy_api_list_generation/policy_api_list_generator.py) - Python script that produces these files.
- [GitHub Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-policy-api-list.yaml) - Runs on every push to the default branch and creates a PR if the output changes.
