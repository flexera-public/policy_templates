name "Reserved Instances Coverage"
rs_pt_ver 20180301
type "policy"
short_description "A policy that sends email notifications on reserved instance coverage"
long_description "Version 0.1"
severity "medium"
category "Cost"

permission "optima" do
  label "Access Optima Resources"
  resources "rs_optima.aws_reserved_instances"
  actions "rs_optima.index"
end

permission "permissions" do
  label "Access CM Index/Show/Data"
  actions "rs_cm.index", "rs_cm.show", "rs_cm.data"
  resources "rs_cm.instances", "rs_cm.monitoring_metrics"
end

##################
# User inputs    #
##################

parameter "param_email" do
  category "Contact"
  label "Email addresses (separate with commas)"
  type "string"
  allowed_pattern /^([a-zA-Z0-9-_.]+[@]+[a-zA-Z0-9-_.]+[.]+[a-zA-Z0-9-_]+,*|)+$/
end

parameter "param_service" do
 category "Service"
 label "AWS Service"
 type "string"
 allowed_values "Amazon Elastic Compute Cloud - Compute", "Amazon ElastiCache", "Amazon Redshift","Amazon Relational Database Service"
 default "Amazon Elastic Compute Cloud - Compute"
end

parameter "historical_number_of_days_in_past" do
  type "number"
  label "Number of days in the past to view RI Coverage"
  allowed_values "7", "14","30", "90", "180", "365"
  default "7"
end

parameter "param_utilization" do
  category "RI"
  label "Utilization"
  type "number"
  default "100"
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
    query "Service", $param_service
    query "startDate", "2018-02-01"
    query "endDate", "2018-03-01"
    query "X-Amz-Target", "AWSCostExplorerService.GetReservationCoverage"
    #query "X-Amz-Target", "AWSCostExplorerService.GetReservationCoverage"
    #path "/api/reco/orgs/2932/aws_reserved_instances"

  end
  result do
    encoding "json"
    collect jmes_path(response,"[*]") do
      field "total", jmes_path(col_item,"Total")
      field "coveragesbytime", jmes_path(col_item,"CoveragesByTime")
      #field "account_id", jmes_path(col_item,"account_id")
      #field "region", jmes_path(col_item,"region")
      #field "instance_type", jmes_path(col_item,"instance_type")
      #field "instance_count", jmes_path(col_item,"number_of_instances")
    end
  end
end

escalation "alert" do
  email $param_email
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
  #check lt(to_n(val(item,"utilization_percentage")),$param_utilization)
  check lt($param_utilization,$param_utilization)
 end
end