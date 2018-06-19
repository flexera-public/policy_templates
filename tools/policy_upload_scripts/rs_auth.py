### RIGHTSCALE AUTHENTICATION ###
import requests,json

# Oauth authentication using RightScale Refresh Token
def rs_oauth(shard, refresh_token):
    uri = "https://us-{}.rightscale.com/api/oauth2".format(shard)
    data = {
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }
    headers = {"X-Api-Version": "1.5"}
    headers["content-type"] = "application/json"
    response = requests.post(uri, headers=headers, data=json.dumps(data))
    response_json_obj = json.loads(response.text)
    try: 
        response_json_obj["access_token"]
    except KeyError:
        print "Invalid authentication."
        print "Response: "
        print response_json_obj
        exit(1)
    access_token = response_json_obj["access_token"]
    return access_token

    
# Basic authentication using RightScale username and password
def rs_basic_auth(shard, account_id, username, password):
    uri = "https://us-{}.rightscale.com/api/sessions".format(shard)
    data = {
        "email": username,
        "password": password,
        "account_href": "/api/accounts/{}".format(account_id)
    }
    headers = {"X-Api-Version": "1.5"}
    headers["content-type"] = "application/json"
    response = requests.post(uri, headers=headers, data=json.dumps(data))
    if response.status_code != 204:
        print "Invalid authentiction."
        print "Status Code: {}".format(response.status_code)
        exit(1)
    set_cookie = response.headers["Set-Cookie"]
    cookie = set_cookie.split(";")[0]
    access_token = cookie.split("=")[-1]
    return access_token