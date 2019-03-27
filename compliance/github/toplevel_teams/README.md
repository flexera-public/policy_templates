## GitHub.com Top-Level Teams

### What it does

This Policy Template gets the top-level / parent Teams for a GitHub.com Org and creates an incident if any do not match the whitelisted values.

### Parameters
1. GitHub.com Organizations to check - Example: `flexera`
2. Whitelisted Top-Level Team Names - Example: `Engineering`, `Services`
3. Email address to send escalation emails to - Example: `noreply@example.com`


### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report


### Required Permissions

This policy requires permissions to access GitHub.com API as the Owner of the Organization(s).  Before applying this policy, create a GitHub.com Personal Access Token with `repo`, and `admin:org read:org` scopes, and save the token in the project on Cloud Management as credential named `GITHUB_API_TOPLEVEL_TEAMS_PERSONAL_ACCESS_TOKEN`

This policy requires permissions to access RightScale resources (credentials). Before applying this policy add the following roles to the user applying the policy.  For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - credential_viewer or admin
- Cloud Management - observer


### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
