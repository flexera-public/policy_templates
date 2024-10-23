# Flexera Billing Centers from Dimension Values

## What It Does

This policy generates a billing center structure based on specified dimensions. It allows users to create a hierarchical billing center structure that reflects their organizational needs by using existing dimensions -- including custom Rule-Based Dimensions, Tag Dimensions, or Cloud Bill Dimensions like Vendor, Cloud Vendor Account Name.

Billing Centers are required for granular access to cost data in Flexera and this Policy Template can help create the Billing Centers which are used to grant access to User Groups and Users.

Even without a requirement for granular access, the hierarchy view approach Billing Centers uses can also help an application owner find their costs and usage using a familiar hierarchy.

## How It Works

- The policy leverages the specified dimensions to create a hierarchical billing center structure.
- Users can specify a list of dimensions to be used for generating the billing center structure.
- An optional suffix can be appended to the billing center names to designate the level, which is useful for deeply nested billing centers.

### Example Scenario

Consider a scenario where the default `Dimension List` parameter value is used: "Vendor" and "Cloud Vendor Account Name". The policy will generate a hierarchical billing center structure based on these dimensions. Here are the vendor values and some example cloud account names:

- **Vendor Values**: "AWS", "Azure", "Google", "Oracle"
- **Cloud Account Names**: "project-alpha", "project-beta", "project-gamma", "project-delta", "project-epsilon"

The resulting hierarchy would look like this:

```
├── AWS
|   |
|   ├── aws-account1
|   ├── aws-account2
|   └── aws-account3
|
├── Azure
|   |
|   ├── azure-sub-A
|   ├── azure-sub-B
|   └── azure-sub-C
|
├── Google
|   |
|   ├── gcp-project-alpha
|   ├── gcp-project-beta
|   └── gcp-project-gamma
|
└── Oracle
    |
    ├── oci-account1
    ├── oci-account2
    └── oci-account3
```

In this example, the top level of the hierarchy is the "Vendor" dimension, and each vendor has several cloud accounts under it, represented by the "Cloud Vendor Account Name" dimension. This structure would work well if you wanted to grant access to costs at a Cloud Vendor or Cloud Vendor Account Scope.

## Input Parameters

- *Dimension List* - A list of dimensions to use for generating the billing center structure. Default is ["Cloud Vendor", "Cloud Vendor Account Name"].
- *Append Suffix* - A suffix to append to the end of the billing center name to designate the level. This can be useful for deeply nested billing centers.

## Policy Actions

The following policy actions are taken based on the specified dimensions:

- Generate a hierarchical billing center structure.
- Optionally append a suffix to the billing center names.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy does not incur any additional costs as it only generates a billing center structure based on the specified dimensions.
