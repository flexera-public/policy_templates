### RIGHTSCALE AUTHENTICATION ###
import requests,json

# Oauth authentication using RightScale Refresh Token
def rs_oauth(refresh_token):
    data = {
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }
    headers = {"X-Api-Version": "1.5"}
    headers["content-type"] = "application/json"

    shards = ["3", "4", "10"]
    shard_idx = 0
    shard_found = False
    while (shard_found == False) and (shard_idx < 3): 
        shard = shards[shard_idx]
        shard_idx = shard_idx + 1
        try: 
            uri = "https://us-{}.rightscale.com/api/oauth2".format(shard)
            response = requests.post(uri, headers=headers, data=json.dumps(data))
            response_json_obj = json.loads(response.text)
            response_json_obj["access_token"]
            access_token = response_json_obj["access_token"]
            shard_found = True
        except: 
            shard_found = False
    
    if not shard_found:
        print "Invalid authentication. Check your credentials."
        exit(1)

    return { "access_token": access_token, "shard": shard }

    
# Basic authentication using RightScale username and password
def rs_basic_auth(account_id, username, password):
    data = {
        "email": username,
        "password": password,
        "account_href": "/api/accounts/{}".format(account_id)
    }
    headers = {"X-Api-Version": "1.5"}
    headers["content-type"] = "application/json"

    shards = ["3", "4", "10"]
    shard_idx = 0
    shard_found = False
    while (shard_found == False) and (shard_idx < 3): 
        shard = shards[shard_idx]
        shard_idx = shard_idx + 1
        uri = "https://us-{}.rightscale.com/api/sessions".format(shard)
        try:
            response = requests.post(uri, headers=headers, data=json.dumps(data))
        except: 
            shard_found = False
        
        if response.status_code == 204:
            shard_found = True
            set_cookie = response.headers["Set-Cookie"]
            cookie = set_cookie.split(";")[0]
            access_token = cookie.split("=")[-1]
    
    if not shard_found:
        print "Invalid authentication. Check your credentials."
        exit(1)
        
    return { "access_token": access_token, "shard": shard }