# Meta Parent Policy Compiler

A script that compiles a "Meta Parent" Policy Template from a "Child" Policy Template source file.

## Usage

Basic Usage:

```sh
ruby meta_parent_policy_compiler.rb [optional_path_to_child_policy_template] [optional_path_to_child_policy_template] ...
```

If no child policy templates files are specified, then the default list of child policy template files that is defined in the

Output meta parent policy template file will be the same directory as the source child policy template but with a `_meta_parent.pt` suffix.

## Automated Workflow
There is an automated workflow that runs every time a push to the default branch is made.  Whenever there are changes resulting from running the compile script, a new PR is made and can be approved by the Policy Template Maintainers.

[![Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/workflows/generate-meta-parent-policy-templates.yaml/badge.svg?event=push)](https://github.com/flexera-public/policy_templates/actions/workflows/generate-meta-parent-policy-templates.yaml)

Workflow defined in file [.github/workflows/generate-meta-parent-policy-templates.yaml](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-meta-parent-policy-templates.yaml)
