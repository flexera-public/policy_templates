## Billing Center Access Report

### What it does

This Policy Template accepts an input that defines which Azure regions are allowed by your compliance policies. Any Azure resource that exists outside of your approved regions will be raised in an Incident. Incidents will escalate to an email notification and will trigger an approval workflow prior to executing Cloud Workflow to delete the resources.

### Pre-reqs

- Required roles:
  - `billing_center_admin` or `billing_center_viewer`
  - `enterprise_manager`

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
