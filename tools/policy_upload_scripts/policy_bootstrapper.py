#!/usr/bin/env python
#
# Boostraps the "policy sync" policy to all accounts in the user-provided organization.
# See https://github.com/rightscale/policy_templates/tree/master/tools/policy_sync
# 
# Script Function:
# - Find all the accounts in the given organization.
# - Upload and apply the "policy sync" policy to all the accounts.
# 
import requests,json,argparse,getpass,sys,operator
sys.path.insert(0, "./support_modules")
import rs_auth,rs_user_info,rs_account_info

### User inputs and generation of access_token for subsequent API calls ###
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--org', required=True)
parser.add_argument('-r', '--refresh_token', help='RightScale Refresh Token with Enterprise_Manager role. Not used if using username/password authentication.')
parser.add_argument('-u', '--username', help='RightScale username with Enterprise_Manager role. Not used if using refresh_token authentication. Will prompt for password.')
parser.add_argument('-a', '--account', help='Only needed if using username/password authentication.')
args = parser.parse_args()

# Gather up the inputs
org = args.org
refresh_token = args.refresh_token
username = args.username
account_id = args.account

# Synch Policy Template info used below
policy_synch_policy_name = "Policy Template Synchronization Policy Template"
policy_synch_template_uri = "/tools/policy_sync/policy_sync.pt"

if refresh_token is None:
    if username is None:
        print "Need to provide refresh token or username and account ID."
        exit(1) 
    else:
        if account_id is None:
            print "For basic authentication, a RightScale account ID needs to be provided to which you have enterprise_manager role."
            exit(1)
        password = getpass.getpass()
        print "Authenticating to RightScale ..."
        auth_info = rs_auth.rs_basic_auth(account_id, username, password)
        using_basic_auth = True
else:
    print "Authenticating to RightScale ..."
    auth_info = rs_auth.rs_oauth(refresh_token)
    using_basic_auth = False

access_token = auth_info["access_token"]
shard = auth_info["shard"]

# Base URLs for below
cm_base_url = "https://us-{}.rightscale.com".format(shard)
git_base_url = "https://raw.githubusercontent.com/rightscale/policy_templates/master"

# Get the RightScale username (i.e. email address) for the user whose refresh token or creds were used
user_email = rs_user_info.rs_user_email(shard,access_token) 

# Get all the accounts in the org
grs_headers = {
  "X-API-Version" : "2.0",
  "Authorization" : "Bearer {}".format(access_token),
  "content-type" : "application/json"
}
grs_url = cm_base_url + "/grs/orgs/{}/projects".format(org)
accounts = requests.get(grs_url, headers=grs_headers)
accounts_json = json.loads(accounts.text)
# If the organization has a mix of accounts in different shards, we will have to re-authenticate to the new shard
# So sort the accounts such that accounts in the same shard are grouped together to avoid unnecessary authentications.
accounts_json.sort(key=lambda e: e["legacy"]["account_url"]) 
    
### Get the policy template from github
pol_template_url = git_base_url + policy_synch_template_uri
git_file = requests.get(pol_template_url)
git_file = git_file.text

### Upload the policy template
gov_headers = {
  "API-Version" : "1.0",
  "Authorization" : "Bearer {}".format(access_token),
  "content-type" : "application/json"
}

# get file name from policy template uri path
filename =  policy_synch_template_uri.split("/")[-1]
upload_body = {
	"filename" : filename,
	"source" : git_file
}

gov_host = "governance-{}.rightscale.com".format(shard)
apply_body = {
    "name" : "Policy Synchronization for Account {}".format(account_id),
    "template_href" : "placeholder",
    "dry_run" : False,
    "frequency" : "daily",
    "options" : [
        {
            "name" : "escalate_to",
            "value" : [ user_email ]
        },
        {
           "name" : "param_alert_options",
           "value" : "Email and Upload" 
        },
        {
            "name" : "param_governance_host",
            "value" : gov_host
        },
        {
            "name" : "force_upgrade",
            "value" : 0  
        },
    ]
} 

