#!/usr/bin/env python
#
# Boostraps the "policy sync" policy to all accounts in the user-provided organization.
# See https://github.com/rightscale/policy_templates/tree/master/tools/policy_sync
# 
# Script Function:
# - Find all the accounts in the given organization.
# - Upload and apply the "policy sync" policy to all the accounts.
# 
import requests,json,argparse,getpass,sys
sys.path.insert(0, "../support_modules")
sys.path.insert(0, "./support_modules")
import rs_auth,rs_account_info

### User inputs and generation of access_token for subsequent API calls ###
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--org', required=True)
parser.add_argument('-r', '--refresh_token')
parser.add_argument('-u', '--username')
parser.add_argument('-a', '--account')
args = parser.parse_args()

# Gather up the inputs
org = args.org
refresh_token = args.refresh_token
username = args.username
account_id = args.account

print "THIS SCRIPT TERMINATES ALL APPLIED POLICIES IN THE ORG AND DELETES ALL UPLOADED POLICIES FROM ORG, {}".format(org)
try:
    wanna = input("IF YOU WANT TO CONTINUE, ENTER \"CONTINUE\" (with double quotes and all): ") 
    if wanna != "CONTINUE":
        print "Processing stopped."
        exit(10)
except NameError:
    print "Processing stopped"
    exit(10)

if refresh_token is None:
    if username is None:
        print "Need to provide refresh token or username and account ID."
        exit(1) 
    else:
        if account_id is None:
            print "For basic authentication, a RightScale account ID needs to be provided to which you have enterprise_manager role."
            exit(1)
        password = getpass.getpass()
        auth_info = rs_auth.rs_basic_auth(account_id, username, password)
        using_basic_auth = True
else:
    auth_info = rs_auth.rs_oauth(refresh_token)
    using_basic_auth = False

access_token = auth_info["access_token"]
shard = auth_info["shard"]

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
# If the organization has a mix of accounts in different shards, we will have to re-authenticate to the new shard
# So sort the accounts such that accounts in the same shard are grouped together to avoid unnecessary authentications.
accounts_json.sort(key=lambda e: e["legacy"]["account_url"]) 

# For each account:
#   Get the applied templates and terminate them
#   Get the uploaded templates and delete them
    
### Upload the policy template
gov_headers = {
  "API-Version" : "1.0",
  "Authorization" : "Bearer {}".format(access_token),
  "content-type" : "application/json"
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
            gov_endpoint = "https://governance-{}.rightscale.com".format(shard)
        else:
            # If using refresh token, then not much that can be done
            print "**** WARNING WARNING WARNING ****"
            print "This Organization has a mix of accounts across RightScale shards."
            print "You will need to re-run with a refresh token that has enterprise_manager role in an account on shard, {}".format(account_shard)
            print ""
            did_not_complete = True
            continue
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
        
if did_not_complete:
    print "################################"
    print "Check output above - some accounts did not get cleaned up as expected."
    print "################################"