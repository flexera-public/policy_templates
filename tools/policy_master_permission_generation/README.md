# Generate Policy Permissions Script

This script parses the `README.md` files for each Policy Template and generates a policy permission list dataset which can be used to generate other artifacts that require permissions.

## Enabling a Policy Template for Automated Policy Permission Generation

1. Open `.pt` file in code editor to review

1. For each `datasource` which make a `request` and include an `auth` configuration (i.e. *auth_azure*, *auth_aws*, etc..) validate the permission required for that request is in the `README.md`.  The goal here is to validate that all permissions that at needed by the `.pt` file are documented in the `README.md`

1. Add the `.pt` file to list of files in [`tools/policy_master_permission_generation/validated_policy_templates.yaml`](./validated_policy_templates.yaml)

1. Run [`tools/policy_master_permission_generation/generate_policy_master_permissions.rb`](./generate_policy_master_permissions.rb)

   ```sh
   $ ruby tools/policy_master_permission_generation/generate_policy_master_permissions.rb
   ```

1. For each permission in the `README.md`, validate that the permission is correctly added to the output datasets in [`data/policy_permissions_list`](../../data/policy_permissions_list)

1. Commit and push changes to datasets in [`data/policy_permissions_list`](../../data/policy_permissions_list) and [`tools/policy_master_permission_generation/validated_policy_templates.yaml`](./validated_policy_templates.yaml)

   ```sh
   # Stage the changes
   $ git add data/policy_permissions_list/ tools/policy_master_permission_generation/validated_policy_templates.yaml

   # Commit the changes
   $ git commit -m "task: enable PT for automated permissions"

   # Push changes to github for review;
   # git push .....
   ```

## Identifying Missing Templates

A companion script, [`generate_missing_permission_list.rb`](./generate_missing_permission_list.rb), identifies policy template files in the repository that are not yet present in `validated_policy_templates.yaml`. It writes two output files:

- `data/policy_permissions_list/missing_policy_templates.json`
- `data/policy_permissions_list/missing_policy_templates.yaml`

Run from the repository root:

```sh
ruby tools/policy_master_permission_generation/generate_missing_permission_list.rb
```

## Automated Workflows

### Generate Policy Master Permissions

There is an automated [GitHub Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-policy-master-permissions-json.yaml) that runs every time a push to the master branch modifies a `.pt` file or any file in this directory. It runs `generate_policy_master_permissions.rb` and automatically opens a pull request with the updated permissions data files, which can be approved by the Policy Template Maintainers.

### Generate Missing Templates List

There is a second automated [GitHub Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-policy-master-permission-missing-templates.yaml) that runs every time the [Test Policies](https://github.com/flexera-public/policy_templates/actions/workflows/test-policies.yaml) workflow completes successfully against master. It runs `generate_missing_permission_list.rb` and automatically opens a pull request with the updated list of policy templates not yet covered by the permissions process.
