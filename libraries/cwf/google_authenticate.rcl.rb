# This library code can be used to authenticate against the google api with cwf actions. 
define google_authenticate() return $access_token do
  #The scope below only counts for devstorage, you will want to change to accomodate your needs. 
  $jwt = {
    iss: cred("GCE_PLUGIN_ACCOUNT"),
    aud:"https://oauth2.googleapis.com/token",
    exp: to_n(strftime(now()+3600, "%s")),
    iat:to_n(strftime(now(), "%s")),
    scope: "https://www.googleapis.com/auth/cloud-platform https://www.googleapis.com/auth/devstorage.read_only"
  }

  $signed_sigurature = jwt_encode("RS256", $jwt, cred("GCE_PLUGIN_PRIVATE_KEY"),{typ:"JWT"})

  $response = http_request({
    verb: 'post',
    href: '/token',
    host: 'oauth2.googleapis.com',
    https: true,
    headers: {
      "content-type": "application/json"
    },
    body:{
      "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",         
      "assertion": $signed_sigurature
    }
  })
  $access_token = $response["body"]["access_token"]
end