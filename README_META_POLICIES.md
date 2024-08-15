# Meta Policies

> Note: This is an **alpha** feature and should only be used with guidance from your Flexera Account Manager

## Description

Meta policies enable the user to apply multiple child policy templates at the same time, consolidating the results into a single policy incident. The primary use case is for AWS, where certain API calls, such as API calls to gather information about EC2 instances, can only be performed on a per-account basis. Meta policies enable a user to apply a single policy that will run child policies across all AWS accounts. Meta policies for Azure and GCP work similarly, but are primarily intended for situations where scale is preventing a single policy from being able to complete, since both of these providers allow for access across the entire estate with a single credential.

There are two components of a meta policy; the child policy, which is just the normal policy template one would typically use from the Flexera policy catalog, and the `Meta Parent` policy, which handles managing and applying child policies across all accounts and consolidates their incidents into a single incident for convenience.

## Configuration

### Flexera

For all meta policies, a Flexera credential with the appropriate permissions needs to be [added to the Flexera CCO platform](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm).

- Permissions:
  - `governance:action_status:index`
  - `governance:action_status:show`
  - `governance:applied_policy:create`
  - `governance:applied_policy:delete`
  - `governance:applied_policy:index`
  - `governance:applied_policy:show`
  - `governance:applied_policy:update`
  - `governance:incident:index`
  - `governance:incident:run_action`
  - `governance:incident:show`
  - `governance:policy_aggregate:create`
  - `governance:policy_aggregate:delete`
  - `governance:policy_aggregate:index`
  - `governance:policy_aggregate:show`
  - `governance:policy_aggregate:update`
  - `governance:policy_template:index`
  - `governance:policy_template:retrieve_data`
  - `governance:policy_template:show`
  - `governance:published_template:index`
  - `governance:published_template:show`
  - `optima:billing_center:index`
  - `optima:billing_center:show`
  - `optima:cloud_vendor_account:index`
  - `optima:custom_dimension:index`
  - `optima:custom_dimension:show`
  - `optima:recommendation:index`
  - `optima:recommendation:show`

- The above permissions correspond to the following roles in the Flexera CCO platform:
  - `Automation: Approve policies`
  - `Automation: Create policies`
  - `Automation: Manage policies`
  - `Automation: Publish policies`
  - `Automation: View policies`
  - `Cloud: View bill adjustments`
  - `Cloud: View cloud`
  - `Cloud: View cloud costs`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### Amazon Web Services

#### Create AWS Cross-Account Roles in AWS Account(s)

