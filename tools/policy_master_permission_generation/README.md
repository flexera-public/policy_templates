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
