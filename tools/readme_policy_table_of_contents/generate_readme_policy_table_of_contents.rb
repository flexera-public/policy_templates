require 'uri'
require 'yaml'
require_relative '../lib/policy_parser'


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
    # Exclude Turbonomic policies
    if file.include? "turbonomic" then next end

    # Exclude Policies that have publish: "false" in the metadata
    if open(file).grep(/publish: \"false\"/).length > 0 then next end

    # Exclude Policies that are no longer being updated
    if open(file).grep(/This policy is no longer being updated/).length > 0 then next end

    # After all exclusions, we can assume the policy should be in the output
    # Parse the policy from string to object
    pp.parse(file)

    # Construct the policy hash with just the info we need for the output
    p = {file: file, name: pp.parsed_name, category: pp.parsed_category, provider: pp.parsed_info[:provider], service: pp.parsed_info[:service], policy_set: pp.parsed_info[:policy_set]}
    if pt_stats[:categories][p[:category]].nil? then pt_stats[:categories][p[:category]] = 0 end
    if pt_stats[:providers][p[:provider]].nil? then pt_stats[:providers][p[:provider]] = 0 end
    if pt_stats[:services][p[:service]].nil? then pt_stats[:services][p[:service]] = 0 end
    if pt_stats[:policy_sets][p[:policy_set]].nil? then pt_stats[:policy_sets][p[:policy_set]] = 0 end
    pt_stats[:categories][p[:category]] += 1
    pt_stats[:providers][p[:provider]] += 1
    pt_stats[:services][p[:service]] += 1
    pt_stats[:policy_sets][p[:policy_set]] += 1
    pt_stats[:total_count] += 1


    # Append the policy hash to the list of all policy templates
    all_pts << p

    # Aggregate Policies that have a savings field in result
    # These will have special attention brought to them to increase visibility
    if open(file).grep(/field \"savings\" do/).length > 0 then
      # Append the policy hash to the list of policies
      optimization_pts << p
      pt_stats[:optimization_count] += 1
    end
  end
end

# Construct the output
puts "### Categories"
puts ""
puts "- [Optimization](#policy-templates-for-optimization)"
pt_stats[:categories].sort.each do |category,index|
  puts "- [#{category}](#policy-templates-for-#{category.downcase.gsub(" ","-")})"
end
puts ""

puts "### Policy Templates for Optimization"
puts "These templates can generate savings estimates for your environment."
puts ""
# To make the list easier to format, group the policies by provider
optimization_pts_grouped = optimization_pts.group_by { |h| h[:provider] }
# For each provider, print the provider and list of policies
optimization_pts_grouped.sort.each do |provider, pts|
  puts "#### #{provider}"
  puts ""
  pts.each do |pt|
    dirname = File.dirname(pt[:file])
    puts "- [#{pt[:name]}](#{dirname})"
  end
  puts ""
end

# To make the list easier to format, group the policies by provider
category_pts = all_pts.group_by { |h| h[:category] }
category_pts.sort.each do |category, c_pts|
  puts "### Policy Templates for #{category}"
  puts ""
  provider_pts = c_pts.group_by { |h| h[:provider] }
  provider_pts.sort.each do |provider, p_pts|
    puts "#### #{provider}"
    puts ""
    service_pts = p_pts.group_by { |h| h[:service] }
    service_pts.sort.each do |service, s_pts|
      if service.length > 0 then
        puts "- #{service}"
        puts ""
      end
      s_pts.each do |pt|
        if pt[:name].length > 0 then
          dirname = File.dirname(pt[:file])
          puts "  - [#{pt[:name]}](#{dirname})"
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

