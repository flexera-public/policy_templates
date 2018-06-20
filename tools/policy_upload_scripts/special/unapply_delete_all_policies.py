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

print "THIS SCRIPT TERMINATES ALL APPLIED POLICIES IN THE ORG AND DELETES ALL UPLOADED POLICIES FROM ORG, {}".format(org)
try:
    wanna = input("IF YOU WANT TO CONTINUE, ENTER \"CONTINUE\" (with double quotes and all): ") 
    if wanna != "CONTINUE":
        print "Processing stopped."
        exit(10)
except NameError:
    print "Processing stopped"
    exit(10)

# Base URLs for below
cm_base_url = "https://us-{}.rightscale.com".format(shard)
gov_endpoint = "https://governance-{}.rightscale.com".format(shard)

# Get all the accounts in the org
grs_headers = {
  "X-API-Version" : "2.0",
  "Authorization" : "Bearer {}".format(access_token),
  "content-type" : "application/json"
}
grs_url = cm_base_url + "/grs/orgs/{}/projects".format(org)
accounts = requests.get(grs_url, headers=grs_headers)
accounts_json = json.loads(accounts.text)

# For each account:
#   Get the applied templates and terminate them
#   Get the uploaded templates and delete them
    
### Upload the policy template
gov_headers = {
  "API-Version" : "1.0",
  "Authorization" : "Bearer {}".format(access_token),
  "content-type" : "application/json"
}

for account in accounts_json:
    account_id = account["id"]
    print "Terminating all applied policies in account, {}.".format(account_id) 
    gov_base_url = "{}/api/governance/projects/{}".format(gov_endpoint,account_id)
    applied_policies = requests.get(gov_base_url+"/applied_policies", headers=gov_headers) 
    applied_policies = json.loads(applied_policies.text)
    try:
        for applied_policy in applied_policies["items"]:
            pol_href = applied_policy["href"]
            # terminate applied policy
            print "Terminating: {}".format(pol_href)
            term_resp = requests.delete(gov_endpoint+pol_href, headers=gov_headers)
    except KeyError:
        print "No applied policies found in account, {}.".format(account_id)
        
    print ""
    print "Deleting all uploaded policies in account, {}.".format(account_id) 
    uploaded_policies = requests.get(gov_base_url+"/policy_templates", headers=gov_headers) 
    uploaded_policies = json.loads(uploaded_policies.text)
    try:
        for uploaded_policy in uploaded_policies["items"]:
            pol_href = uploaded_policy["href"]
            print "Deleting: {}".format(pol_href)
            del_resp = requests.delete(gov_endpoint+pol_href, headers=gov_headers)
    except KeyError:
        print "No uploaded policies found in account, {}.".format(account_id)
        
    print ""
    print ""
        