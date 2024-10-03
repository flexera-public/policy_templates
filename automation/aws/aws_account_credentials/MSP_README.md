# MSP Report: AWS Account Credentials

## What It Does

This policy template gathers all of the "AWS Account Credentials" incident data from the various child organizations of an MSP organization and provides a consolidated report. This policy template assumes that all of the child organizations have the [Meta Parent: AWS Account Credentials](https://github.com/flexera-public/policy_templates/tree/master/automation/aws/aws_account_credentials/META_README.md) policy template running and working as intended.

## How To Use

1. Upload both the [AWS Account Credentials](https://github.com/flexera-public/policy_templates/tree/master/automation/aws/aws_account_credentials/aws_account_credentials.pt) and [Meta Parent: AWS Account Credentials](https://github.com/flexera-public/policy_templates/tree/master/automation/aws/aws_account_credentials/aws_account_credentials_meta_parent.pt) policy templates to your child organizations. It is recommended that you make this part of your normal onboarding automation.
2. Apply the [Meta Parent: AWS Account Credentials](https://github.com/flexera-public/policy_templates/tree/master/automation/aws/aws_account_credentials/aws_account_credentials_meta_parent.pt) policy template in each child organization. The default parameter options should work in most cases. It is recommended that you make this part of your normal onboarding automation.
3. Upload and apply the [MSP Report: AWS Account Credentials](https://github.com/flexera-public/policy_templates/tree/master/automation/aws/aws_account_credentials/aws_account_credentials_msp.pt) policy template in the parent organization. It will scrape the incidents produced by the above and raise an incident (and, optionally, email this incident) with a consolidated report.
