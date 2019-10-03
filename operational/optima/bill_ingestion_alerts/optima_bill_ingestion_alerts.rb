name "Optima Bill Ingestion Alerts"
rs_pt_ver 20180301
type "policy"
short_description "This policy alerts you when bill data for AWS, Azure, or Google connected bills are not being ingested. See [README](https://github.com/rightscale/policy_templates/tree/master/operational/optima/bill_ingestion_alerts) for more details"
long_description "Version: 1.0"
severity "medium"
category "Operational"
tenancy "single"

###############################################################################
# Parameters
###############################################################################

parameter "param_email" do
  type "list"
  label "Email List"
  description "Email addresses of the recipients you wish to notify"
end

###############################################################################
# Authentication
###############################################################################

auth "auth_rs", type: "rightscale"

###############################################################################
# Pagination
###############################################################################

###############################################################################
# Datasources
###############################################################################

datasource "ds_bill_connects" do
  request do
    auth $auth_rs
    host "onboarding.rightscale.com"
    path join(["/api/onboarding/orgs/",rs_org_id,"/bill_connects"])
    header "Api-Version", "1.0"
    header "User-Agent", "RS Policies"
  end
  result do
    encoding "json"
    collect jmes_path(response,"[*]") do
      field "cloud_vendor_id", jmes_path(col_item,"cloud_vendor_id")
      field "created_at", jmes_path(col_item,"created_at")
      field "href", jmes_path(col_item,"href")
      field "id", jmes_path(col_item,"id")
      field "updated_at", jmes_path(col_item,"updated_at")
    end
  end
end

datasource "ds_csp_partners" do
  request do
    auth $auth_rs
    host "optima.rightscale.com"
    path join(["/analytics/orgs/",rs_org_id,"/azure_csp_partners"])
    header "Api-Version", "1.0"
    header "User-Agent", "RS Policies"
  end
  result do
    encoding "json"
    collect jmes_path(response,"[*]") do
      field "cloud_vendor_id", "azure-csp"
      field "created_at", jmes_path(col_item,"created_at")
      field "href", jmes_path(col_item,"href")
      field "id", jmes_path(col_item,"id")
      field "updated_at", jmes_path(col_item,"updated_at")
    end
  end
end

datasource "ds_normalize_bill_connects" do
  run_script $js_normalize_bill_connects, $ds_bill_connects, $ds_csp_partners
end

datasource "ds_billing_centers" do
  request do
    auth $auth_rs
    host rs_optima_host
    path join(["/analytics/orgs/",rs_org_id,"/billing_centers"])
    header "Api-Version", "1.0"
    header "User-Agent", "RS Policies"
    query "view", "allocation_table"
  end
  result do
    encoding "json"
    collect jmes_path(response,"[*]") do
      field "href", jmes_path(col_item,"href")
      field "id", jmes_path(col_item,"id")
      field "name", jmes_path(col_item,"name")
      field "parent_id", jmes_path(col_item,"parent_id")
      field "ancestor_ids", jmes_path(col_item,"ancestor_ids")
      field "allocation_table", jmes_path(col_item,"allocation_table")
    end
  end
end

datasource "ds_new_bc_costs" do
  iterate $ds_normalize_bill_connects
  request do
    run_script $js_new_costs_request, rs_org_id, $ds_billing_centers, val(iter_item,"cloud_vendor_select")
  end
  result do
    encoding "json"
    collect jmes_path(response,"rows[*]") do
      field "vendor", jmes_path(col_item, "dimensions.vendor")
      field "vendor_account", jmes_path(col_item,"dimensions.vendor_account")
      field "vendor_account_name", jmes_path(col_item,"dimensions.vendor_account_name")
      field "cost_amortized_unblended_adj", jmes_path(col_item,"metrics.cost_amortized_unblended_adj")
      field "usage_amount", jmes_path(col_item, "metrics.usage_amount")
      field "region", jmes_path(col_item, "dimensions.region")
      field "service", jmes_path(col_item, "dimensions.service")
      field "resource_type", jmes_path(col_item, "dimensions.resource_type")
      field "id", jmes_path(col_item,"dimensions.billing_center_id")
      field "resource_id", jmes_path(col_item, "dimensions.resource_id")
      field "timestamp", jmes_path(col_item,"timestamp")
    end
  end
end

datasource "ds_filter_cloud_bills" do
  run_script $js_filter_cloud_bills, $ds_new_bc_costs, $ds_normalize_bill_connects
end

###############################################################################
# Scripts
###############################################################################

