# Flexera Automation CloudFormation Template

## Overview

Template to create a CloudFormation Stack with IAM Role and Permission Policy resources required by [Flexera Automation](https://docs.flexera.com/flexera/EN/Automation/AutomationGS.htm).

## Usage

The CloudFormation Template can be deployed to multiple accounts (as a CloudFormation StackSet) or to a single account (as a CloudFormation Stack).

---

### Create StackSet (Multiple Accounts)

AWS CloudFormation StackSets extends the capability of stacks by enabling you to create, update, or delete stacks across multiple accounts with a single operation.

See [AWS Docs > CloudFormation > Working with StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) for more information.

#### **Recommended:** Create *CloudFormation StackSet* with AWS Console

<details>
<summary><b><i>Click to expand instructions</i>: Create <i>CloudFormation StackSet</i> with AWS Console</b></summary>

> <i>**Note**: The following steps are very closely aligned with AWS Official Docs here:</i>
>
> [AWS Docs > CloudFormation > Create a stack set with service-managed permissions using the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html#stacksets-orgs-associate-stackset-with-org)

As you follow the official docs, you can use the recommended configurations below.

 - Under **Permissions**, choose **Service-managed permissions**

   > If trusted access with AWS Organizations is disabled, a banner displays. Trusted access is required to create or update a stack set with service-managed permissions. Only the administrator in the organization's management account has permissions to [manage trusted access](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.html)

 - Under **Prepare template**, choose **Template is ready**.

 - Under **Specify template**, provide the template S3 URL:

   <https://flexera-cloudformation-public.s3.us-east-2.amazonaws.com/FlexeraAutomationPolicies_latest.template>

   > It's recommended to use an official release for Production use-cases (i.e. *vX.Y.Z*).  All official releases can be found under [releases/](./releases/) folder and are published to  `https://flexera-cloudformation-public.s3.us-east-2.amazonaws.com/FlexeraAutomationPolicies_vX.Y.Z.template`. An example of an release template S3 URL:
   >
   > **https://flexera-cloudformation-public.s3.us-east-2.amazonaws.com/FlexeraAutomationPolicies_v0.1.1.template**

 - On the **Specify StackSet details** page, provide a name for the stack set, specify *Flexera Organization ID* and any other parameters, and then choose **Next**.

   > Naming the Stack Name the same value as *IAM Role Name* parameter is recommended.
   >
   > For example, if *IAM Role Name* parameter is `FlexeraAutomationPolicies-Org12345`, then the recommended StackSet name is `FlexeraAutomationPolicies-Org12345`.

 - On the **Configure StackSet options** page, under **Tags**, specify any tags to apply to resources in your stack.  This is optional. The resources created by the template do not have any cost associated and so the need for tags may only apply for certain use-cases.

 - For **Execution configuration**, choose **Active** so that StackSets performs non-conflicting operations concurrently and queues conflicting operations.

 - On the **Set deployment options** page, under Deployment targets, we recommend choosing **Deploy to organization** to deploy to all accounts in your organization.

 - On the **Auto-deployment options**, under **Automatic deployment**, `Enabled` is recommended to automatically deploy to new accounts added to organization or target OUs in the future.

 - If you enabled automatic deployment, under **Account removal behavior**, `Delete stacks` recommended to remove access when an account is removed from organization or target OUs in the future.

 - Under **Specify regions**, choose only **1 region** to deploy the StackSet to.

   We recommend to use the same region the CloudFormation StackSet is deployed to.

   *This template creates IAM Role and IAM Policy resources, which are "Global" resources.  If this CloudFormation Template is deployed to more than 1 region using the same "IAM Role Name" and "IAM Role Path" parameter value, there will be a conflict trying to create IAM Roles that have the same name.*

 - On the **Deployment options**
   - Under **Maximum concurrent accounts**, choose `Percent` and set field value to `100`.

     Using **100%** maximum concurrent accounts is recommended to increase deployment speed of the Stack instances.
   - Under **Maximum concurrent accounts**, choose `Percent` and set field value to `100`.

     Using **100%** failure tolerance is recommended to allow all account Stack instances to attempt even if one Stack instance fails.

   - Under **Region Concurrency**, choose `Sequential`.

     This ultimately has no affect as the CloudFormation StackSet should be deployed to only 1 region.

  - Click **Next**, and review the summary of the StackSet before continuing.

  - At bottom, under **Capabilities**, check the box next to `I acknowledge that AWS CloudFormation might create IAM resources with custom names` and click **Submit** button to create the StackSet

    This acknowledgement is required because AWS CloudFormation will create an IAM Role and an IAM Policy (as expected).

  - Allow Stack instances to deploy and get to *"Current"* Status.  If any fail, you can review the details of the failed Stack instances and take action as needed.

  - Construct **IAM Role ARN** for AWS STS Credential Setup in Flexera Automation

    The *IAM Role ARN* is the ARN of the IAM Role created by the CloudFormation Template and is needed when creating the [AWS STS Credential in Flexera Automation](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm).  You only need to create **1** AWS STS Credential in Flexera Automation for each StackSet that is created because all IAM Roles created by the StackSet will have the same name and can leverage [AWS STS Multi-Account Credential Usage](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1136870).

    The CloudFormation Template Outputs are not visible at the StackSet level, and instead we recommend constructing the IAM Role ARN using the following:

    `arn:aws:iam::<AWS Account ID>:role/<IAM Role Name>`

     - `<AWS Account ID>` is the AWS Account ID of the account the CloudFormation Stack instance has been deployed to.
     - `<IAM Role Name>` is the value of the *IAM Role Name* parameter provided to the CloudFormation StackSet.

    For example, if the Stack instance was depoyed to AWS Account `123456789012` and the *IAM Role Name* parameter was `FlexeraAutomationPolicies-Org12345`, then the IAM Role ARN to input in Flexera Platform would be `arn:aws:iam::123456789012:role/FlexeraAutomationPolicies-Org12345`.

    **See [Flexera Docs > Automation > AWS STS Multi-Account Credential Usage](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1136870) for more information.**

</details>

<!-- TODO

#### <i>Alternatives to create CloudFormation StackSet</i>:

<details>
<summary><b><i>Click to expand instructions</i>: Create <i>CloudFormation StackSet</i> with AWS CLI</b></summary>

##### Prerequisites

 - **Root ID** (`r-abcd` -- used to deploy to all existing/new accounts) or **Org Unit (OU) ID** (`ou-abcd-zyxwvuts` -- to deploy to subset of accounts)

</details>

-->

---

### Create Stack (Single Account)

If you do not have an AWS Organization setup, or you prefer to deploy to a single account, then you can use the CloudFormation Template to create a CloudFormation Stack.

#### **Recommended:** Create <i>CloudFormation Stack</i> with AWS Console using "Quick-create" link

  - [Quick-create with Default Permissions (Read Only)](https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/quickcreate?templateUrl=https://flexera-cloudformation-public.s3.us-east-2.amazonaws.com/FlexeraAutomationPolicies_latest.template&stackName=FlexeraAutomationAccessRole)

  - [Quick-create with Read and Take Action Permissions](https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/quickcreate?templateUrl=https://flexera-cloudformation-public.s3.us-east-2.amazonaws.com/FlexeraAutomationPolicies_latest.template&stackName=FlexeraAutomationAccessRole&param_paramFlexeraOrgId=&param_paramFlexeraZone=app.flexera.com&param_paramPermsAWSOldSnapshots=Read%20and%20Take%20Action&param_paramPermsAWSUnusedIPAddresses=Read%20and%20Take%20Action&param_paramPermsAWSUnusedVolumes=Read%20and%20Take%20Action)

#### <i>Alternatives to create CloudFormation Stack</i>:

<details>
<summary><i>Click to expand instructions</i>: Create <i>CloudFormation Stack</i> with AWS CLI</summary>

```sh
# Create Stack using CloudFormation Templates Parameter Default Values
aws --region us-east-2 cloudformation create-stack \
  --template-url https://flexera-cloudformation-public.s3.us-east-2.amazonaws.com/FlexeraAutomationPolicies_latest.template \
  --stack-name FlexeraAutomationAccessRole \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameters ParameterKey=paramFlexeraOrgId,ParameterValue=12345
```

</details>

<details>
<summary><i>Click to expand instructions</i>: Create <i>CloudFormation Stack</i> with Terraform</summary>

```terraform
resource "aws_cloudformation_stack" "FlexeraAutomationAccessRole" {
  name         = "FlexeraAutomationAccessRole"
  template_url = "https://flexera-cloudformation-public.s3.us-east-2.amazonaws.com/FlexeraAutomationPolicies_latest.template"

  parameters = {
    paramFlexeraOrgId = "12345"
  }

  capabilities = [
    "CAPABILITY_NAMED_IAM", # Required to create IAM Role
  ]

}
```

</details>

---

## For Maintainers

New releases are created by copying the latest version of template to `releases/` and appending a version number (using [Semantic Versioning](https://semver.org/) strategies).  Files under `releases/` should not be modified once they are merged and committed to default branch.

Publishing releases and latest Template files to S3 is handled by GitHub Actions workflow [
Publish CloudFormation Templates
](../../.github/workflows/cfn-publish.yaml) and triggered when [Test CloudFormation Templates](../../.github/workflows/cfn-test.yaml) finishes successfully after commit to the default branch.
