# Changelog

## v4.2.1

- Added `Service` field to incident table
- Minor code improvements to conform with current standards.

## v4.2

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v4.1

- Fixed issue where currency conversion would sometimes not work as expected.

## v4.0

- Policy now converts savings to local currency when appropriate
- Added exchange rate context to incident to allow user to revert currency conversion when needed
- Added ability to use Project list parameter as either an "allow" list or a "deny" list
- Added ability to filter recommendations by region
- Several parameters altered to be more descriptive and intuitive to use
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v3.3

- Modified the number of GCP recommender API calls that can be done before waiting to prevent a quota limit error: 100 request per minute.

## v3.2

- Updated recommendation service from 'Storage' to 'Compute'.
- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v3.1

- Fixed issue preventing policy from updating in the public catalog

## v3.0

- Added **Term** parameter, now filtering the recommendations by 1 year or 3 year term is possible.
- Added **Recommendation Algorithm** parameter, now users can choose between *Stable use* or *Optimal use*

## v2.7

- Removed param_automatic_action parameter, no applicable CWF
- hardset reduction type from Usage Reduction to Rate Reduction being set in scraper service

## v2.6

- Added policySet as Reserved Instance to populate the Total Potential Savings

## v2.5

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.4

- remove duplicate data fields for subscriptionID and subscriptionName

## v2.3

- added project name/id/number fields and moved account versions to end

## v2.2

- Fixed missing savings field
- updated changelog ordering

## v2.1

- Changes to fields for spend recommendations
  - changed "location" to "region"
  - changed "primary_impact" to "primaryImpact"
  - changed "projectID" to "accountID"
  - added "accountNumber"
  - added "accountName"
  - added "resourceID"
  - added "resourceName"
  - added "resourceType"
  - added "plan"
  - added "tags"
  - changed "id" path from "name" to "resourceID"
  - added "service"
  - added "description"

- Change to template name from "Google Committed Use Discount Recommender Policy" to "Google Committed Use Discount Recommender"

- updates to output of cud recommendations savings, addition of monthly calculations

## v2.0

- Initial Release
