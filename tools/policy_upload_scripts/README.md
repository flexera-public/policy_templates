# Policy Upload Scripts

## Scripts/Modules
### policy_bootstrapper.py
Provides an easy way to push the official set of RightScale policies to all accounts in an organization.
When invoked, the script uploads and applies the "Policy Template Synchronization" policy template to 
ALL accounts in the specified organization.

The "Policy Template Synchronization" policy template is a meta policy that uploads all the offical set of RightScale policies to the account
it is applied in.
So the policy_bootstrapper.py script provides an easy way to upload and apply this policy synch policy to all the accounts in the specified organization.

#### How to Use
* Git clone or copy the python files found here.
* ./policy_bootstrapper.py -h 
  * for help and options
* Example call:
  * ./policy_bootstrapper.py --refresh_token xxxxxxxx --org 1234
    * This will upload the policy synch policy to all accounts in org, 1234 and set up email notifications for the user that owns the given refresh token

### rs_auth.py
A helper module for RightScale authentication. It will cycle through the RightScale shards to authenticate and
if successful, it retuns the discovered shard and access token.

### rs_user_info.py
A helper module used to find the RightScale username (i.e. email address) associated with a given authenticated access token.
This is handy when applying policy templates since it is useful to set up an email recipient.

  
## Prerequisites
* Python 2.7 or later

## Cost
This Policy Template does not incur any cloud costs.