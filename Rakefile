require 'rubygems'
require 'json'
require 'fileutils'

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
    @version = nil

    if !file.match(/test_code/)
      f = File.open(file, "r:bom|utf-8")
      f.each_line do |line|
        if line =~ /^name/
          @name = line.split(' ')[1..-1].join(' ').to_s.chomp('"').reverse.chomp('"').reverse
        end
        if line =~ /long_description/
          if line =~ /Version/
            @version = line.split(':').last.strip.chomp("\"")
          end
        end
        if line =~ /short_description/
          @description = line.split(' ')[1..-1].join(' ').to_s.chomp('"').reverse.chomp('"').reverse.split('.').first
        end
        if line =~ /category \"(compliance|cost|operational|security|saas management)\"/i
          @category = line.split(' ')[1..-1].join(' ').to_s.chomp('"').reverse.chomp('"').reverse
          @category = @category.gsub(" ","_")
          @category = @category.downcase
        end
        if line =~ /severity/
          @severity = line.split(' ')[1..-1].join(' ').to_s.chomp('"').reverse.chomp('"').reverse
        end
      end

      # skip policy if the version isn't supplied or if version is '0.0'
      if ! @version || @version == '0.0'
        puts "Skipping #{@name}, policy missing version"
        next
      end

      puts "Adding #{@name}"

      file_list<<{
        "name": @name,
        "file_name": file,
        "version": @version,
        "change_log": change_log,
        "description": @description,
        "category": @category,
        "severity": @severity,
        "readme": readme
      }
    end
  end
  policies = {"policies": file_list }
  File.open('dist/active-policy-list.json', 'w') { |file| file.write(JSON.pretty_generate(policies)+"\n") }
end
