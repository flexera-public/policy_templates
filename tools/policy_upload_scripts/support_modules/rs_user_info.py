# Helper function to get user email from access_token
import requests,json

def rs_user_email(shard, access_token):
    cm_base_url = "https://moo-93.test.rightscale.com".format(shard)
    cm_headers = {
      "X-API-Version" : "1.5",
      "Authorization" : "Bearer {}".format(access_token)
    }
    
    # First get the user's href
    session_url = cm_base_url+"/api/sessions"
    body = {
        "view" : "whoami"
    }
    my_session = requests.get(session_url, headers=cm_headers, data=body)
    my_session_json = json.loads(my_session.text)
    for link in my_session_json["links"]:
        if link["rel"] == "user":
            my_user_href = link["href"]
            
    # Now get the user's email using the user's href
    my_user_info = requests.get(cm_base_url+my_user_href, headers=cm_headers)
    my_user_info_json = json.loads(my_user_info.text)
    user_email = my_user_info_json["email"]
    return user_email
        