var ds_with_access_link = [];
var base_url="https://" + rs_cm_host + "/acct/" + rs_project_id
var ds_original_dataset = [];
var ds_cm16_dataset = [];

for ( var i = 0; i < ds_original_dataset.length; i++ ) {
  if ( ds_cm16_dataset.length > 0 ) {
    // Assume Instance Type
    for ( var n = 0; n < ds_cm16_dataset.length; n++ ) {
      if ( ds_original_dataset[i]["href"] == ds_cm16_dataset[n]["href"] ){
          var data = ds_original_dataset[i]["href"].split("/")
          $cloud_id = $data[3]
          ds_original_dataset[i]["server_access_link"] = base_url.concat("/clouds/",$cloud_id,"/instances/",ds_cm16_dataset[n]["legacy_id"])
      }
    }
  } else {
    // Assume Volume Type
    ds_original_dataset[i]["server_access_link"] = base_url.concat(ds_original_dataset[i]["href"])
  }
}

ds_with_access_link = ds_original_dataset