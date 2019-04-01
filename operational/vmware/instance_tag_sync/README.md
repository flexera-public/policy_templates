## VMWare Instance Tag Sync

### What it does

This Policy Template is used to automatically synchronize the CMP Tags to VMWare. 

### Functional Details
This policy has the following requirements to function properly. You will need to setup a wstunnel to the vsphere server. There is a 1:1 relationship between RCAV's and this policy.
1. RCAV
1. The cloud configured inside of CMP 
1. [WS-Tunnel](https://github.com/rightscale/wstunnel)
1. `/usr/local/bin/wstunnel cli -token $WSTUNNEL_TOKEN -tunnel wss://wstunnel10-1.rightscale.com -server $VSPHERE_HTTPS -logfile /var/log/wstuncli-policy.log -pidfile /var/run/wstunnel-policy.pid`

This policy performs the following action:
- Synchronizes Instance Tags from RightScale to VMware

### Input Parameters

This policy has the following input parameter required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Cloud Name* - Name of VMWare Cloud to run the policy against
- *wstunnel token* - Token for Tunnel to VSphere Server
- *vsphere username* - VSphere Username
- *vsphere password* - VSphere Password
- *tag category* - VMware Category for Tag Association

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- VMware instances are tagged

### Cloud Management Required Permissions

This policy requires permissions to access Cloud Management resources; Clouds and Subnets.  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or at the Organization level. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - observer
- Cloud Management - admin or credential_viewer
- Cloud Management - security_manager

### VMWare Required Permissions

  1. Assign or Unassign vSphere Tag
  1. Assign or Unassign vSphere Tag on Object
  1. Create vSphere Tag
  1. Create vSphere Tag Category
  1. Delete vSphere Tag
  1. Delete vSphere Tag Category
  1. Edit vSphere Tag
  1. Edit vSphere Tag Category
  1. Modify UsedBy Field For Category
  1. Modify UsedBy Field For Tag

### Supported Clouds

- VMWare

### Cost

This Policy Template does not incur any cloud costs.