- The same name should be used for the role in every account. Permissions should be configured for whichever policy templates you intended to use.
- Recommended method for creating roles is AWS CloudFormation (StackSets). [We provide a template](https://raw.githubusercontent.com/flexera-public/policy_templates/master/tools/cloudformation-template/FlexeraAutomationPolicies.template) for this purpose.

#### [Create an AWS credential in the Flexera CCO platform](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1122264)

- This should be created as an ordinary AWS cross-account role.
- The role can be any of the roles created in step 1. The meta policy will infer the credentials for the rest of the AWS accounts based on the shared name.

### Microsoft Azure

Microsoft Azure requires no special configuration. Simply [add a Microsoft Azure credential](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1124668) with the appropriate permissions to the Flexera CCO platform.

### Google Cloud

Google Cloud requires no special configuration. Simply [add a Google Cloud credential](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) with the appropriate permissions to the Flexera CCO platform.

## Usage

Once the above configuration is complete, usage is straight-forward; apply the Meta Parent policy from the policy catalog for the policy template you're interested in, selecting the appropriate credential when applying the policy.

## Technical Details

### Expected lifecycle

#### First Parent Policy run

Creates the initial batch of create child policies and summary incidents.  Child policies are created in batches and if number of children is >20 [or `max_actions`], then it will take more than one run to deploy all child policies.

#### 2nd, 3rd, 4th, etc.. Parent Policy runs

Subsequent runs triggers `create`/`update`/`delete` of child policies associated with the Parent Applied Policy.

Child policies are managed in batches and each run can result in `max_actions` number of each; `create`, `update`, and `delete` actions.

For example, if you have 200 child policies to be created, the first run would create 50, the second run would create another 50, and so on until all 200 child policies are created.

#### Terminate Parent Policy

Terminating the Parent Policy will only delete the Parent Policy in that moment.  The child policies will terminate themselves on their next scheduled run when they see that the Parent Policy no longer exists.

----

## Known Limitations

### Recommendations may take up to 1hr to appear in the UI

Microservice that generates recommendations is configured to run on a schedule, so they will not immediately appear when an incident is created.  This is a Flexera One limitation and not necessarily related to Meta Policies.

### Child Applied Policies and Incidents are not currently visible in the UI

It's not possible to view logs or trigger "run now" on child policies.
It's not possible to view incidents from child policies in the UI beside the Cost Recommendations page.

### Recommendations from Child Policy Incidents take minimum 1day to disappear

Cost Savings Recommendations disappear when the Child Applied Policy is terminated, which happens on schedule depending `param_policy_schedule` (default: daily, [weekly, monthly]). Child Policies and Incidents are hidden from UI, and so this can be a little confusing and it's not possible using UI to trigger terminate or run now of child policy to clean up incidents/recommendations in < 1hr.  Must use API to "run" all child policies and trigger the ad-hoc "clean" when the child policies delete themselves if they don't have a parent policy that exists.

----

## Meta Policy Development

### Child Policy Template Modifications

A "child" policy is essentially just a standard policy template [i.e. from the catalog] which has some additional datasources and logic to make it work with the Meta Parent Policy.  The child policy can be used exactly as before and the additions have no resulting impact to their current functionality.

#### **Increment Version and Update CHANGELOG**

These changes should follow the standard change management processes, which includes bumping the version and updating the CHANGELOG.  Example CHANGELOG message:
`- Added logic required for "Meta Policy" use-cases`

#### **Identify "first" datasource and Add Header**

The easiest way to identify the "first" datasource absolutely is to apply the policy and then "View Logs" -- the first datasource listed is the one that should be modified.  The header parameter below should be added to the request.

```ruby
# Header X-Meta-Flexera has no affect on datasource query, but is required for Meta Policies
# Forces `ds_is_deleted` datasource to run first during policy execution
header "Meta-Flexera", val($ds_is_deleted, "path")
```

Example in datasource:

```ruby
datasource "ds_regions_list" do
  request do
    ...
    # Header X-Meta-Flexera has no affect on datasource query, but is required for Meta Policies
    # Forces `ds_is_deleted` datasource to run first during policy execution
    header "Meta-Flexera", val($ds_is_deleted, "path")
  end
  result do
    ...
  end
end
```

#### **Modify Policy Validation `check` statements**

All `check` statements needs to be modified to add an additional `logic_or()` statement to check if the `ds_parent_policy_terminated` is true.  This is required to ensure that the policy does not generate incidents if there is a parent policy and it has been deleted.

```ruby
# Policy check fails and incident is created only if data is not empty and the Parent Policy has not been terminated
check logic_or($ds_parent_policy_terminated,    <original check statement>    )
```

Given this original `check`: `check eq(size(val(data, "idle_instances")), 0)`

Example modified `check`:

```ruby
policy "pol_utilization" do
  validate $ds_instance_cost_mapping do
    ...
    # Policy check fails and incident is created only if data is not empty and the Parent Policy has not been terminated
    check logic_or($ds_parent_policy_terminated,    eq(size(val(data, "idle_instances")), 0)    )
    ...
  end
end
```

#### **Append Common Meta Policy Logic**

The majority of additions for child policies are common to all policies.  Generally it is recommended to place this at the bottom with the following comments.

<details><summary>Common Meta Policy Logic (Click to Expand)</summary>

```ruby
###############################################################################
# Meta Policy [alpha]
# Not intended to be modified or used by policy developers
###############################################################################

# If the meta_parent_policy_id is not set it will evaluate to an empty string and we will look for the policy itself,
# if it is set we will look for the parent policy.
datasource "ds_get_policy" do
  request do
    auth $auth_flexera
    host rs_governance_host
    ignore_status [404]
    path join(["/api/governance/projects/", rs_project_id, "/applied_policies/", switch(ne(meta_parent_policy_id, ""), meta_parent_policy_id, policy_id) ])
    header "Api-Version", "1.0"
  end
  result do
    encoding "json"
    field "id", jmes_path(response, "id")
  end
end

datasource "ds_parent_policy_terminated" do
  run_script $js_decide_if_self_terminate, $ds_get_policy, policy_id, meta_parent_policy_id
end

# If the policy was applied by a meta_parent_policy we confirm it exists if it doesn't we confirm we are deleting
# This information is used in two places:
# - determining whether or not we make a delete call
# - determining if we should create an incident (we don't want to create an incident on the run where we terminate)
script "js_decide_if_self_terminate", type: "javascript" do
  parameters "found", "self_policy_id", "meta_parent_policy_id"
  result "result"
  code <<-EOS
  var result
  if (meta_parent_policy_id != "" && found.id == undefined) {
    result = true
  } else {
    result = false
  }
  EOS
end

# Two potentials ways to set this up:
# - this way and make a unneeded 'get' request when not deleting
# - make the delete request an interate and have it iterate over an empty array when not deleting and an array with one item when deleting
script "js_make_terminate_request", type: "javascript" do
  parameters "should_delete", "policy_id", "rs_project_id", "rs_governance_host"
  result "request"
  code <<-EOS

  var request = {
    auth:  'auth_flexera',
    host: rs_governance_host,
    path: "/api/governance/projects/" + rs_project_id + "/applied_policies/" + policy_id,
    headers: {
      "API-Version": "1.0",
      "Content-Type":"application/json"
    },
  }

  if (should_delete) {
    request.verb = 'DELETE'
  }
  EOS
end

datasource "ds_terminate_self" do
  request do
    run_script $js_make_terminate_request, $ds_parent_policy_terminated, policy_id, rs_project_id, rs_governance_host
  end
end

datasource "ds_is_deleted" do
  run_script $js_check_deleted, $ds_terminate_self
end

# This is just a way to have the check delete request connect to the farthest leaf from policy.
# We want the delete check to the first thing the policy does to avoid the policy erroring before it can decide whether or not it needs to self terminate
# Example a customer deletes a credential and then terminates the parent policy. We still want the children to self terminate
# The only way I could see this not happening is if the user who applied the parent_meta_policy was offboarded or lost policy access, the policies who are impersonating the user
# would not have access to self-terminate
# It may be useful for the backend to enable a mass terminate at some point for all meta_child_policies associated with an id.
script "js_check_deleted", type: "javascript" do
  parameters "response"
  result "result"
  code <<-EOS
  result = {"path":"/"}
  EOS
end
```

</details>

----

### Meta Parent Policy Template

The Meta Parent Policy Template is a new policy template, that is associated with a specific child policy template.  We have a script to compile the Meta Parent Policy Templates once the child policy template has the appropriate "meta" code added to it and those changes have been published.

When we want to create a new Meta Parent policy template regularly, we should append the list defined in [tools/meta_parent_policy_compiler/meta_parent_policy_compiler.rb](tools/meta_parent_policy_compiler/meta_parent_policy_compiler.rb)

More information at [tools/meta_parent_policy_compiler/README.md](tools/meta_parent_policy_compiler/README.md)

#### Custom Meta Parent Templates

For generating meta parent policy templates in the Flexera catalog, a custom template file can be used for situations where the default template file produces undesired results. To take advantage of this functionality, you need to do the following:

- Place the custom template file in the same directory as the policy template itself. For example, if the path to your policy template is `operational/aws/tag_cardinality/aws_tag_cardinality.pt`, the custom template file path should be `operational/aws/tag_cardinality/aws_tag_cardinality_meta_parent.pt.template`. There is no required naming convention but the convention implied with this example is recommended.

- Add a `meta_template` field to the info() block of the child policy template containing the file name of the custom template. For the above example, this would look like the following:

```
info(
  version: "3.2.0",
  provider: "AWS",
  service: "Tags",
  policy_set: "Tag Cardinality",
  meta_template: "aws_tag_cardinality_meta_parent.pt.template"
)
```

- As long as the above has been done correctly, the automation for generating meta parent policy templates will automatically use the custom template instead of the default one.
