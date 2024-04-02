# Cloud Data Scripts

Scripts to generate various cloud-specific data assets that are stored in `/data`. Most of these scripts generate pricing tables for various types of cloud resources.

## Usage

- Create a new branch and switch to that branch.
- Run the desired script from the root directory of the repository like so: `python3 tools/cloud_data/aws/aws_ec2_pricing.py`
- Run the `git add .` command to add the newly generated files.
- Commit and push the changes and submit a pull request.

## Automated Workflow

There are automated workflows that run once per week for each script and automatically submit a pull request with the updated file. This is to ensure that the resulting data assets are maintained and up to date. The new PR can be approved by the Policy Template Maintainers.

- [AWS EC2 Pricing Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-aws-ec2-pricing-json.yaml)
- [AWS RDS Pricing Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-aws-rds-pricing-json.yaml)
- [Azure VM Pricing Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-azure-vm-pricing-json.yaml)
- [Azure MD Pricing Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-azure-md-pricing-json.yaml)
