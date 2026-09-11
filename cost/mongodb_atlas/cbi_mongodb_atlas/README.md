# MongoDB Atlas Common Bill Ingestion

## What It Does

This policy template retrieves MongoDB Atlas invoices and converts them to the Flexera Common Bill Ingestion (CBI) format. It uploads each selected billing period to an existing Flexera CBI endpoint so MongoDB Atlas costs can be viewed and allocated in Flexera Cloud Cost Optimization.

## How It Works

- The policy template uses the MongoDB Atlas API to retrieve organization groups and invoices for the requested number of months.
- MongoDB Atlas invoice line items are converted to CBI CSV records and uploaded in the order required by Flexera: create an upload, upload the CSV file, and commit the upload.
- The default lookback is one month. For an initial backfill, temporarily increase *Months* (for example, to 12), then return it to 1 for regular monthly operation.
- MongoDB Atlas invoice amounts use the currency reported by the first invoice payment. If the API does not return a payment currency, the template falls back to `USD`.

## Input Parameters

- *MongoDB Atlas Organization ID* - The 24-character MongoDB Atlas organization ID to query. This value is required and has no customer-specific default.
- *Months* - The number of months of invoices to retrieve on each run. Use a larger value for the initial backfill and use 1 for normal monthly updates.
- *Bill Connect ID* - The existing Flexera CBI endpoint that should receive the MongoDB Atlas costs. The endpoint must be created before this policy template is applied, and the value must match the endpoint's ID.
- *Email Addresses* - Email addresses of recipients to notify after invoice data is uploaded.

## Policy Actions

- Upload MongoDB Atlas invoice data to Flexera Cloud Cost Optimization through Common Bill Ingestion.
- Send an email report when the upload completes.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- **MongoDB Atlas Digest Credential** (*provider=mongodb_atlas*) - Create a custom Digest credential containing a MongoDB Atlas public/private API key pair. This credential is not able to be created through the normal Flexera user interface. Use Credentials API to create credential with type `digest`:

```sh
export flexeraAccesstoken="access.token.here"
export flexeraOrgId="12345"
export mongoPublicKey="..."
export mongoPrivateKey="..."
curl -i -H "Authorization: Bearer ${flexeraAccesstoken}" -X PUT "https://api.flexera.com/cred/v2/orgs/${flexeraOrgId}/credentials/digest/mongodb-atlas" -d "{\"password\": \"${mongoPrivateKey}\",\"username\": \"${mongoPublicKey}\",\"name\": \"MongoDB Atlas\",\"tags\": [{\"key\": \"provider\", \"value\": \"mongodb_atlas\"}]}"
```

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) with roles that allow viewing billing centers and creating, uploading, and committing CBI bill uploads. The closest standard CBI templates use `billing_center_viewer` and `csm_bill_upload_admin`; a `policy_viewer` role may also be required by the tenant's credential setup.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### Additional Requirements

Create the MongoDB CBI endpoint before running this policy template. Use the endpoint ID as the *Bill Connect ID* value. The endpoint's displayed cloud vendor name can be set to MongoDB (or another name suitable for your organization).

The generated `Tags` field preserves MongoDB Atlas line-item tags and adds `mongo-cluster-name` when a group name or cluster name is available. Its value is `groupName.clusterName` when both are present, or the available name when only one is present. The template also adds `mongo-stitch-app-name` and `mongo-cloud-provider` when Atlas returns those values. Create matching custom tags in Flexera if you use these values for allocation. The CBI dimensions are mapped as follows: the Atlas project ID and name populate `CloudVendorAccountID`/`CloudVendorAccountName` and `ResourceGroup`; `Category` is `Database`; `ResourceType` and `UsageType` use the Atlas SKU; `ResourceID` uses the cluster name; and `Service` is `MongoDB Atlas`. Atlas invoice details do not provide a reliable `InstanceType` or `Region`, so those columns remain blank.

## Supported Clouds

- MongoDB Atlas

## Cost

This policy template does not incur any cloud costs.
