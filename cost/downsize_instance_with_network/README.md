## Downsize Instances CPU, Memory, and Network Policy Template

### What it does

This Policy Template uses user defined to determine if you can decrease the size of your running instance.  

### Usage

The Downsize Instances Policy Template is used to actually downsize instances user defined tags on the instances.  The policy will use the *Tags to find instances* list to find the instances with provided tags and downsize them.  The tags must be inform of a [RightScale Tag](https://docs.rightscale.com/cm/ref/list_of_rightscale_tags.html#overview)
To downsize the instance it must be **stopped**.  If you don't want to stop and resize the instance you can add an additional tag and include that tag in the *Tags to ignore instances* input.
If a server is marked `N/A`, no action will be taken and only the resize tag will be removed. You will need to manually move that instance to another family type.
When an instance is downsized a new tag *rs_downsize:cooldown* is added which value is the date and time of the number of days from the Downsize to the Cooldown Days parameter.  This tag is then deleted after the Cooldown Days has exceeded.  This policy will also provide a very rough estimate of the amount of money that can be saved(check *Cost Limitations* below)


### Parameters

#### Downsize Instances Policy Template
1. Email list - List of email addresses to send incident report to
2. Tags to find instances - List of tags used to filter instances that must validate policy. (e.g.: ec2:downsize:true, azure:downsize:true, gce:downsize=true)
3. Tags to ignore instances - List of tags that will exclude instances from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'
4. Cooldown Days - Days to cooldown between checks of same instance.
5. param_avg_free_memory_percent - Average free memory percent to allow for downsize, -1 means ignore parameter
6. param_max_free_memory_percent - Maximum free memory percent to allow for downsize, -1 means ignore parameter
7. param_avg_cpu_idle - Average cpu idle percent to allow for downsize, -1 means ignore parameter
8. param_max_cpu_idle - Maximum cpu idle percent to allow for downsize, -1 means ignore parameter
9. param_avg_network_throughput_interface_eth0 - Average network throughput interface_eth0 to allow for downsize, -1 means ignore parameter
10. param_max_network_throughput_interface_eth0 - Maximum network throughput via interface_eth0 to allow for downsize, -1 means ignore parameter
11. param_avg_network_throughput_Amazon_Elastic_Network_Adapter - Average network throughput via Amazon_Elastic_Network_Adapter to allow for downsize - Maximum network throughput Amazon_Elastic_Network_Adapter to allow for downsize, -1 means ignore parameter
12. param_max_network_throughput_Amazon_Elastic_Network_Adapter, Maximum network throughput Amazon_Elastic_Network_Adapter to allow for downsize, -1 means ignore parameter
13. param_avg_network_throughput_Intel_R_82599_Virtual_Function - Average network throughput via Intel_R_82599_Virtual_Function to allow for downsize, -1 means ignore parameter
14. param_max_network_throughput_Intel_R_82599_Virtual_Function - Maximum network throughput via Intel_R_82599_Virtual_Function  to allow for downsize, -1 means ignore parameter
15. param_avg_network_throughput_Amazon_PV_Network_Adapter - Average network throughput via Amazon_PV_Network_Adapter to allow for downsize
16. param_max_network_throughput_Amazon_PV_Network_Adapter - Maximum network throughput via Amazon_PV_Network_Adapter to allow for downsize
    * * Cost Limitations * * 
         1. Based on AWS us-east-1(N. Virginia).
         2. Based on linux on demand servers only
         3. 720 hours regardless of month
         4. Cost are static, they are hard coded. 
         5. cost data date: 2019-09-12

#### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Delete Cooldown tag after cooldown days has exceeded
- Send an email report

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, instances and tags).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer

### Supported Clouds

- AWS

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
