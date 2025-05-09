# Azure Cloud Data

Various Azure-specific data assets, such as pricing data. Some assets are manually maintained and some are generated through automation; see the [Cloud Data Scripts README](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/README.md) for more information on how these assets are generated.

## azure_compute_instance_types.json / instance_types.json

`azure_compute_instance_types.json` is a newer asset generated and updated through automation. It's data comes directly from the Azure API. This asset should be used in policy templates that need detailed information about Azure virtual machine instance types.

`instance_types.json` is similar but is older and manually maintained. It should not be used in policy templates going forward. This asset will remain in the repository long term to ensure that older policy templates continue to function as intended.

Some data fields in `azure_compute_instance_types.json` are currently imported from `instance_types.json` until we build proper automation to gather/calculate this information:

- superseded
- specs.nfu
