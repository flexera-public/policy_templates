# Meta Parent Policy Compiler

A script that compiles a "Meta Parent" Policy Template from a "Child" Policy Template source file.

## Usage

Basic Usage:

- Specify *--from-list* as the first parameter and the file path of a YAML file as the second parameter to automatically generate meta parents from a list of file paths. The YAML file should contain a flat list of file names/paths under the grouping "policy_templates":
  - Example: `ruby meta_parent_policy_compiler.rb --from-list default_template_files.yaml`
- Specify *--target-policy* as the first parameter, a policy template file path as the second parameter and a cloud provider (aws azure google) for the third parameter to generate a meta parent policy template from one of the provided meta parent templates for major cloud providers.
  - Example: `ruby meta_parent_policy_compiler.rb --target-policy local/aws/aws_vms.pt aws`
- Specify *--target-policy* as the first parameter, a policy template file path as the second parameter, 'custom' for the third parameter, and a meta parent template file path for the fourth parameter to generate a meta parent policy template using a custom meta parent template file.
  - Example: `ruby meta_parent_policy_compiler.rb --target-policy local/oci/oci_vms.pt custom local/oci/oci_vms_meta_parent.pt.template`

Example YAML file list:

```yaml
policy_templates:
-  "../../automation/aws/aws_missing_regions/aws_missing_regions.pt"
-  "../../compliance/aws/disallowed_regions/aws_disallowed_regions.pt"
-  "../../compliance/aws/ecs_unused/aws_unused_ecs_clusters.pt"
-  "../../compliance/aws/iam_role_audit/aws_iam_role_audit.pt"
```

Output meta parent policy template file will be the same directory as the source child policy template but with a `_meta_parent.pt` suffix.

Note: Child policy templates have to be modified in a few small ways in order for meta parent policy templates to be generated. Please see the [Meta Policies README](https://github.com/flexera-public/policy_templates/blob/master/README_META_POLICIES.md) for more information.

## Automated Workflow

There is an automated workflow that runs every time a push to the default branch is made.  Whenever there are changes resulting from running the compile script, a new PR is made and can be approved by the Policy Template Maintainers.

[![Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/workflows/generate-meta-parent-policy-templates.yaml/badge.svg?event=push)](https://github.com/flexera-public/policy_templates/actions/workflows/generate-meta-parent-policy-templates.yaml)

Workflow defined in file [.github/workflows/generate-meta-parent-policy-templates.yaml](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-meta-parent-policy-templates.yaml)
