## Tools

- [Flexera Automation CloudFormation Template](./tools/cloudformation-template)
- [`fpt` Command Line Tool](https://github.com/flexera-public/policy_sdk/tree/master/cmd/fpt)

## Policy Data Sets

Some policies require external data sets to function.  These data sets are stored in the [data](./data) directory.  The following data sets are available:

- [AWS Regions](./data/aws/regions.json)
- [AWS Instance Types](./data/aws/instance_types.json)
- [Azure Instance Types](./data/azure/instance_types.json)
- [Google Instance Types](./data/google/instance_types.json)
- [Currency Reference](./data/currency/currency_reference.json)
- [Azure SQL Service Tier Types](./data/azure/sql_service_tier_types.json)
- [Azure SQL Managed Instance Tier Types](./data/azure/sqlmi_tier_types.json)
- [TZ database Timezone List](./data/tz_database/timezones_list.json)

## Instructions to upload policy templates to Flexera CMP Policies

- The policy templates in the repo are the files that have a .pt extension.
- Select the desired policy template, click on the “Raw” button, and then right-click and choose “Save As” to save the file to your computer.
- To upload the template to your account, navigate over to the Templates page in the left nav bar in [Governance](https://governance.rightscale.com). Ensure you have the role to access policy management in RightScale. Learn More about [Policy Access Control](https://docs.flexera.com/flexera/EN/Automation/AutomationGS.htm#how-policies-work-access-control).
- Click the “Upload Policy Template” button in the account you wish to test the policy and follow the instructions to upload the template you just downloaded.

## Policy Template Documentation

- [Getting Started](https://docs.flexera.com/flexera/EN/Automation/AutomationGS.htm)
- [Reference Documentation](https://docs.flexera.com/flexera/EN/Automation/AutomationRefInfo.htm#automationrefinfo_1419216867_1009635)
- [Policy Template Language](https://docs.flexera.com/flexera/EN/Automation/PTL.htm#automationrefinfo_1419216867_1122815)
- [Markdown Editor](https://jbt.github.io/markdown-editor/) - Use this to test Markdown Syntax
- [README GUIDELINE](./README_GUIDELINE.md)

## Getting Help

Support for these policy templates will be provided though GitHub Issues and the Flexera Community.
Visit [Flexera Community](https://community.flexera.com) to join!

### Opening an Issue

Github issues contain a template for three types of requests(Bugs, New Features to an existing Policy Template, New Policy Template Request)

- Bugs: Any issue you are having with an existing policy template not functioning correctly, this does not include missing features, or actions.
- New Feature Request: Any feature(Field, Action, Link, Output, etc) that are to be added to an existing policy template.
- New Policy Template Request: Request for a new policy template.

### Troubleshooting Danger Locally

- You can test against a pull request via: `bundle exec danger pr https://github.com/flexera-public/policy_templates/pull/73 --pry`
- [Danger Troubleshooting](http://danger.systems/guides/troubleshooting.html)