script "js_normalize_bill_connects", type: "javascript" do
  parameters "ds_bill_connects","ds_csp_partners"
  result "result"
  code <<-EOS
    var result = [];
    var bill_connects = ds_bill_connects.concat(ds_csp_partners);
    _.each(bill_connects, function(bill_connect){
      var vendor = bill_connect['cloud_vendor_id'];
      if ( vendor === "aws" ) {
        cloud_vendor_normal = "aws"
        cloud_vendor_select = "AWS"
        cloud_vendor_friendly = "Amazon Web Services"
      } else if ( vendor === "azure-ea" ) { 
        cloud_vendor_normal = "azure"
        cloud_vendor_select = "Azure"
        cloud_vendor_friendly = "Microsoft Azure EA"
      } else if ( vendor === "azure-csp" ) {
        cloud_vendor_normal = "azurecsp"
        cloud_vendor_select = "AzureCSP"
        cloud_vendor_friendly = "Microsoft Azure CSP"
      } else if ( vendor === "google" ) {
        cloud_vendor_normal = "google"
        cloud_vendor_select = "Google"
        cloud_vendor_friendly = "Google Cloud Platform"
      }

      result.push({
        cloud_vendor_id: bill_connect.cloud_vendor_id
        created_at: bill_connect.created_at
        href: bill_connect.href
        id: bill_connect.id
        updated_at: bill_connect.updated_at
        cloud_vendor_normal: cloud_vendor_normal
        cloud_vendor_select: cloud_vendor_select
        cloud_vendor_friendly: cloud_vendor_friendly
      })
    })
EOS
end

script "js_new_costs_request", type: "javascript" do
  parameters "org_id","ds_billing_centers","cloud_vendor_select"
  result "request"
  code <<-EOS
    // format the date for the `daily` API
    // returns date formatted as string: YYYY-mm-dd
    function getFormattedDailyDate(date) {
      var year = date.getFullYear();

      var month = (1 + date.getMonth()).toString();
      month = month.length > 1 ? month : '0' + month;

      var day = date.getDate().toString();
      day = day.length > 1 ? day : '0' + day;
      return year + '-' + month + '-' + day;
    }

    // subtract day(s) from the current day
    function subtractDays(date, days) {
      var result = new Date(date);
      result.setDate(result.getDate() - days);
      return result;
    }

    var now = new Date();
    var end_date = getFormattedDailyDate(now)
    var start_date = getFormattedDailyDate(subtractDays(now, 4))
    var billing_center_ids = []
    var top_billing_centers = _.reject(ds_billing_centers, function(bc){ return bc.parent_id != null });
    billing_center_ids = _.map(top_billing_centers, function(value, key){ return value.id });

    var dimensions = ["billing_center_id","vendor","vendor_account","vendor_account_name","category","instance_type","region","resource_type","service","usage_type","usage_unit","resource_id"]

    var request = {
      auth: "auth_rs",
      host: "optima.rightscale.com",
      verb: "POST",
      path: "/bill-analysis/orgs/" + org_id + "/costs/select",
      body_fields: {
        "billing_center_ids": billing_center_ids,
        "dimensions": dimensions,
        "metrics": ["usage_amount", "cost_amortized_unblended_adj"],
        "granularity": "day",
        "start_at": start_date,
        "end_at": end_date,
        "limit": 1,
        "filter": {
          "dimension":"vendor",
          "type":"equal",
          "value": cloud_vendor_select
        }
      },
      headers: {
        "Api-Version": "1.0",
        "User-Agent": "RS Policies",
      }
    }
EOS
end

script "js_filter_cloud_bills", type: "javascript" do
  parameters "ds_new_bc_costs", "ds_normalize_bill_connects"
  result "result"
  code <<-EOS
    var result = [];
    var current_clouds = _.unique(_.pluck(ds_new_bc_costs, 'vendor').map(function(line) {return line.toLowerCase()}))

    console.log("current_clouds:", current_clouds)
    
    //Bill connect is aws, azure-ea, ??, ??
    //Bill data vendor is AWS, Azure, AzureCSP, Google

    _.each(ds_normalize_bill_connects, function(bill_connect){
      var vendor = bill_connect['cloud_vendor_normal'];
      var vendor_friendly = bill_connect['cloud_vendor_friendly']
      console.log("Vendor: " + vendor)
      
      if ( _.contains(current_clouds, vendor) ) {
        //Current bill data contains this vendor, nothing more to do
      } else {
        result.push({
          cloud_vendor: vendor_friendly
        })
      }
    })
EOS
end

###############################################################################
# Policy
###############################################################################

policy "policy_bill_ingestion_alert" do
  validate $ds_filter_cloud_bills do
    summary_template "{{ rs_org_name }} (Org ID: {{ rs_org_id }}): Optima Bill Ingestion Alert"
    detail_template <<-EOS
# Optima Bill Ingestion Alert

Optima has not recently ingested bill data for the following clouds:

{{ range data -}}
* {{ .cloud_vendor }}
{{ end }}

Please verify that the relevant credentials are still accurate.<br>
[Optima - Cloud Provider Billing Data Instructions](https://helpnet.flexerasoftware.com/Optima/#helplibrary/Cloud_Provider_Billing_Data_Instructions.htm)<br>
[Optima - Billing Configuration](https://analytics.rightscale.com/orgs/{{ rs_org_id }}/settings/billing-config)<br>
___
###### Policy Applied in Account: {{ rs_project_name }} (Account ID: {{ rs_project_id }}) within Org: {{ rs_org_name }} (Org ID: {{ rs_org_id }})
EOS
    escalate $escalation_send_email
    check eq(size(data),0)
  end
end

###############################################################################
# Escalations
###############################################################################

escalation "escalation_send_email" do
  email $param_email
end

###############################################################################
# Cloud Workflow
###############################################################################

define sys_log($subject, $detail) do
  if $$debug
    rs_cm.audit_entries.create(
      notify: "None",
      audit_entry: {
        auditee_href: @@account,
        summary: $subject,
        detail: $detail
      }
    )
  end
end