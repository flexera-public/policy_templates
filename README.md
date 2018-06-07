# Please contact sales@rightscale.com to learn more.

# RightScale Policy Templates

This repo contains a library of open source RightScale Policy Templates for various categories. 

## Released Policy Templates

### Cost
- [AWS Reserved Instance Expiration](./cost/aws/reserved_instances/expiration/)
- [AWS Reserved Instances Utilization](./cost/aws/reserved_instances/utilization/)
- [AWS Reserved Instance Reservation Coverage](./cost/aws/reserved_instances/coverage/)
- [Downsize Instances](./cost/downsize_instance/)
- [Unattached Volumes Policy](./cost/volumes/)

### Security
- [ICMP Enabled Security Group](./security/security_groups/icmp_enabled/)
- [Security Group Rules Without Description](./security/security_groups/rules_without_descriptions/)
- [AWS Open Buckets Policy](./security/storage/aws/public_buckets/)
- [Google Open Buckets Policy](./security/storage/google/public_buckets/)

### Operational
Coming Soon

### Compliance
- [Untagged Resources](./compliance/tags/tag_checker)

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
