# MongoDB Atlas Common Bill Ingestion

## What It Does

This policy template retrieves MongoDB Atlas invoices and converts them to the Flexera Common Bill Ingestion (CBI) format. It uploads each selected billing period to an existing Flexera CBI endpoint so MongoDB Atlas costs can be viewed and allocated in Flexera Cloud Cost Optimization.

## How It Works

- The policy template uses the MongoDB Atlas API to retrieve organization groups and invoices for the selected billing period.
- MongoDB Atlas invoice line items are converted to CBI CSV records and uploaded in the order required by Flexera: create an upload, upload the CSV file, and commit the upload.
- Select the current month, previous month, or a specific month. Use *Billing Period* to provide a month in `YYYY-MM` format when *Month To Ingest* is set to *Specific Month*.
- MongoDB Atlas invoice amounts are written with `USD` as the currency code. This template assumes the MongoDB Atlas billing API data being retrieved is billed in USD; validate this assumption if your organization uses another billing currency.

## Input Parameters

- *Email Addresses* - Email addresses of recipients to notify after invoice data is uploaded.
- *Month To Ingest* - Select whether to retrieve invoices for the current month, previous month, or a specific month.
- *Billing Period* - The month to retrieve in `YYYY-MM` format. This parameter is used only when *Month To Ingest* is *Specific Month*.
- *Flexera CBI Endpoint* - The ID of the existing Flexera CBI endpoint that should receive MongoDB Atlas costs. This value is required and must match the endpoint's ID.
- *MongoDB Atlas Organization ID* - The 24-character MongoDB Atlas organization ID to query. This value is required and has no customer-specific default.

## Policy Actions

- Upload MongoDB Atlas invoice data to Flexera Cloud Cost Optimization through Common Bill Ingestion.
- Send an email report when the upload completes.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- **MongoDB Atlas Digest Credential** (*provider=mongodb_atlas*) - Create a custom Digest credential containing a MongoDB Atlas public/private API key pair. This credential is not able to be created through the normal Flexera user interface.
  - `Organization Billing Viewer`
  - `Organization Read-Only`

  Use the [Credentials](https://developer.flexera.com/docs/api/cred/v2#/Digest%20Credential/Digest%20Credential%23create_project) API to create a `digest` credential:

  ```sh
  export flexeraAccesstoken="access.token.here"
  export flexeraProjectId="123456"
  export mongoPublicKey="..."
  export mongoPrivateKey="..."
  export flexeraApiHost="https://api.flexera.com"
  curl -i -H "Content-Type: application/json" -H "Authorization: Bearer ${flexeraAccesstoken}" -X PUT "${flexeraApiHost}/cred/v2/projects/${flexeraProjectId}/credentials/digest/mongodb-atlas" -d '{"password": "'"${mongoPrivateKey}"'","username": "'"${mongoPublicKey}"'","name": "MongoDB Atlas","tags": [{"key": "provider", "value": "mongodb_atlas"}]}'
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `csm_bill_upload_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### Additional Requirements

Create the MongoDB CBI endpoint before running this policy template by following the [Flexera Common Bill Ingestion setup instructions](https://docs.flexera.com/flexera-one/administration/cloud-settings/bill-data-connections/bill-connect-configurations/common-bill-ingestion/). Use the endpoint ID as the *Flexera CBI Endpoint* value. The endpoint's displayed cloud vendor name can be set to MongoDB (or another name suitable for your organization).

The generated `Tags` field includes the custom tag key `mongo-cluster-name` when a group name or cluster name is available. Its value is `groupName.clusterName` when both are present, or the available name when only one is present. Create a matching custom tag in Flexera if you use this value for allocation. If your allocation model does not use this tag, adapt or remove that tag mapping in a copy of the template; the account and resource fields remain available for allocation.

## Supported Clouds

- MongoDB Atlas

## Cost

This policy template does not incur any cloud costs.
