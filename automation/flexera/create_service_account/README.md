# Flexera Create Service Account

## What It Does

This policy template creates a Flexera service account via the IAM API, assigns the specified org-level roles to it, generates a client secret, and then registers an OAuth2 credential in Flexera Automation using that client ID and secret. If all steps succeed, an incident is raised containing the credential details and confirmation of role assignments.

## How It Works

The policy template performs the following steps in sequence:

1. Creates the service account by calling `POST /iam/v1/orgs/{org_id}/service-accounts` with the specified name and description.
1. Since the creation response returns an empty body, lists all service accounts via `GET /iam/v1/orgs/{org_id}/service-accounts` and identifies the newly created one by name to obtain its ID.
1. Assigns each selected role to the service account by calling `PUT /iam/v1/orgs/{org_id}/access-rules/grant` once per role.
1. Generates a client secret for the service account by calling `POST /iam/v1/orgs/{org_id}/service-accounts/{id}/clients`.
1. Registers an OAuth2 credential in Flexera Automation by calling `PUT /cred/v2/projects/{project_id}/credentials/oauth2/{cred_id}` using the client ID and secret from the previous step.
1. Since the credential creation response returns an empty body, lists credentials via `GET /cred/v2/orgs/{org_id}/credentials` filtered by name and identifies the newly created one to obtain its ID.
1. Raises an incident containing the credential details and role assignment summary.

If any step fails, the policy execution fails immediately and no further steps are taken.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Service Account Name* - The name to give the new Flexera service account and its corresponding Flexera Automation credential.
- *Service Account Description* - The description to give the new Flexera service account and its corresponding Flexera Automation credential. Defaults to empty.
- *Roles* - The roles to assign to the service account. Select role(s) by display name.

> **Important:** This policy template creates Flexera resources each time it runs. It is intended to be applied once, used to create the service account and credential, then terminated. See the Next Steps section in the incident for termination instructions.

## Policy Actions

The following actions may be taken by this policy template:

- Raises an incident containing the new credential details upon successful creation.
- Sends an email notification to the specified addresses.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `iam_admin`
  - `enterprise_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any additional costs.
