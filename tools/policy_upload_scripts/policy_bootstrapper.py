#!/usr/bin/env python
#
# Uploads and applies the "upload policy" policy to all accounts in the user-provided organization.
# See 
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

refresh_token = args.refresh_token
username = args.username
shard = args.shard
account_id = args.account
pol_template_uri = args.policy_template

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
    
### Get the policy template
base_git_url = "https://raw.githubusercontent.com/rightscale/policy_templates/master"
pol_template_url = base_git_url + pol_template_uri
git_file = requests.get(pol_template_url)
git_file = git_file.text
### /GET POLICY TEMPLATE FILE ###


### UPLOAD POLICY TEMPLATE ###
gov_url = "https://governance-"+shard+".rightscale.com/api/governance/projects/"+account_id+"/policy_templates"

headers = {
  "API-Version" : "1.0",
  "Authorization" : "Bearer {}".format(access_token)
}

# get file name from policy template uri path
filename =  pol_template_uri.split("/")[-1]
body = {
	"filename" : filename,
	"source" : git_file
}
r = requests.post(gov_url, headers=headers, json=body) 
### /UPLOADE POLICY TEMPLATE ###

print r.text




