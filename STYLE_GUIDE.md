# Flexera Policy Template Catalog Style Guide

Policy templates that go into the catalog should follow the conventions outlined here. These conventions ensure that policy code is organized and readable, and ensures that policy templates in the catalog are usable by non-technical users and presented in a professional way.

The Dangerfile that runs whenever a pull request is made against the _master_ branch will test for many of these guidelines and report warnings/errors as appropriate. Please correct any warnings/errors that are not false positives before asking for peer review.

Note that this is not intended as a guide for general best practices for policy development. It only covers style and conventions specific to the public catalog. For general training on how to develop policy templates, please take a look at the [Policy Development Training](https://github.com/flexera-public/policy_engine_training) repository.

## General Style Guidelines

- Policy templates for the catalog are visible to users in the Flexera platform. For that reason, grammar and spelling should be on point, and slang, abbreviations (when not widely-used acronyms), etc. should be avoided, particularly for parts of the policy template that appear in the UI, such as names and descriptions of parameters and anything raised in an incident table.

- README files, CHANGELOG files, and anything user-visible in the policy template itself should be written with a non-technical user in mind. Explain things in clear English and avoid using programming or IT jargon where possible. The CHANGELOG should describe changes in terms of the difference the end user will see, not in terms of the changes made to the policy template code.

- Refer to policy templates as "policy templates" and not as "policies", and refer to applied policy templates as "applied policies". This is to keep terminology in line with our documentation and avoid confusion.

- Avoid references to RightScale, Optima, or other terms that were in use prior to RightScale's acquisition. Refer to "Flexera" and "Cloud Cost Optimization" instead.

## File Names & Directory Structure

The following directory structure should be used for provider-specific policy templates. [Snake case](https://en.wikipedia.org/wiki/Snake_case) should be used.

- /{category}/{provider}/{policy template name}/
  - _Example_: `/cost/aws/old_snapshots/`

The following directory structure should be used for general Flexera policy templates. [Snake case](https://en.wikipedia.org/wiki/Snake_case) should be used.

- /{category}/flexera/{product}/{policy template name}/
  - _Example_: `/cost/flexera/cco/focus_report/`

Every policy template should be in its own directory that contains the following files:

- The policy template itself. File name should be in [snake case](https://en.wikipedia.org/wiki/Snake_case) and be similar to the name of the policy template itself. In most cases, the file name should start with the cloud provider or service the policy template is for.
  - _Example_: aws_rightsize_ec2_instances.pt

- (If applicable) The meta parent for the policy template. This should be generated automatically when needed.

- CHANGELOG.md

- README.md

## Versioning

Flexera policy templates use [semantic versioning](https://semver.org/). This means all version numbers should contain three period-separated integers (example: `1.27.3`) that represent the MAJOR, MINOR, and PATCH versions respectively.

- MAJOR version should be changed if someone using automation to apply the updated policy template would run into an error or unexpected outcomes due to changes in parameters or fundamental changes in how the policy template works or what it does.

- MINOR version should be changed if new functionality or features are added in a way that does not fundamentally change what the policy template does and would not cause errors or problems for someone automating application of the policy template. For example, if new functionality were added with a parameter whose default value disables the new functionality.

- PATCH version should be changed for bug fixes or other minor changes that don't actually add new features or functionality, provided that the change does not meet the criteria for a MAJOR version change.

All version changes should be documented in the CHANGELOG.md file for the policy template.

## CHANGELOG.md

- The CHANGELOG.md file should be written in [Markdown](https://www.markdownguide.org/).

- The CHANGELOG.md file should always begin with the line `# Changelog` followed by an empty line.

- Each version, beginning with the most recent version, should be presented after `## v` and followed by an empty line.
  - _Example_: `## v2.3.0`

- Following the version should be a markdown list of all of the changes made in that version followed by an empty line. Changes should be described in terms of how they impact the end user where possible, making as few references to coding jargon or code itself as possible.

### Example

```text
# Changelog

## v0.2.0

- Removed requirement for AWS credential
- Internal API is now used to gather AWS account and tag information

## v0.1.0

- Initial release
```

## README.md

- The README.md file should be written in [Markdown](https://www.markdownguide.org/).

- The first line should begin with `#` followed by the name of the policy template.
  - _Example_: `# AWS Rule-Based Dimension From Account Tags`

- The following sections should be included in the order presented below. Optional sections are marked as optional. All sections should begin with `##`.
  1. What It Does
  1. How It Works (Optional)
  1. Input Parameters
  1. Policy Actions
  1. Prerequisites
  1. Supported Clouds
  1. Cost

- Additional sections needed for a specific policy template due to unique functionality or circumstances that do _not_ fall into one of the above sections should be added at the bottom and preceded with `##`. Additional sections needed for a specific policy template that _do_ fall into one of the above sections should be added to the bottom of that section and preceded with `###`.

### What It Does

This section should be a basic description of what the policy template does in 2-5 sentences.

#### Example

```text
## What It Does

This policy template finds AWS snapshots in the given account which are older than the specified days and deletes them after user approval. Snapshots with an associated AMI can be included or excluded depending on the settings selected when applying the policy; if included, the AMI will be deleted along with the snapshot if the snapshot is deleted.
```

### How It Works

This section should describes how the policy template produces the result it produces. Should be included when a user might want to know the specific formula used to calculate a value or the means by which specific data points are acquired.

Not required for simple policy templates where there is not much to say here.

#### Example

```text
## How It Works

- The policy leverages the AWS API to retrieve all instances and then uses the AWS CloudWatch API to check the instance CPU and Memory utilization over a specified number of days.
- The utilization data is provided for the following statistics: Average, Maximum, Minimum, 99th percentile, 95th percentile, 90th percentile.
- The policy identifies all instances that have CPU utilization and/or Memory utilization below the Idle Instance CPU/Memory Threshold(s) defined by the user. The recommendation provided for Idle Instances is a termination action; termination can be performed in an automated manner or after approval.
- The policy identifies all instances that have CPU utilization and/or Memory utilization below the Underutilized Instance CPU/Memory Threshold(s) defined by the user. The recommendation provided for Inefficient/Underutilized Instances is a downsize action; downsizing can be performed in an automated manner or after approval.
```

### Input Parameters

This section should contain a list of all of the policy template's parameters and what they do, including, where applicable, additional context not present in the policy template itself. Each parameter should be presented like the below example, with the name italicized and followed by a `-` character, followed by a description of the parameter.

An additional paragraph should be included at the bottom if destructive actions are possible due to choices made in parameters.

#### Example

```text
## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.
```

### Policy Actions

This section should contain a list of all possible actions the policy template can take, including sending an incident email.

#### Example

```text
## Policy Actions

- Send an email report
- Delete old snapshots after an approval
```

### Prerequisites

This section outlines the requirements for using the policy template. This will always begin with information about credentials and should always start with the following paragraph:

```text
This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).
```

This should be followed by an itemized list of every credential required for the policy template. Each credential should include a link to Flexera documentation about the credential, a description of the expected provider tag for the credential, and a list of specific permissions the credential needs. Optional permissions for specific functionality should be indicated with a `*` character and a footnote.

```text
- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeImages`
  - `ec2:DescribeSnapshots`
  - `ec2:DeregisterImage`*
  - `ec2:DeleteSnapshot`*
  - `rds:DescribeDBInstances`
  - `rds:DescribeDBSnapshots`
  - `rds:DescribeDBClusters`
  - `rds:DescribeDBClusterSnapshots`
  - `rds:DeleteDBClusterSnapshot`*
  - `rds:DeleteDBSnapshot`*
  - `sts:GetCallerIdentity`
  - `cloudtrail:LookupEvents`

  \* Only required for taking action (deletion); the policy will still function in a read-only capacity without these permissions.
```

After the list of credentials, the following paragraph should always be included at the end.

```text
The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.
```

For most policy templates, credentials are the only requirement. Any requirements other than credentials should be specified at the bottom of this section, beneath the above paragraph.

### Supported Clouds

This section contains a simple list of the cloud or SaaS providers supported by the policy template. A single item with "All" can be used for cloud-agnostic policy templates.

#### Example

```text
## Supported Clouds

- AWS
```

### Cost

This section just contains a simple statement about whether costs can be incurred from executing the policy template.

#### Example

```text
## Cost

This policy template does not incur any cloud costs.
```

## Policy Template

### General Conventions

- Anything contained within a block should be tabbed. Nested tabbing should be used for blocks within blocks.
  - Tabbing should be done using 2 space characters. It is recommended that you configure your editor to do this automatically whenever you press the tab key.

- Code blocks should always be separated from one another with an empty line.

- Avoid consecutive empty lines. There should only be one empty line between code blocks.

- Comma-separated lists should have a space following each comma. _Example_: apple, banana, pear

### Basic Structure

Strictly speaking, the Policy Template Language does not require that the various components of your policy template be in any particular order. That said, the following general arrangement is required for catalog policy templates.

Sections should be omitted if your policy template contains no blocks for that section, and blocks that are unused (such as a `pagination` or `credential` block that is never actually used by a `datasource` block) should be removed.

1. Metadata
1. Parameters
1. Credentials
1. Pagination
1. Datasources & Scripts
1. Policy
1. Escalations
1. Resolutions
1. Cloud Workflow

Each section (except for Metadata) should be preceded with comments resembling the below to clearly indicate where they begin:

```ruby
###############################################################################
# Datasources & Scripts
###############################################################################
```

Datasources should be presented in the order that they are expected to execute, followed by any script blocks that they call.

### Deprecated Code Blocks

The following code block types are deprecated and should not be used.

- Permission
- Resources

### Block Naming Conventions

Block names should always be in double-quotes and in [snake case](https://en.wikipedia.org/wiki/Snake_case). _Example_: `policy "pol_utilization" do`

Each block in the policy template should follow these naming conventions:

- **Parameter**
  - Names begin with `param_`
  - _Example_: `param_email`

- **Credential**
  - Names begin with `auth_`, followed by the provider or tool name.
  - _Example_: `auth_azure`

- **Pagination**
  - Names begin with `pagination_`, followed by the provider or tool name.
  - _Example_: `pagination_azure`

- **Datasource**
  - Names begin with `ds_`
  - _Example_: `ds_subscriptions`

- **Script**
  - Names begin with `js_`
  - _Example_: `js_filtered_subscriptions`

- **Paired Datasource/Script**
  - When a script pairs with a specific datasource, both blocks should share the same base name with their respective prefixes.
  - _Example_: `ds_filtered_subscriptions`, `js_filtered_subscriptions`

- **Policy**
  - Names begin with `pol_` and reflect what the policy template checks.
  - _Example_: `pol_rightsize_compute`

- **Escalation**
  - Names begin with `esc_`
  - _Example_: `esc_email`

- **Resolution**
  - Names begin with `res_`
  - _Example_: `res_resize_instances`

- **Cloud Workflow**
  - Named after the function they perform.
  - _Example_: `define delete_unattached_volumes`

### Metadata

The following guidelines should be used when specifying policy template metadata:

- **name**
  - Should clearly convey the policy template's purpose and, if applicable, include the cloud provider.
  - _Example_: `AWS Rightsize EC2 Instances`

- **short_description**
  - In most cases, should match the first lines of the README description.
  - Should include a link to the README.
  - _Example_: `Check for EC2 instances that have inefficient utilization for a specified number of days and downsizes or terminates them after approval. See the [README](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/) and [docs.flexera.com/flexera/EN/Automation](https://docs.flexera.com/flexera/EN/Automation/AutomationGS.htm) to learn more.`

- **long_description**
  - Always set to an empty string.

- **category**
  - Should be set to one of the following categories based on the policy template's intended purpose: Compliance, Cost, Operational, SaaS Management, Security

- **severity**
  - Choose sensible default based on how the policy template will typically be used.

- **default_frequency**
  - Choose sensible default based on how the policy template will typically be used.

- **info**
  - _version (required)_: The version number of the policy template. Semantic versioning should be used. _Example_: 1.0.3
  - _provider (required)_: The cloud or software provider the policy template is for. _Example_: AWS
  - _hide_skip_approvals (required): Set to "true" for most use cases. This hides the UI option to skip approvals, which causes confusion for some users.
  - _service (recommended)_: The category of service, product, etc. that the policy template is for. Avoid using abbreviations like "CCO" or "IAM". _Example_: Compute
  - _policy_set (recommended)_: The name of the set/collection that the policy template belongs to. _Example_: Rightsize Compute Instances
  - _recommendation_type_: Only required for policy templates intended to be scraped by the Optimization Dashboard. Should be set to either "Usage Reduction" (deleting or downsizing resources) or "Rate Reduction" (buying/adjusting commitments to lower cost without changing resources themselves) based on the type of recommendations the policy template produces.
  - _deprecated_: Defaults to "false" if unspecified. Include if you need to set this to "true" to indicate that a policy template is deprecated and no longer recommended for general use.
  - _publish_: Defaults to "true" if unspecified. Include if you need to set this to "false" to prevent the policy template from being published in the catalog.

- **tenancy**
  - This metadata field is defunct and should not be specified in any policy template.

#### Example

```ruby
name "AWS Rightsize EC2 Instances"
rs_pt_ver 20180301
type "policy"
short_description "Check for EC2 instances that have inefficient utilization for a specified number of days and downsizes or terminates them after approval. See the [README](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/) and [docs.flexera.com/flexera/EN/Automation](https://docs.flexera.com/flexera/EN/Automation/AutomationGS.htm) to learn more."
long_description ""
severity "low"
category "Cost"
default_frequency "weekly"
info(
  version: "5.3.2",
  provider: "AWS",
  service: "Compute",
  policy_set: "Rightsize Compute Instances",
  recommendation_type: "Usage Reduction",
  hide_skip_approvals: "true"
)
```

### Parameters

The following guidelines should be used for `parameters` blocks:

- Fields should be placed in the following order:
  1. `type`
  1. `category`
  1. `label`
  1. `description`
  1. `allowed_values` / `allowed_pattern`
  1. `min_value`
  1. `max_value`
  1. `default`

- **category**
  - Should always be included for every parameter.
  - Should be used to group similar parameters together.
  - _Example_: `Filters`

- **label**
  - A very short description of the parameter.
  - Should be a few words at the most and should be capitalized.
  - _Example_: `Email Addresses`

- **description**
  - A longer description (1-3 sentences) of the parameter written in plain English.
  - _Example_: `Email addresses of the recipients you wish to notify when new incidents are created.`

- **default**
  - A default should always be specified except in those cases where user input is absolutely required.
  - If the user is not required to specify a value, the default should either be an empty string `""` or an empty list `[]` depending on the type of the parameter.
  - If user input is required, put this comment instead of a default field: `# No default value, user input required`

#### Example

```ruby
parameter "param_regions_list" do
  type "list"
  category "Filters"
  label "Allow/Deny Regions List"
  description "A list of allowed or denied regions. See the README for more details"
  allowed_pattern /^([a-zA-Z-_]+-[a-zA-Z0-9-_]+-[0-9-_]+,*|)+$/
  default []
end
```

### Datasources

The following guidelines should be used for `datasource` blocks:

- Omit fields where the default covers it. For example, the default of the `verb` field is "GET", so there should never be any reason to specify this value explicitly for GET requests.

- Avoid setting the `scheme` field to "HTTP" unless absolutely necessary. Most REST APIs fully support HTTPS.

- The fields in the `request` block should always be in the following order:
  1. `auth`
  1. `pagination`
  1. `verb`
  1. `scheme`
  1. `host`
  1. `path`
  1. `header`
  1. `query`
  1. `body` / `body_field`
  1. `ignore_status`

#### Example

```ruby
datasource "ds_cloud_vendor_accounts" do
  request do
    auth $auth_flexera
    host val($ds_flexera_api_hosts, 'flexera')
    path join(["/finops-analytics/v1/orgs/", rs_org_id, "/cloud-vendor-accounts"])
    header "Api-Version", "1.0"
  end
  result do
    encoding "json"
    collect jmes_path(response, "values[*]") do
      field "id", jmes_path(col_item, "aws.accountId")
      field "name", jmes_path(col_item, "name")
      field "tags", jmes_path(col_item, "tags")
    end
  end
end
```

### Scripts

The following guidelines should be used for `script` blocks:

- The fields in the `script` block should always be in the following order:
  1. `parameters`
  1. `result`
  1. `code`

- **Name**
  - If the script is called by a single datasource, their names should match. _Example_: `ds_filtered_subscriptions`, `js_filtered_subscriptions`
  - If the script is called by a multiple datasources, give it a clear name that indicates it's function. _Example_: `js_cost_request`

- **Parameters**
  - Parameters should, where possible, be given the same name as the element being passed into the parameter. For example, if the datasource is passing "param_email" as the first parameter to the script, then the name of this parameter in the script should also be "param_email".

  - Parameters should be in the following order when called by a datasource:
    1. val(iter_item, _string_). _Example_: `val(iter_item, "id")`
    1. datasources. _Example_: `$ds_azure_vms`
    1. parameters. _Example_: `$param_emails`
    1. variables. _Example_: `rs_org_id`
    1. raw values. _Example_: `"primary"`

- **Result**
  - For scripts used to generate an API request, the result field should be set to `request`
  - For all other scripts, it should be set to `result`

- **Best Practices**
  - Don't do too much in a single script. Consider chaining 2 or 3 scripts if doing a complex multi-part operation. This will greatly simplify debugging.
  - Maintain consistent spacing and present code in a readable fashion.
  - Favor performance and readability over reducing the number of lines of code.
    - Make use of empty lines where appropriate to avoid bunching large amounts of code into a single wall of text.
    - Make use of [Underscore.js](https://underscorejs.org/) for common tasks. Avoid for loops where possible.
    - Avoid nested loops or other inefficient methods of searching through and processing data. The [Policy Development Training Repository](https://github.com/flexera-public/policy_engine_training/) has information on [optimizing policy templates](https://github.com/flexera-public/policy_engine_training/tree/main/lessons/13_optimization).
  - Favor descriptive variable names over short ones. Avoid, where possible, using single letter variable names like `o` or `p`.
  - Avoid leaving `console.log()` commands used for debugging in scripts. Debugging code should be removed once development work is complete.

#### Example

```ruby
script "js_aws_account", type:"javascript" do
  parameters "ds_cloud_vendor_accounts", "ds_get_caller_identity"
  result "result"
  code <<-EOS
  result = _.find(ds_cloud_vendor_accounts, function(account) {
    return account['id'] == ds_get_caller_identity[0]['account']
  })

  // This is in case the API does not return the relevant account info
  if (result == undefined) {
    result = {
      id: ds_get_caller_identity[0]['account'],
      name: "",
      tags: {}
    }
  }
EOS
end
```

### Policy

The following guidelines should be used for the `policy` block:

- Within the `validate` or `validate_each` block, fields should be placed in the following order:
  1. `summary_template`
  1. `detail_template`
  1. `check`
  1. `escalate`
  1. `hash_include` or `hash_exclude`
  1. `export`

- For the `summary_template` field:
  - Include the name of the applied policy itself. This is to make it easier to know which policy template the incident is associated with on the Automation -> Incidents page in Flexera One.

- For the `detail_template` field:
  - Use complete English sentences with proper grammar/spelling where it makes sense to do so.
  - **Currency**: Include currency symbol and appropriate separators. _Example_: `US$ 123,456.78`
  - **Percentages**: Append `%`. _Example_: `89.45%`

- For the `export` field:
  - Place fields with data the user is more likely to care about near the top of the list.
  - Avoid putting currency symbols, percentage signs, or other characters in fields that contain numbers. This tends to break sorting, making the column less usable.
    - Either place the symbol in the name of the field itself (_Example_: `CPU Usage (%)`) or include it in a separate column.
  - Sort the data by whichever field(s) make sense. For example, for a recommendations policy template, the largest potential savings should be at the top.
  - For policy templates that produce recommendations for the Optimization Dashboard, [specific export fields are required](https://docs.flexera.com/flexera/EN/Automation/CreateRecomendationFromPolicyTemp.htm).

#### Example

```ruby
policy "pol_disallowed_creds" do
  validate_each $ds_disallowed_credentials do
    summary_template "{{ with index data 0 }}{{ .policy_name }}{{ end }}: {{ len data }} Disallowed Automation Credentials Found"
    check eq(val(item, "id"), "")
    escalate $esc_email
    escalate $esc_delete_credentials
    export do
      resource_level true
      field "id" do
        label "ID"
      end
      field "name" do
        label "Name"
      end
      field "provider" do
        label "Provider"
      end
      field "scheme" do
        label "Scheme"
      end
    end
  end
end
```

### Escalations

The following guidelines should be used for `escalation` blocks:

- Fields should be placed in the following order:
  1. `automatic`
  1. `label`
  1. `description`
  1. `email`
  1. `run`

- **label**
  - A very short description of the escalation.
  - Should be a few words at the most and should be capitalized.
  - _Example_: `Stop Instances`

- **description**
  - A longer description (1-3 sentences) of the escalation written in plain English.
  - _Example_: `Approval to stop all selected instances.`

#### Example

```ruby
escalation "esc_downsize_instances" do
  automatic contains($param_automatic_action, "Downsize Instances")
  label "Downsize Instances"
  description "Approval to downsize all selected instances"
  run "downsize_instances", data
end
```

### Cloud Workflow

The following guidelines should be used for Cloud Workflow:

- Cloud Workflow blocks should be named after the task they are performing.
  - _Example_: `delete_snapshots`

- Plural should be used for the block that runs the action against a set of resources. Singular should be used for a separate block that runs against individual resources.
  - _Example_: `delete_snapshots` block iterates over a list of snapshots and calls `delete_snapshot` to delete each one.

- The `task_label` function should be used to document things as they happen to assist in debugging and troubleshooting:
  - _Example_: `task_label("Get AWS EC2 image successful: " + $instance["resourceID"])`

- `sub on_error: handle_error()` should be used to gather errors to be raised all at once. That way, a single failure doesn't prevent the rest of the actions from being performed.
  - Code that might raise errors should be inside of a `sub on_error: handle_error() do` `end` block.
  - `handle_error` should be its own dedicated Cloud Workflow block that stores errors in a global `$$errors` variable.
  - After that block, check if `$$errors` contains anything, and if it does, raise all of the errors at once.
    - `if inspect($$errors) != "null"` `raise join($$errors, "\n")` `end`

- Maintain consistent spacing and present code in a readable fashion.

- Favor performance and readability over reducing the number of lines of code.

- Make use of empty lines where appropriate to avoid bunching large amounts of code into a single wall of text.

- Favor descriptive variable names over short ones. Avoid, where possible, using single letter variable names like `o` or `p`.

#### Example

```ruby
define delete_snapshots($data, $param_azure_endpoint) return $all_responses do
  $$all_responses = []

  foreach $instance in $data do
    sub on_error: handle_error() do
      call delete_snapshot($instance, $param_azure_endpoint) retrieve $delete_response
    end
  end

  if inspect($$errors) != "null"
    raise join($$errors, "\n")
  end
end

define delete_snapshot($instance, $param_azure_endpoint) return $response do
  $host = $param_azure_endpoint
  $href = $instance["id"]
  $params = "?api-version=2019-07-01"
  $url = $host + $href + $params
  task_label("DELETE " + $url)

  $response = http_request(
    auth: $$auth_azure,
    https: true,
    verb: "delete",
    host: $host,
    href: $href,
    query_strings: { "api-version": "2019-07-01" }
  )

  task_label("Delete Azure snapshot response: " + $instance["id"] + " " + to_json($response))
  $$all_responses << to_json({"req": "DELETE " + $url, "resp": $response})

  if $response["code"] != 204 && $response["code"] != 202 && $response["code"] != 200
    raise "Unexpected response deleting Azure snapshot: "+ $instance["id"] + " " + to_json($response)
  else
    task_label("Delete Azure snapshot successful: " + $instance["id"])
  end
end

define handle_error() do
  if !$$errors
    $$errors = []
  end
  $$errors << $_error["type"] + ": " + $_error["message"]
  # We check for errors at the end, and raise them all together
  # Skip errors handled by this definition
  $_error_behavior = "skip"
end
```
