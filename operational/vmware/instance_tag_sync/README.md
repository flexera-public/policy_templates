# VMWare Instance Tag Sync

## What it does

This Policy Template is used to automatically synchronize the CMP Tags to VMWare.

## Functional Details

This policy has the following requirements to function properly. You will need to setup a wstunnel to the vsphere server. There is a 1:1 relationship between RCAV's and this policy.

- RCAV
- The cloud configured inside of CMP
- [WS-Tunnel](https://github.com/rightscale/wstunnel)
- `/usr/local/bin/wstunnel cli -token $WSTUNNEL_TOKEN -tunnel wss://wstunnel10-1.rightscale.com -server $VSPHERE_HTTPS -logfile /var/log/wstuncli-policy.log -pidfile /var/run/wstunnel-policy.pid`

This policy performs the following action:

- Synchronizes Instance Tags from RightScale to VMware

## Input Parameters

This policy has the following input parameter required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Cloud Name* - Name of VMWare Cloud to run the policy against
- *wstunnel host* - Host for Tunnel to VSphere Server
- *wstunnel token* - Token for Tunnel to VSphere Server
- *vsphere username* - VSphere Username
- *vsphere password* - VSphere Password
- *tag category* - VMware Category for Tag Association
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Synchronize Tags" action while applying the policy, the identified resources tags will be synchronized from CMP to VMWare.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- VMware instances are tagged

Please note that wstunnel should be running for the action to complete successfully.

## Cloud Management Required Permissions

This policy requires permissions to access Cloud Management resources; Clouds and Subnets.  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or at the Organization level. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - observer

## VMWare Required Permissions

- Assign or Unassign vSphere Tag
- Assign or Unassign vSphere Tag on Object
- Create vSphere Tag
- Create vSphere Tag Category
- Delete vSphere Tag
- Delete vSphere Tag Category
- Edit vSphere Tag
- Edit vSphere Tag Category
- Modify UsedBy Field for Category
- Modify UsedBy Field for Tag

## Supported Clouds

- VMWare

## Cost

This Policy Template does not incur any cloud costs.
