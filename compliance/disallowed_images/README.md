# Disallowed Cloud Images

## What it does

This policy checks all running instances for disallowed cloud images. The user is given the option to Terminate the instance after approval.

## Functional Details

The policy leverages the CMP API to check all instances not using the provided list of cloud image resource_uids. Running instance states include any instance with state: running, operational and provisioned. Found instances are terminated after user approval.

### Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Exclude Tags* - List of tags that will exclude instances from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag must be of the format 'namespace:predicate=value'. Example: 'rs_agent:type=right_link_lite,rs_monitoring:state=auth'.
- *Allowed Cloud Images* - A list of allowed cloud images resource_uids.

### Actions

- Sends an email notification.
- Terminate instances with disallowed cloud images after approval.

### Required RightScale Roles

- policy_designer
- policy_manager
- policy_publisher
- credential_viewer

### Supported Clouds

- Amazon
- Azure
- Google
- Openstack
- VmWare

### Cost

This Policy Template does not incur any cloud costs.
