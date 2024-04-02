# Change History Script

Script to generate the `data/change_history/change_history.json` and `HISTORY.md` files.

- `data/change_history/change_history.json`: A list of all pull requests merged into the repository with the exception of pull requests to update that file.
- `HISTORY.md`: A curated, human-readable list of the last 100 pull requests that updated a policy asset.

## Usage

- Create a new branch and switch to that branch.
- Run the script from the root directory of the repository like so: `ruby tools/change_history/generate_change_history.rb`
- Run the `git add .` command to add the newly generated files.
- Commit and push the changes and submit a pull request.

## Automated Workflow

There is an automated [Github Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/update-change-history.yaml) that runs every time a pull request is merged and automatically submits a pull request with the updated files. The new PR can be approved by the Policy Template Maintainers.
