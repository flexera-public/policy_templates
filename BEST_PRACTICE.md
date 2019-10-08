# Best Practice Guide

This document is to help developers to have consistent policies and guide the development approach.  

## Template Design

- Policy Metadata should be at the top of the policy file
Consider an appropriate name that will resonate well with the policy users/customers.   The policy name should give a good idea of what the policy will do.
   - The short_description attribute should contain the same as the first couple of lines of the policy description as shown in the README
   - The short description should have a link to the README file
   - The long_description should have the Version number.  For example: "Version: 1.0."
   - Consider the appropriate category and severity of the policy.
- Parameter declarations should follow the metadata declarations
   - consider appropriate label and description to make the inputs intuitive
   - labels should be short, i.e. Email List
   - descriptions should be long. i.e. Enter the email addresses to send the incident report to.  
- Permission declarations should follow the parameter declarations
- Auth declarations should follow the permissions declarations
- resource declarations should follow the auth declarations
- datasource declarations should follow the resource declarations
- Escalation and Resolution declarations should follow the datasource declarations
- policy declaration should follow the escalation and resolution declarations
- CWF definitions should follow the policy declarations
- A policy with an action other than email should also include request_approval in the actions escalation.

## Programming Patterns
- When working with RightScale resources you can create a single policy for all clouds.  When working with cloud API's directly each cloud should have its own policy.  For example, when working with cloud IAM API, create three separate policies for AWS, Azure, and Google.
- Use Javascript Datasource to create maps and links between resources.  For example, you can create a cloud map with it's href and instance href to show the cloud and instance within the same table.
- Use CWF (Cloud Workflow Flow) to handle automation, ie. delete or tag a resource.
- Use multiple escalations to handle different actions.  
- Any policy that checks resources needs to have an input for which tags to ignore. Any resource with those tags will not be checked/reported on for the policy.

## Common Functional Requirements
- If an API being used as a datasource paginates responses, pagination must be implemented as described in the docs
- If the policy is checking a "resource", and that resource supports tagging, then the policy must provide a "Tags to Ignore" parameter which allows the user to specify a list of tags. Any resource that contains any tag listed should be ignored during evaluation. The user can specify a tag key only, or a tag key + value.

## Naming Conventions
- Resources have the resource_name for its name i.e. `rs_cm.clouds = clouds`
- Datasources are all prefixed with `ds_`
- Javascript datasources start with `js_`
- Policy declarations start with `policy_`
- Escalation declarations start with `esc_`
- Resolution declarations start with `res_`

## Repository Structure

- The policy file name should the same or similar to the policy name in the NAME metadata.
- The policy file extension should be .pt
- Each policy should be in the sub directory of the policy category and it's own directory.
- Each policy directory should include the CHANGELOG.md and README.md files
- The root README.md file should be updated to reference new policy.

## Versioning the Policy
- When the .pt file changes the version number should increment and the CHANGELOG.md updated
- Each policy release should increment the Version number in the long_description Attribute
- Each release should include the changes made included in the CHANGELOG file

## Development Workflow
Developers are not allowed to commit directly to the Master branch.  Instead commit and push your changes to a branch, then create pull requests for peer reviews.  

For questions or comments post a [new issue](https://github.com/flexera/policy_templates/issues/new) with a *question* label.
