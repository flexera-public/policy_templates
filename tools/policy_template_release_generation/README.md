# Policy Template Release Notification Generation

A script that posts a formatted Microsoft Teams notification whenever policy templates are updated on the master branch.

## Overview

`generate_policy_release_notification_contents.rb` inspects the most recent commit to master and identifies changed `CHANGELOG.md` and `.pt` files. It then formats a summary of the updates (new versions, change descriptions, and links to templates) and delivers it as a webhook message to a Microsoft Teams channel.

## Usage

Run from the repository root:

```bash
ruby tools/policy_template_release_generation/generate_policy_release_notification_contents.rb
```

The `TEAMS_WEBHOOK_URL` environment variable must be set to a valid Microsoft Teams incoming webhook URL.

## Automated Workflow

There is an automated [GitHub Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-policy-release-notifications.yaml) that triggers on every push to master that modifies a `.pt` file. The workflow uses the `POLICY_CATALOG_UPDATE_TEAMS_WEBHOOK_URL_PROD` repository secret as the webhook URL.
