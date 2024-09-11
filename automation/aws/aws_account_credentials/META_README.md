# Meta Parent: AWS Account Credentials

## What It Does

This meta parent policy template consolidates the results of all of the associated child policy templates to provide a single report of all AWS accounts in the Flexera organization. Each AWS account in the consolidated incident report will contain a status field with one of the following values:

- *Passed* - The AWS cross-account role exists and the child applied policy was able to successfully make a GetCallerIdentity request to AWS STS with it.
- *Failed* - Either the AWS cross-account role does not exist or is not configured correctly, resulting in failure when making a GetCallerIdentity request to AWS STS with it.
- *Unknown* - The child applied policy has not yet been created or completed execution, and as a result, the status of the AWS cross-account role is unknown. This is most commonly seen soon after applying the meta parent policy and should mostly disappear after 24 hours.

__NOTE: This meta parent policy template is not automatically generated and is customized for this specific use case. It needs to be manually updated and maintained whenever the child policy template is updated.__