did_not_complete = False
for account in accounts_json:
    account_id = account["id"]
    account_name = account["name"]
    account_shard = rs_account_info.rs_account_shard(account)
    print "####### Account, {} ({}) #######".format(account_name, account_id)
    if (shard != account_shard):
        if using_basic_auth:
            # Need to re-authenticate against the new account since it is in a different shard
            auth_info = rs_auth.rs_basic_auth(account_id, username, password)
            access_token = auth_info["access_token"]
            shard = auth_info["shard"]
            # Need to reset some values based on the new shard
            gov_host = "governance-{}.rightscale.com".format(shard)
            options = [
                {
                    "name" : "escalate_to",
                    "value" : [ user_email ]
                },
                {
                    "name" : "param_alert_options",
                    "value" : "Email and Upload" 
                },
                {
                    "name" : "param_governance_host",
                    "value" : gov_host
                },
                {
                    "name" : "force_upgrade",
                    "value" : 0
                }
            ]
            apply_body["options"] = options
        else:
            # If using refresh token, then not much that can be done
            print "**** WARNING WARNING WARNING ****"
            print "This Organization has a mix of accounts across RightScale shards."
            print "You will need to re-run with a refresh token that has enterprise_manager role in an account on shard, {}".format(account_shard)
            print ""
            did_not_complete = True
            continue

    gov_endpoint = "https://governance-{}.rightscale.com".format(shard)
    gov_base_url = "{}/api/governance/projects/{}".format(gov_endpoint,account_id)
    
    # This script will always push the policy synch policy. 
    # So if the policy synch policy is already in the account, terminate it if applied and remove it first. 
    print "Removing old Policy Synchronization Policy from account, {}, if found.".format(account_id)
    # See if the synch policy has been applied and if so, terminate it (them)
    applied_policies = requests.get(gov_base_url+"/applied_policies", headers=gov_headers) 
    applied_policies = json.loads(applied_policies.text)
    try:
        for applied_policy in applied_policies["items"]:
            try: 
                if (applied_policy["policy_template"]["name"] == policy_synch_policy_name):
                    pol_href = applied_policy["href"]
                    # terminate applied policy
                    print "Terminating applied policy, {} (href: {})".format(applied_policy["policy_template"]["name"],pol_href)
                    term_resp = requests.delete(gov_endpoint+pol_href, headers=gov_headers)
            except:
                print "Problem terminating policy"
    except:
        # no-op
        print "No applied policies found."

    # See if the synch policy has been uploaded and if so remove it - clean slate, baby
    uploaded_policies = requests.get(gov_base_url+"/policy_templates", headers=gov_headers) 
    uploaded_policies = json.loads(uploaded_policies.text)
    try:
        for uploaded_policy in uploaded_policies["items"]:
            try:
                if (uploaded_policy["name"] == policy_synch_policy_name):
                    pol_href = uploaded_policy["href"]
                    print "Deleting: uploaded policy, {} (href: {})".format(uploaded_policy["name"],pol_href)
                    del_resp = requests.delete(gov_endpoint+pol_href, headers=gov_headers)
            except:
                print "Problem deleting policy"
    except:
        # no-op
        print "No uploaded policies found."
    
    # Now that we have a clean slate, upload and apply the latest version of the policy synch template.
    print "Uploading Policy Synchronization Policy to account, {}.".format(account_id) 
    upload_response = requests.post(gov_base_url+"/policy_templates", headers=gov_headers, json=upload_body) 
    upload_response_status_code = upload_response.status_code
    if upload_response_status_code != 200:
        print "Account {}: Policy Sync policy failed to upload. Error Code: {}.".format(account_id, upload_response.status_code)
        if upload_response_status_code == 409:
            print "This is likely a policy template conflict error."
            print "This should not have happened since the policy synch template should have been removed above."
            print "Check if the \""+policy_synch_policy_name+"\" policy has already been uplaoded."
        else:
            print "Error Response Body: {}".format(upload_response.text)
            did_not_complete = True
    else:
        # Get the info for the uploaded template
        upload_response_json = json.loads(upload_response.text)
        template_href = upload_response_json["href"]
    
        # Now apply the policy 
        apply_body["template_href"] = template_href
        print "Applying Policy Synchronization policy to account, {}.".format(account_id)
        apply_response = requests.post(gov_base_url+"/applied_policies", headers=gov_headers, json=apply_body)
       
        apply_status_code = apply_response.status_code
        if apply_status_code != 200:
            print "Error applying the policy file in account {}.".format(account_id) 
            print "Error status code: {}; Error response: {}".format(apply_status_code, apply_response.text)
            did_not_complete = True
        else:
            print ""
        
if did_not_complete:
    print "################################"
    print "Check output above - some accounts did not get set up as expected."
    print "################################" 
        