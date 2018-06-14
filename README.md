# RightScale Policy Templates

This repo contains a library of open source RightScale Policy Templates to provide goveranance via automation across Cost, Security, Operational, and Compliance categories. 

Please contact sales@rightscale.com to learn more. 

## Released Policy Templates

### Cost
- [AWS Reserved Instance Expiration](./cost/aws/reserved_instances/expiration/)
- [AWS Reserved Instances Utilization](./cost/aws/reserved_instances/utilization/)
- [AWS Reserved Instance Reservation Coverage](./cost/aws/reserved_instances/coverage/)
- [Downsize Instances](./cost/downsize_instance/)
- [Unattached Volumes Policy](./cost/volumes/)
- [Old Snapshots](./cost/volumes/old_snapshots/)

### Security
- [Security Group: ICMP Enabled](./security/security_groups/icmp_enabled/)
- [Security Group: Rules Without Description](./security/security_groups/rules_without_descriptions/)
- [Security Group: High Open Ports](./security/security_groups/high_open_ports/)
- [AWS Open Buckets Policy](./security/storage/aws/public_buckets/)
- [Google Open Buckets Policy](./security/storage/google/public_buckets/)

### Compliance
- [Untagged Resources](./compliance/tags/tag_checker)

### Operational
  Coming Soon

## Instructions to upload policy templates to RightScale

- The policy templates in the repo are the files that have a .pt extension. 
- Select the desired policy template, click on the “Raw” button, and then right-click and choose “Save As” to save the file to your computer.
- To upload the template to your account, navigate over to the Templates page in the left nav bar in [Governance](https://governance.rightscale.com). Ensure you have the role to access policy management in RightScale. Learn More about [Policy Access Control](http://docs.rightscale.com/policies/#how-policies-work-access-control).
- Click the “Upload Policy Template” button in the account you wish to test the policy and follow the instructions to upload the template you just downloaded.


## RightScale Policy Template Documentation
- [Getting Started](http://docs.rightscale.com/policies/getting_started/)
- [Reference Documentation](http://docs.rightscale.com/policies/reference/)
- [Policy Template Language](http://docs.rightscale.com/policies/reference/policy_template_language.html)
- [Markdown Editor](https://jbt.github.io/markdown-editor/) - Use this to test Markdown Syntax

## Getting Help
Support for these policy templates will be provided though GitHub Issues and the RightScale public slack channel #policies.
Visit http://chat.rightscale.com/ to join!

### Opening an Issue
Github issues contain a template for three types of requests(Bugs, New Features to an existing Policy Template, New Policy Template Request)

- Bugs: Any issue you are having with an existing policy template not functioning correctly, this does not include missing features, or actions.
- New Feature Request: Any feature(Field, Action, Link, Output, etc) that are to be added to an existing policy template.
- New Policy Template Request: Request for a new policy template.
