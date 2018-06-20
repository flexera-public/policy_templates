#!/usr/bin/env python
#
# Boostraps the "policy sync" policy to all accounts in the user-provided organization.
# See https://github.com/rightscale/policy_templates/tree/master/operational/policy_sync
# 
# Script Function:
# - Find all the accounts in the given organization.
# - Upload and apply the "policy sync" policy to all the accounts.
# 
import requests,json,argparse,getpass
import rs_auth,rs_user_info

### User inputs and generation of access_token for subsequent API calls ###
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--shard', required=True)
parser.add_argument('-o', '--org', required=True)
parser.add_argument('-r', '--refresh_token')
parser.add_argument('-u', '--username')
parser.add_argument('-a', '--account')
args = parser.parse_args()

# Gather up the inputs
shard = args.shard
org = args.org
refresh_token = args.refresh_token
username = args.username
account_id = args.account

if refresh_token is None:
    if username is None:
        print "Need to provide refresh token or username and account ID."
        exit(1) 
    else:
        if account_id is None:
            print "For basic authentication, a RightScale account ID needs to be provided to which you have enterprise_manager role."
            exit(1)
        password = getpass.getpass()
        access_token = rs_auth.rs_basic_auth(shard, account_id, username, password)
else:
    access_token = rs_auth.rs_oauth(shard,refresh_token)
    
# Base URLs for below
cm_base_url = "https://us-{}.rightscale.com".format(shard)
gov_host = "governance-{}.rightscale.com".format(shard)
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
    
### Get the policy template from github
pol_template_uri = "/operational/policy_sync/policy_sync.pt"
pol_template_url = git_base_url + pol_template_uri
git_file = requests.get(pol_template_url)
git_file = git_file.text

### Upload the policy template
gov_headers = {
  "API-Version" : "1.0",
  "Authorization" : "Bearer {}".format(access_token),
  "content-type" : "application/json"
}

# get file name from policy template uri path
filename =  pol_template_uri.split("/")[-1]
upload_body = {
	"filename" : filename,
	"source" : git_file
}

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
            "value" : 1
        },
    ]
} 


for account in accounts_json:
    account_id = account["id"]
    print "Uploading Policy Synchronization Policy to account, {}.".format(account_id) 
    gov_base_url = "https://{}/api/governance/projects/{}".format(gov_host,account_id)
    upload_response = requests.post(gov_base_url+"/policy_templates", headers=gov_headers, json=upload_body) 
    upload_response_status_code = upload_response.status_code
    if upload_response_status_code != 200:
        print "Account {}: Policy Sync policy failed to upload. Error Code: {}.".format(account_id, upload_response.status_code)
        if upload_response_status_code == 409:
            print "This is likely a policy template conflict error."
            print "Check if the \"Policy Template Synchronization Policy Template\" policy has already been uplaoded."
        print "Error Response Body: {}".format(upload_response.text)
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
        else:
            print "#####################################"
            print ""
        
        
        