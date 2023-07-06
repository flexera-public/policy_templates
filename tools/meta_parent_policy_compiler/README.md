# Meta Parent Policy Compiler

A script that compiles a "Meta Parent" Policy Template from a "Child" Policy Template source file.

## Usage

Basic Usage:

```sh
ruby meta_parent_policy_compiler.rb <path_to_child_policy_template>
## Output will be the same directory as the source child policy template with `_meta_parent.pt` suffix
```

Example batch run with bash:

```sh
for child_pt in ../../cost/azure/unused_volumes/azure_unused_volumes_meta_parent.pt ../../cost/aws/idle_compute_instances/idle_compute_instances.pt ../../cost/aws/object_storage_optimization/aws_object_storage_optimization.pt ../../cost/aws/old_snapshots/aws_delete_old_snapshots.pt ../../cost/aws/rightsize_compute_instances/aws_compute_rightsizing.pt ../../cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing.pt ../../cost/aws/unused_ip_addresses/aws_unused_ip_addresses.pt ../../cost/aws/unused_rds/unused_rds.pt ../../cost/aws/unused_volumes/aws_delete_unused_volumes.pt; do
  ruby meta_parent_policy_compiler.rb $child_pt;
done
```
