# Agent Reference Data

This directory contains manually-maintained reference material used by the `policy-dev` agent (`.github/agents/policy-dev.agent.md`) when creating and reviewing policy templates.

## Manually Maintained Files

### code_examples.txt

**Description:** The canonical DSL and JavaScript code examples for the Flexera Policy Template Language, covering credentials, pagination, datasource patterns, common JavaScript patterns (parameter sanitization, tag/region/subscription/project filtering), the policy block, the AWS region error-reporting pattern, the final transform/cost template conventions, escalations, cloud workflow actions, Flexera API boilerplate datasources, the Meta Policy canonical block, provider boilerplate datasources, standard parameter conventions, and statistics category parameters.

`.github/agents/policy-dev.agent.md` references this file by section title instead of embedding the code inline, so the examples only need to be updated in one place. Each section is introduced by a `##` or `###` header whose title exactly matches the corresponding header in `policy-dev.agent.md`, so the two files can be cross-referenced by title. This file intentionally contains code only (with brief inline comments where needed to distinguish variants); the prose explanations of when/why/how to use each pattern live in `policy-dev.agent.md`.

**Example:**

```text
### Credentials

credentials "auth_aws" do
  schemes "aws", "aws_sts"
  label "AWS"
  description "Select the AWS Credential from the list"
  tags "provider=aws"
  aws_account_number $param_aws_account_number  # for Meta Policy cross-account support
end
```
