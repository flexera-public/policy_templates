script "filter_resources", type: "javascript" do
  parameters "resources","resource_tags","clouds" ,"param_tag_keys"
  result "filtered_resources"
  code <<-EOS
// This is the list of filtered volumes.
var filtered_resources = [];
var tag_keys_array = param_tag_keys.split(',')
// This is the map of volume href to its tags.
var tags = {};
for (var i = 0; i < resource_tags.length; i++) {
  rt = resource_tags[i]
  for (var j = 0; j < rt['links'].length; j++) {
    link = rt['links'][j]
    if (link['rel'] == 'resource') {
      tags[link['href']] = rt['tags']
    }
  }
}
// Go through all the rsources and filter the ones that don't
// comply with the tag rules.
for (var i = 0; i < resources.length; i++) {
  var res = resources[i]
  var res_tags = []
  // Tags is an array of hashes each with just 'name'. Let's convert
  // them to an array of strings.
  for (var j = 0; j < tags[res['href']].length; j++) {
    res_tags.push(tags[res['href']][j]['name'].split("=")[0])
  }
  // Determines whether this resource is properly tagged
  var bad = false;
  if ( _.intersection(tag_keys_array, res_tags).length != tag_keys_array.length ) {
    bad = true;
  }
  if ( res['type'] === 'volumes'){
    state=res['status']
  } else {
    state=res['state']
  }
  // create cloud_href from resource href
  var split = res['href'].split('/')
  var index = res['href'].indexOf('/'+split[4])
  var cloud_href = res['href'].substring(0,index)
  // create a map of clouds with href key to get type and name
  var cloud_map = {}
  for (var i = 0; i < clouds.length; i++) {
      var cloud = clouds[i]
      cloud_map[cloud['href']]={'type': cloud['type'],'name': cloud['name']}
  }
  // update resource array with resources that are missing tags
  if ( bad ) {
    filtered_resources.push(
    { id: res['id'],
      name: res['name'],
      state: state,
      href: res['href'],
      type: res['type'],
      cloud_name: cloud_map[cloud_href]['name'],
      cloud_type: cloud_map[cloud_href]['type'],
      tags: res_tags,
    }
    )
  }
};
  EOS
end
