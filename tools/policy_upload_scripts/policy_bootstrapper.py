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
import rs_auth

### User inputs and generation of access_token for subsequent API calls ###
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--shard', required=True)
parser.add_argument('-r', '--refresh_token')
parser.add_argument('-u', '--username')
parser.add_argument('-a', '--account')
args = parser.parse_args()

# Gather up the inputs
refresh_token = args.refresh_token
username = args.username
shard = args.shard
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
gov_base_url = "https://{}/api/governance/projects/{}".format(gov_host,account_id)
git_base_url = "https://raw.githubusercontent.com/rightscale/policy_templates/master"

# Get authenticated user's username so it can be used when applying the policy for email notifications
headers = {
  "X-API-Version" : "1.5",
  "Authorization" : "Bearer {}".format(access_token)
}

# First get the user's href
session_url = cm_base_url+"/api/sessions"
body = {
    "view" : "whoami"
}
my_session = requests.get(session_url, headers=headers, data=body)
my_session_json = json.loads(my_session.text)
for link in my_session_json["links"]:
    if link["rel"] == "user":
        my_user_href = link["href"]
        
# Now get the user's email using the user's href
my_user_info = requests.get(cm_base_url+my_user_href, headers=headers)
my_user_info_json = json.loads(my_user_info.text)
user_email = my_user_info_json["email"]
    
### Get the policy template from github
pol_template_uri = "/operational/policy_sync/policy_sync.pt"
pol_template_url = git_base_url + pol_template_uri
git_file = requests.get(pol_template_url)
git_file = git_file.text

### Upload the policy template
headers = {
  "API-Version" : "1.0",
  "Authorization" : "Bearer {}".format(access_token),
  "content-type" : "application/json"

}

# get file name from policy template uri path
filename =  pol_template_uri.split("/")[-1]
body = {
	"filename" : filename,
	"source" : git_file
}
upload_response = requests.post(gov_base_url+"/policy_templates", headers=headers, json=body) 

upload_response_status_code = upload_response.status_code
if upload_response_status_code != 200:
    print "Account {}: Policy Sync policy failed to upload. Error Code: {}.".format(account_id, upload_response.status_code)
    if upload_response_status_code == 409:
        print "This is likely a policy template conflict error."
        print "Check if the \"Policy Template Synchronization Policy Template\" policy has already been uplaoded."
else:
    # Get the info for the uploaded template
    upload_response_json = json.loads(upload_response.text)
    template_href = upload_response_json["href"]

    # Now pply the policy 
    body = {
        "name" : "Policy Synchronization for Account {}".format(account_id),
        "template_href" : template_href,
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
    payload = json.dumps(body)
    apply_response = requests.post(gov_base_url+"/applied_policies", headers=headers, data=payload)
    
    print apply_response.status_code
    print apply_response.headers
    print apply_response.text
    

