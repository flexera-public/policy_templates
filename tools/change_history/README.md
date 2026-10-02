# Change History Script

Script to generate the `data/change_history/change_history.json` and `HISTORY.md` files.

- `data/change_history/change_history.json`: A list of all pull requests merged into the repository with the exception of pull requests to update that file.
- `HISTORY.md`: A curated, human-readable list of the last 100 pull requests that updated a policy asset.

## Incremental Fetching

The script only asks the Github Search API for pull requests merged after the most recent one already recorded in `data/change_history/change_history.json`, then merges those into the existing data. It does not re-fetch or re-process the entire pull request history on every run.

If `data/change_history/change_history.json` does not exist or cannot be parsed, the script falls back to a one-time full historical fetch using the Pull Requests API (the Search API caps results at 1,000 per query, so it cannot be used to rebuild the complete history). This full fetch is slow, since it makes a separate API call per pull request to determine which files it modified, so avoid deleting `data/change_history/change_history.json` unless a full rebuild is actually needed.

## Usage

- Create a new branch and switch to that branch.
- Run the script from the root directory of the repository like so: `ruby tools/change_history/generate_change_history.rb`
- Run the `git add .` command to add the newly generated files.
- Commit and push the changes and submit a pull request.

## Automated Workflow

There is an automated [Github Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/update-change-history.yaml) that runs every time a pull request is merged and automatically submits a pull request with the updated files. The new PR can be approved by the Policy Template Maintainers.
