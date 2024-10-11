# Flexera Billing Centers from Dimension Values

## What It Does

This policy generates a billing center structure based on specified dimensions. It allows users to create a hierarchical billing center structure that reflects their organizational needs by using existing dimensions -- including custom Rule-Based Dimensions, Tag Dimensions, or Cloud Bill Dimensions like Vendor, Cloud Vendor Account Name.

Billing Centers are required for granular access to cost data in Flexera and this Policy Template can help create the Billing Centers which are used to grant access to User Groups and Users.

Even without a requirement for granular access, the heirarchy view approach Billing Centers uses can also help an application owner find their costs and usage using a familiar hierarchy.

## Functional Details

- The policy leverages the specified dimensions to create a hierarchical billing center structure.
- Users can specify a list of dimensions to be used for generating the billing center structure.
- An optional suffix can be appended to the billing center names to designate the level, which is useful for deeply nested billing centers.

## Input Parameters

- *Dimension List* - A list of dimensions to use for generating the billing center structure. Default is ["Cloud Vendor", "Cloud Vendor Account Name"].
- *Append Suffix* - A suffix to append to the end of the billing center name to designate the level. This can be useful for deeply nested billing centers.

## Policy Actions

The following policy actions are taken based on the specified dimensions:

- Generate a hierarchical billing center structure.
- Optionally append a suffix to the billing center names.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources. In order to apply this policy, you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy.

### Credential configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy does not incur any additional costs as it only generates a billing center structure based on the specified dimensions.
```
