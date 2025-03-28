require 'uri'
require 'yaml'
require 'fileutils'
require_relative '../../.dangerfile/policy_parser'


pp = PolicyParser.new
pt_files = Dir.glob('./**/*\.pt').select { |e| File.file? e }
all_pts = []
optimization_pts = []
pt_stats = {
  total_count: 0,
  optimization_count: 0,
  categories: {},
  providers: {},
  services: {},
  policy_sets: {}
}
if (pt_files.length != 0)
  pt_files.each do |file|
    ## Begin Policy Exclusions ##
    # Exclude Policies that have publish: "false" in the metadata
    if File.open(file).grep(/publish: \"false\"/).length then next end

    # Exclude Meta Parent Policies
    if file.include?("meta_parent") then next end
    ## End Policy Exclusions ##

    # After all exclusions, we can assume the policy should be in the output
    # Parse the policy from string to object
    pp.parse(file)

    # Construct the policy hash with just the info we need for the output
    p = {file: file, name: pp.parsed_name, category: pp.parsed_category, provider: pp.parsed_info[:provider], service: pp.parsed_info[:service], policy_set: pp.parsed_info[:policy_set], recommendation_type: pp.parsed_info[:recommendation_type]}

    ## Check that all keys/values are not nil
    p.each do |key, value|
      if value.nil? then p[key] = "" end
    end

    # Check if the pt_stats counters have been initialized yet
    # If not, initialize them with count starting at 0
    if pt_stats[:categories][p[:category]].nil? then pt_stats[:categories][p[:category]] = 0 end
    if pt_stats[:providers][p[:provider]].nil? then pt_stats[:providers][p[:provider]] = 0 end
    if pt_stats[:services][p[:service]].nil? then pt_stats[:services][p[:service]] = 0 end
    if pt_stats[:policy_sets][p[:policy_set]].nil? then pt_stats[:policy_sets][p[:policy_set]] = 0 end

    # Increment the stats for the policy
    pt_stats[:categories][p[:category]] += 1
    pt_stats[:providers][p[:provider]] += 1
    pt_stats[:services][p[:service]] += 1
    pt_stats[:policy_sets][p[:policy_set]] += 1
    pt_stats[:total_count] += 1

    # Append the policy hash to the list of all policy templates
    all_pts << p

    # Optimization Policies will be listed separately with intent to highlight them
    # Requirements for Optimization Policies:
    # - Must have all required fields and metadata (https://docs.flexera.com/flexera/EN/Automation/CreateRecomendationFromPolicyTemp.htm)
    pt_file = File.open(file)

    if (pt_file.grep(/field \"savings\" do/).length > 0 \
      and p[:provider] != nil and p[:provider].length > 0) then
      # As of April 2023, recommendation_type is a required metadata in the docs,
      # but the policies that generate savings recommendations do not have it.
      # Likely end up this is not required and we do not need this check, but
      # saving it in comment for now until we can confirm
      # and p[:recommendation_type] != nil and (p[:recommendation_type] == "Usage Reduction" or p[:recommendation_type] == "Rate Reduction")
      # Same for this, docs are wrong. Confirmed on 2023-04-12 we have Recommendations with policy_set="" or undefined.
      # and p[:policy_set] != nil and p[:policy_set].length > 0

      # Append the policy hash to the list of policies
      optimization_pts << p
      pt_stats[:optimization_count] += 1
    end
  end
end

# Definition to sort the hash object of pt_stats recursively
# Minimizes diff between runs, which makes code review easier
def sort_hash_recursively(stats)
  stats.keys.sort.each do |key|
    if stats[key].is_a?(Hash)
      stats[key] = sort_hash_recursively(stats[key])
    end
  end
  return stats.sort.to_h
end
pt_stats = sort_hash_recursively(pt_stats)

# Construct the output
puts "<!--"
puts "  This Table of Contents section is generated by tools/readme_policy_table_of_contents/generate_readme_policy_table_of_contents.rb"
puts "  Do not edit this section manually"
puts "-->"
puts ""
puts "### Categories"
puts ""
puts "- [Optimization](#policy-templates-for-optimization)"
pt_stats[:categories].sort.each do |category,index|
  puts "- [#{category}](#policy-templates-for-#{category.downcase.gsub(" ","-")})"
end
puts ""

puts "### Policy Templates for Optimization"
puts ""
puts "These templates can generate savings estimates for your environment."
puts ""
# To make the list easier to format, group the policies by provider
optimization_pts_grouped = optimization_pts.group_by { |h| h[:provider] }
# For each provider, print the provider and list of policies
optimization_pts_grouped.sort.each do |provider, pts|
  puts "#### #{provider}"
  puts ""
  pts.sort_by{|pt| pt[:name]}.each do |pt|
    dirname = File.dirname(pt[:file])
    puts "- [#{pt[:name]}](#{dirname})"
  end
  puts ""
end

# Output Table of Contents
# Structure is:
# - Category
#   - Provider
#     - Service
#       - Policy Template
# To make the list easier to format, group the policies by provider
category_pts = all_pts.group_by { |h| h[:category] }
# For each group of policies for each Category
category_pts.sort.each do |category, c_pts|
  puts "### Policy Templates for #{category}"
  puts ""
  provider_pts = c_pts.group_by { |h| h[:provider] }
  # For each group of policies for each Provider
  provider_pts.sort.each do |provider, p_pts|
    if provider.length > 0 then
      puts "#### #{provider}"
      puts ""
    end
    service_pts = p_pts.group_by { |h| h[:service] }
    service_pts.sort.each do |service, s_pts|
      if service.length > 0 then
        puts "- #{service}"
        puts ""
      end
      # For each group of policies for each Service
      s_pts.sort_by{|pt| pt[:name]}.each do |pt|
        if pt[:name].length > 0 then
          dirname = File.dirname(pt[:file])
          # Avoid MD005 Inconsistent indentation for list items at the same level
          # If the Service is undefined, then the list item should not be indented
          spacing = ""
          if service.length > 0 then spacing = "  " end
          # Print the policy template name and link to directory
          puts "#{spacing}- [#{pt[:name]}](#{dirname})"
        end
      end
      puts ""
    end
  end
end

puts "<!-- Begin Policy Template Stats -->"
puts "<!--"
puts pt_stats.to_yaml
puts "-->"
puts "<!-- End Policy Template Stats -->"
puts ""
