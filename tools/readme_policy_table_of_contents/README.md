# Policy Template README Table of Contents

## Generate README Table of Contents

The [Generate README Table of Contents](https://github.com/flexera-public/policy_templates/actions/workflows/generate-readme-policy-table-of-contents.yaml) GitHub Actions Workflow is triggered anytime there is a push to the master branch and will create a pull request with the updated README Table of Contents.

The below command can be used for manual generation of the README.md file:

```bash
ruby tools/readme_policy_table_of_contents/generate_readme_policy_table_of_contents.rb
```
