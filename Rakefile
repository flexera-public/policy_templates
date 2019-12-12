require 'rubygems'
require 'json'
require 'fileutils'
require './tools/lib/policy_parser'

# the list of policies is consumed by the tools/policy_sync/policy_sync.pt
# and the docs.rightscale.com build to generate the policies/user/policy_list.html
# the file is uploaded to S3 during a merge to master deploy step in .travis.yml
desc "Create a list of active policies to be published to the Public Policy Catalog"
task :generate_policy_list do
  FileUtils.mkdir_p 'dist'
  file_list = []
  Dir['**/*.pt'].reject{ |f| f['msp/'] }.each do |file|
    change_log = ::File.join(file.split('/')[0...-1].join('/'),'CHANGELOG.md')
    readme = ::File.join(file.split('/')[0...-1].join('/'),'README.md')
    publish = true

    if !file.match(/test_code/)
      f = File.open(file, "r:bom|utf-8")

      pp = PolicyParser.new
      pp.parse(file)
      
      if pp.parsed_info
        version = pp.parsed_info[:version]
        provider = pp.parsed_info[:provider]
        service = pp.parsed_info[:service]
        policy_set = pp.parsed_info[:policy_set]
        publish = pp.parsed_info[:publish]
        # not all templates have the publish key
        # set these to true,
        if publish.nil? || publish=='true' || publish==true
          publish = true
        else
          publish = false
        end
      end

      # skip policy if the version isn't supplied or if version is '0.0'
      if ! version || version == '0.0' || ! publish
        puts "Skipping #{pp.parsed_name}, policy not published"
        next
      end

      puts "Adding #{pp.parsed_name}"

      file_list<<{
        "name": pp.parsed_name,
        "file_name": file,
        "version": version,
        "change_log": change_log,
        "description": pp.parsed_short_description,
        "category": pp.parsed_category,
        "severity": pp.parsed_severity,
        "readme": readme,
        "provider": provider,
        "service": service,
        "policy_set": policy_set,
      }
    end
  end
  policies = {"policies": file_list }
  File.open('dist/active-policy-list.json', 'w') { |file| file.write(JSON.pretty_generate(policies)+"\n") }
end
