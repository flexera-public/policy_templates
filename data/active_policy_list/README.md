# Active Policy List

This JSON file contains a list of all published policies in the catalog and their metadata. This list is generated through automation every time a pull request is merged into the repository.

- [Rakefile](https://github.com/flexera-public/policy_templates/blob/master/Rakefile) used for generating this asset.
- [Github Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/update-active-policy-list.yaml) to run the above Rakefile when a pull request is merged.
- [active_policy_list.json](active_policy_list.json) - The generated JSON file containing list of all policy templates that should be published to the catalog.

## Generally Recommended Policy Templates List

The [`generally_recommended_policy_templates_list.yaml`](generally_recommended_policy_templates_list.yaml) file defines the generally recommended policy templates.  The list is curated by the Flexera Solution Architect and Advisor teams and includes the Catalog Policy Templates we generally recommend for all customers (given they use the respective vendor).

The result of this is that the (active_policy_list.json)[active_policy_list.json] file will contain a `generally_recommended` key for each policy template with a "true" or "false" value.  Automation tools/scripts, as well as Customers directly can reference this list as a source of truth for what policy templates are generally recommended.

Policy Templates which are generally recommended have the following characteristics:
- Be well tested in field
- Have default values for all required parameters
- Existing validated outcomes from customers
