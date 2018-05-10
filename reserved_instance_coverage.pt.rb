name "Reserved Instances Coverage"
rs_pt_ver 20180301
type "policy"
short_description "A policy that sends email notifications on reserved intsance coverage"
long_description "Version 0.1"
severity "medium"
category "Cost"

permission "optima" do
  label "Access Optima Resources"
  resources "rs_optima.aws_reserved_instances"
  actions "rs_optima.index"
end

#parameter "heads_up_days" do
#  type "number"
#  label "Number of days to prior to expiration date to trigger incident"
#end

parameter "heads_up_days2" do
  type "number"
  label "Number of days into the past to view ri converage"
end

parameter "escalate_to" do
  type "string"
  label "Email address to send escalation emails to"
end

auth "mykey", type: "aws" do
  version "4"
  service "ec2"
  region "us-east-1"
  access_key cred("AWS_ACCESS_KEY_ID")
  secret_key cred("AWS_SECRET_ACCESS_KEY")
end

datasource "reservations_coverage" do
  request do
    auth $mykey
    #host "api.ce.us-east-1.amazonaws.com"
    # https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-explorer-api.html
    host "ce.us-east-1.amazonaws.com"
    query "X-Amz-Target", "AWSCostExplorerService.GetReservationCoverage"
    #path "/api/reco/orgs/2932/aws_reserved_instances"
    #TimePeriod:
  end

  result do
    encoding "json"
    collect jmes_path(response,"[*]") do
      field "coveragehours", jmes_path(col_item,"CoverageHours")
      field "coveragesbytime", jmes_path(col_item,"CoveragesByTime")
      #field "account_id", jmes_path(col_item,"account_id")
      #field "region", jmes_path(col_item,"region")
      #field "instance_type", jmes_path(col_item,"instance_type")
      #field "instance_count", jmes_path(col_item,"number_of_instances")
    end
  end
end

escalation "alert" do
    email $escalate_to do
      subject_template "Reserved Instance Coverage"
      body_template "Reserved Instance Coverage"
    end
  end

  policy "ri_coverage" do
    validate_each $reservations_coverage do
      summary_template "Reserved instances coverage."
      detail_template <<-EOS
  Reserved Instance Coverage
  {{ range data }}
  * Account: {{ .account_name }}({{ .account_id }})
  * Region: {{.region}}
  * Instance Type: {{.instance_type}}
  * Instance Count: {{.instance_count}}
  * End Time: {{.end_datetime}}
  ----------------------------
  {{ end }}
  EOS
      escalate $alert
      check gt(dec(to_d(val(item, "end_datetime"), now), prod($heads_up_days, 24*3600))
    end
end