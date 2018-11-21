## Billing Center Access Report

### What it does

This Policy Template can target either all Billing Centers in an Organization or target a specific Billing Center.  Child Billing Centers are supported as well.  The resulting incident is a report of all users that have access to the target Billing Center(s).  If RightScale Groups have been granted access to a Billing Center, the report will indicate which Group has delegated access to a particular user. *This policy should only be applied to the Master Project, and not to each individual project.*

### Pre-reqs

- Required roles:
  - `billing_center_admin` or `billing_center_viewer`
  - `enterprise_manager`

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
