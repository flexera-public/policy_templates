require 'rubygems'
require 'json'
require 'fileutils'
require "open-uri"
require 'yaml'
require 'openssl'
require_relative 'tools/lib/policy_parser'

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

      # get version from long description
      if version.nil? && pp.parsed_long_description =~ /Version/
        version = pp.parsed_long_description.split(':').last.strip.chomp("\"")
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

desc "Creates a KPI file to track policies meeting finops kpis"
task :generate_kpi_list do
  OpenSSL::SSL::VERIFY_PEER = OpenSSL::SSL::VERIFY_NONE
  kpis_url = "https://raw.githubusercontent.com/finopsfoundation/kpis/master/waste-sensors/waste-sensors.yml"
  kpis_file = '../../kpis.json'
  waste_sensor_file = "./waste-sensors.yml"
  SHIELD_URL_PREFIX = 'https://img.shields.io/badge/'.freeze

  open(kpis_url) do |sensors|
    File.open(waste_sensor_file, "wb") do |file|
      file.write(sensors.read)
    end
  end
  parsed_finops_kpis = YAML.load_stream(File.open(waste_sensor_file))

  file_list = []
  Dir['**/*.pt'].reject{ |f| f['msp/'] }.each do |file|
    if !file.match(/test_code/)
      f = File.open(file, "r:bom|utf-8")

      pp = PolicyParser.new
      pp.parse(file)

      if pp.parsed_info
        provider = pp.parsed_info[:provider]
        finops_waste_sensor_id = pp.parsed_info[:finops_waste_sensor_id]
      end
      name = pp.parsed_name
      if !finops_waste_sensor_id.nil?
        file_list<<{
          name: name,
          provider: provider,
          finops_waste_sensor_id: finops_waste_sensor_id
        }
      end
    end
  end

  success_counter = 0
  parsed_finops_kpis.each do |kpi|
    x = file_list.find { |f| f[:finops_waste_sensor_id] == kpi["id"] }
    if !x.nil?
      kpi["policy"] = x[:name]
      success_counter += 1
    else
      kpi["policy"] = nil
    end
  end

  File.open("./finops-kpis.json", "wb") do |file|
    file.write(JSON.pretty_generate(parsed_finops_kpis))
  end

  percentage_coverage = ((success_counter.to_f/parsed_finops_kpis.length().to_f).to_f*100).to_i
  message = "#{percentage_coverage}%"
  png_url = URI.escape(SHIELD_URL_PREFIX + "Finops Waste Sensor Coverage-#{message}-brightgreen.svg?style=plastic")
  open(png_url) do |png|
    File.open('sensors.svg', "wb") do |file|
      file.write(png.read)
    end
  end
  File.delete(waste_sensor_file) if File.exist?(waste_sensor_file)
end
