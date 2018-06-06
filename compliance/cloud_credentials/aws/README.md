### AWS Credentials Update Policy

**What it does**
This Policy Template is used to automatically update the AWS IAM keys used to connect the RightScale account to the applicable AWS account.
When applied, the policy updates the credentials immediately and then updates the credentials thereafter every X number of days where X is specified by the user.

## Functional Details
This policy performs the following actions:
- Create a new set of security credentials for the user-specified AWS IAM user.
- Update the AWS cloud connections to use the new keys.
- Update RightScale Credentials, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY with the new IAM user keys.
- Delete the IAM user's former keys from AWS.

### Caveats and Prerequisites
The policy assumes the following to be true:
- The AWS IAM user used to connect to RightScale is DEDICATED to the RightScale connection. 
  - This requirement is because the policy will get rid of an IAM key if it runs up against a quota issue.
  - This requirement can be circumvented if the IAM user has no quota for the number of keys it can create.
- The AWS IAM user used to connect RightScale to AWS has permissions to create and delete its keys.
- There are RightScale credentials defined in RightScale named AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY that contain the IAM user's currently active keys.
  - This would have been automatically done by RightScale when originally connecting the AWS IAM user to RightScale.

If the policy runs up against a quota for the number of keys that can be active, the policy will delete credentials for the IAM user that are not currenlty being used to connect RightScale to AWS.

### Possible Future Enhancements
- Policy accepts user inputs related to the keys to use for managing the keys used to connect to AWS. 
  - This would enable the use case where RS is connected to AWS with lesser permissions but there is still a need to rotate those keys.

## Supported Clouds
The following clouds are supported: 
- AWS

**Cost**
This Policy Template does not incur any cloud costs.