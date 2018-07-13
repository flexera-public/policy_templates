# Policy Upload Scripts

## Prerequisites
* Python 2.7 or later
* Required Python Modules (pip install):
  * requests
  * json
  * argparse
  * getpass
  * sys
  * operator
  
## How to Use
### Step 1: Download the necessary files
#### Method 1: Git clone method
* `git clone https://github.com/rightscale/policy_templates.git`
* `cd policy_templates/tools/policy_upload_scripts`

#### Method 2: Manually copy the files
* Open a browser and go to https://github.com/rightscale/policy_templates/tree/master/tools/policy_upload_scripts
* Click the Download button to download a zipfile of the git repository.
* Unzip the zip file.
* `cd policy_templates-master/tools/policy_upload_scripts`

### Step 2: Test the script
* Execute: `./policy_bootstrapper.py -h` to get help and options.

### Step 3: Upload and Run Policy Synchronization Policy
#### Option 1: All Accounts in a specified Organization
* Example to upload synch policy to all accounts in the given organization: 
  *`./policy_bootstrapper.py -u USERNAME -a ACCOUNT_ID -o ORGANIZTION_ID`
    * Where USERNAME is the RightScale username for a user with enterprise_manager role in the organization.
    * Where ACCOUNT_ID is the account number for one of the accounts in the organization.
    * Where ORGANIZATION_ID is the organization ID to which you want to upload the policy.
  * Enter password when prompted.
   
#### Option 2: Selective Accounts in a specified Organization
* Example to upload synch policy to all accounts in the given organization: 
  *`./policy_bootstrapper.py -u USERNAME -a ACCOUNT_ID -o ORGANIZTION_ID -t ACCOUNT_ID1,ACCOUNT_ID2` 
    * Where USERNAME is the RightScale username for a user with enterprise_manager role in the organization.
    * Where ACCOUNT_ID is the account number for one of the accounts in the organization.
    * Where ORGANIZATION_ID is the organization ID to which you want to upload the policy.
    * Where ACCOUNT_ID1,ACCOUNT_ID2 is a comma-separated list of accounts in the given ORGANIZATION_ID to which you want to limit uploading the policy synchronization policy.
  * Enter password when prompted.

### Step 4: Verify uploaded RightScale pre-built policies
* Navigate to policy management in Governance and verify you see the Policy Templates in the specified account or organization based on your selection above. 

## Cost
This Policy Template does not incur any cloud costs.
