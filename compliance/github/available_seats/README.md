## GitHub.com Available Seats

### What it does

This Policy Template will get the total used/available seats for a GitHub.com Organization and create an incident if the number of available seats fall outside the policy's min and max parameters.


### Parameters
1. GitHub.com Organizations to check - Example: flexera
2. Allowed Minimum Available Seats - Example: 10
3. Allowed Maximum Available Seats - Example: 50
4. Email address to send escalation emails to - Example: noreply@example.com


### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report


### Required Permissions

This policy requires permissions to access GitHub.com API as the Owner of the Organization(s).  Before applying this policy, create a GitHub.com Personal Access Token under the user with Owner role -- adding the `admin:org read:org` scopes at minimum, and save the token in the project on Cloud Management as credential named `GITHUB_ORG_ADMIN_ACCESS_TOKEN`.  If you are using other Governance Policies for GitHub.com, you may need to include additional roles to sate the need of all policies which use the same credential.  Optionally, you can generate a token with full permission and avoid any issues.

This policy requires permissions to access RightScale resources (credentials). Before applying this policy add the following roles to the user applying the policy.  For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - credential_viewer or admin
- Cloud Management - observer


### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
