# Permission Extractor Script Failure Analysis

## Executive Summary

The permission extraction script fails to derive IAM permissions for 18 policy templates across 6 categories. Root causes fall into **6 main categories**, each requiring specific code changes to `policy_api_list_generator.py`.

---

## Root Cause Categories

### 1. Parameter `allowed_values` Not Enumerated (GCP A1-A3)
**Impact: 3 policies, 17+ missing permissions**

The script finds parameter definitions with `allowed_values` but doesn't:
- Trace how parameters are used in JavaScript
- Extract the mapping from parameter values to actual API identifiers
- Generate permissions for each possible value

**Example:**
```
parameter "param_recommenders" do
  allowed_values [ "Idle Cloud SQL Instance", "Overprovisioned Cloud SQL Instance", ... ]
end

# JS maps to API IDs:
recommender_map = {
  "Idle Cloud SQL Instance": "google.cloudsql.instance.IdleRecommender",
  "Overprovisioned Cloud SQL Instance": "google.cloudsql.instance.OverprovisionedRecommender",
}

# Should generate: recommender.cloudsqlIdleInstanceRecommendations.list
```

---

### 2. Dynamic JavaScript Resource Type Iteration (GCP B2-B3)
**Impact: 2 policies, 22+ missing permissions**

When datasources use `run_script` to generate requests for dynamic resource types:
```
datasource "ds_compute_resources" do
  run_script $js_compute_resources, $param_resource_types
end

script "js_compute_resources" do
  _.each(resource_types, function(type) {
    result.push({
      host: "compute.googleapis.com",
      path: "/compute/v1/projects/" + projectId + "/global/" + type
    })
  })
end
```

The script only sees the template code, not what values `resource_types` contains at runtime (instances, disks, images, snapshots, etc.).

---

### 3. Variable Assignment Resolution in Escalation Blocks (GCP B1, Azure E)
**Impact: 6 policies, 15+ missing permissions**

Define blocks construct URLs via variable assignment:
```
define delete_instance($instance) do
  $href = $instance["id"]  # Full resource path with type embedded
  http_request(
    verb: "delete",
    host: $param_azure_endpoint,
    href: $href
  )
end
```

The script doesn't extract the resource type from `$instance["id"]` which contains `/providers/Microsoft.Compute/virtualMachines/{name}`.

---

### 4. AWS Special Query Parameters & Headers (AWS C, D)
**Impact: 4 policies, 6 missing permissions**

- **S3 query strings**: `?acl=`, `?tagging=`, `?uploads=` not mapped to specific S3 permissions
- **JSON-RPC headers**: AWS Pricing API uses `x-amz-target: AWSPriceListService.GetProducts` header instead of URL for action

---

### 5. Azure Storage Service APIs (Azure F)
**Impact: 3 policies, 3 missing permissions**

Storage service endpoints like `{account}.blob.core.windows.net` aren't ARM APIs. They use:
- Host pattern: `{account}.blob.core.windows.net`
- Query params: `comp=properties`, `comp=list`

These need special mapping, not standard ARM permission derivation.

---

### 6. Azure Role-Based Permissions (Azure F5-F6)
**Impact: 2 policies, 2 missing permissions**

Azure storage services require RBAC roles, not REST API permissions:
- `Storage Queue Data Reader` (not a REST operation)
- `Storage Table Data Reader` (not a REST operation)

Script has no support for role-based permissions.

---

## Detailed Policy Analysis

### GROUP A: GCP Recommender (3 policies)

| Policy | Missing | Root Cause | Effort |
|--------|---------|-----------|--------|
| recommender.pt | 17 permissions | Parameter allowed_values not enumerated | LARGE |
| rightsize_cloudsql_recommendations.pt | 4 permissions | Same as above | LARGE |
| rightsize_vm_recommendations.pt | 2 permissions | Same as above | LARGE |

**Fix:** Extract `allowed_values`, find JS mapping script, generate permissions for each value.

---

### GROUP B: GCP JS Scripts (3 policies)

| Policy | Missing | Root Cause | Effort |
|--------|---------|-----------|--------|
| rightsize_cloudsql_instances.pt | 2 permissions | Variable verb resolution in define blocks | MEDIUM |
| unlabeled_resources.pt | 14 permissions | Dynamic resource type iteration in run_script | LARGE |
| label_cardinality.pt | 8 permissions | Same as above | LARGE |

**Fix:** Analyze `run_script` code to enumerate all possible resource types; resolve variable assignments.

---

### GROUP C: AWS Query Parameters (3 policies)

| Policy | Missing | Root Cause | Effort |
|--------|---------|-----------|--------|
| s3_multipart_uploads.pt | 1 permission | S3 query param `?uploads=` not mapped | SMALL |
| schedule_instance.pt | 2 permissions | Implicit KMS permissions (design limitation) | MEDIUM |
| public_buckets.pt | 1 permission | S3 query param `?acl=` not mapped | SMALL |

**Fix:** Add S3 query string mapping table; document KMS as implicit requirement.

---

### GROUP D: AWS Pricing API (1 policy)

| Policy | Missing | Root Cause | Effort |
|--------|---------|-----------|--------|
| superseded_ebs_volumes.pt | 1 permission | JSON-RPC action in x-amz-target header | SMALL |

**Fix:** Check `x-amz-target` header for action name; extract and map.

---

### GROUP E: Azure ARM Define Blocks (6 policies)

| Policy | Missing | Root Cause | Effort |
|--------|---------|-----------|--------|
| long_stopped_instances.pt | 2 permissions | Extract resource type from path in define block | MEDIUM |
| rightsize_managed_disks.pt | 1 permission | Infer permission from referenced field (managedBy) | MEDIUM |
| rightsize_netapp.pt | 2 permissions | Hierarchical Azure resource paths | MEDIUM |
| rightsize_sql_instances.pt | 2 permissions | Extract resource type from path in define block | MEDIUM |
| unused_app_service_plans.pt | 1 permission | Extract resource type from path in define block | MEDIUM |
| unused_vngs.pt | 1 permission | Extract resource type from path in define block | MEDIUM |

**Fix:** Parse `/providers/{Namespace}/{ResourceType}` pattern from paths; combine with HTTP verb.

---

### GROUP F: Azure Miscellaneous (5 policies)

| Policy | Missing | Root Cause | Effort |
|--------|---------|-----------|--------|
| hybrid_use_benefit_sql.pt | 4 permissions | Conditional resource type mapping in escalation | LARGE |
| unused_volumes.pt | 1 permission | Extract resource type from snapshot path | MEDIUM |
| blob_storage_logging.pt | 2 permissions | Storage API not ARM; query param mapping | MEDIUM |
| private_blob_containers.pt | 2 permissions | Storage API not ARM; comp=list mapping | MEDIUM |
| queue_storage_logging.pt | 1 permission | Role-based (not REST API) | MEDIUM |
| table_storage_logging.pt | 1 permission | Role-based (not REST API) | MEDIUM |

**Fix:** Add storage service detection; support role-based permissions; extract from conditional branches.

---

## Required Code Changes to policy_api_list_generator.py

### 1. Parameter Enumeration (Priority: HIGH)

```python
def _extract_parameter_allowed_values(self):
    """Extract allowed_values from parameter blocks."""
    param_pattern = r'parameter\s+"(\w+)".*?allowed_values\s+\[(.*?)\]'
    results = {}
    for match in re.finditer(param_pattern, self.content, re.DOTALL):
        param_name = match.group(1)
        values_str = match.group(2)
        values = [v.strip().strip('"\'') for v in values_str.split(',')]
        results[param_name] = values
    return results

def _find_parameter_mapping_in_scripts(self, param_name):
    """Find JS variable assignment that maps parameter values to API IDs."""
    # Look for patterns like: map = { "param_value": "api_id", ... }
    # When param_name is param_recommenders, look for recommender_map
    base_name = param_name.replace('param_', '')
    map_pattern = rf'{base_name}_map\s*=\s*\{{(.*?)\}}'
    
    for match in re.finditer(map_pattern, self.content, re.DOTALL):
        # Extract {key: value} pairs
        pairs = self._extract_hash_pairs('{' + match.group(1) + '}')
        yield pairs
```

### 2. Azure Resource Type Extraction (Priority: HIGH)

```python
def _extract_azure_resource_type_from_path(self, path):
    """Extract Microsoft.Service/ResourceType from path."""
    if not path:
        return None
    # Normalize placeholders: /subscriptions/{id}/providers/Microsoft.X/Y/{z}
    normalized = re.sub(r'\{[^}]+\}', '*', path)
    match = re.search(r'/providers/([^/]+/[^/]+(?:/[^/]+/\*)*)', normalized)
    if match:
        resource_path = match.group(1)
        # Remove trailing /* from nested resources
        base_type = re.sub(r'/\*$', '', resource_path)
        return base_type
    return None

def _derive_azure_permission_from_path_and_verb(self, path, method):
    """Derive Azure permission: Microsoft.X/Y/action from path and verb."""
    resource_type = self._extract_azure_resource_type_from_path(path)
    if not resource_type:
        return ''
    
    action_map = {
        'GET': 'read',
        'POST': 'write',
        'PUT': 'write',
        'PATCH': 'write',
        'DELETE': 'delete'
    }
    action = action_map.get(method.upper(), 'read')
    return f'{resource_type}/{action}'
```

### 3. S3 Query String Mapping (Priority: HIGH)

```python
def _get_s3_permission_from_query(self, query_params, method):
    """Map S3 query parameters to specific permissions."""
    s3_operations = {
        'acl': 's3:GetBucketAcl',
        'tagging': 's3:GetBucketTagging',
        'cors': 's3:GetBucketCors',
        'lifecycle': 's3:GetBucketLifecycle',
        'logging': 's3:GetBucketLogging',
        'encryption': 's3:GetBucketEncryption',
        'versioning': 's3:GetBucketVersioning',
        'uploads': 's3:ListBucketMultipartUploads',
        'uploadId': 's3:AbortMultipartUpload',
    }
    
    for param_key in query_params.keys():
        if param_key in s3_operations:
            return s3_operations[param_key]
    return None
```

### 4. JSON-RPC Header Detection (Priority: MEDIUM)

```python
def _get_aws_action_from_header(self, headers):
    """Extract action from x-amz-target header (JSON-RPC style)."""
    target = headers.get('x-amz-target', '')
    if target and '.' in target:
        # Format: "ServiceName.ActionName"
        return target.split('.')[-1]
    return None
```

### 5. Azure Storage Service Detection (Priority: MEDIUM)

```python
def _is_azure_storage_service_endpoint(self, host):
    """Check if host is Azure Blob/Queue/Table storage."""
    return bool(re.search(
        r'\.(blob|queue|table|file)\.core\.(windows\.net|chinacloudapi\.cn)',
        host or ''
    ))

def _derive_azure_storage_permission(self, host, query_params):
    """Derive permission for Azure Storage APIs."""
    if not self._is_azure_storage_service_endpoint(host):
        return ''
    
    comp = query_params.get('comp', '')
    restype = query_params.get('restype', '')
    
    if '.blob.core' in host:
        if comp == 'list' or (restype == 'container' and comp == 'list'):
            return 'Microsoft.Storage/storageAccounts/blobServices/containers/list'
        elif comp == 'properties':
            return 'Microsoft.Storage/storageAccounts/blobServices/containers/list'
    elif '.queue.core' in host:
        return 'Storage Queue Data Reader'  # Role-based
    elif '.table.core' in host:
        return 'Storage Table Data Reader'  # Role-based
    
    return ''
```

### 6. Dynamic Resource Type Analysis (Priority: LARGE)

```python
def _analyze_run_script_for_enumerable_resources(self, script_code, params):
    """Analyze script to find enumerable resource types."""
    # Look for: _.each(param_types, function(...) { ... })
    loop_pattern = r'_\.each\((\w+),\s*function'
    matches = list(re.finditer(loop_pattern, script_code))
    
    for match in matches:
        loop_var = match.group(1)
        # Check if this is a parameter we can enumerate
        for param in params:
            # param might be 'resource_types', loop_var might be 'resource_types'
            param_base = param.replace('$param_', '').replace('$ds_', '')
            if loop_var == param_base or loop_var == param:
                return {
                    'enumerable': True,
                    'parameter': param,
                    'loop_var': loop_var
                }
    
    return {'enumerable': False}
```

---

## Implementation Priority & Effort Estimates

| Priority | Items | Total Effort | Policies Fixed |
|----------|-------|--------------|-----------------|
| P0 (CRITICAL) | Azure ARM path extraction | 4 hours | 6 |
| P0 | S3 query strings + Pricing header | 3 hours | 4 |
| P1 (HIGH) | Parameter allowed_values enum | 6 hours | 3 |
| P1 | Dynamic resource type iteration | 8 hours | 2 |
| P2 (MEDIUM) | Azure Storage service APIs | 4 hours | 3 |
| P2 | Conditional resource mapping | 4 hours | 1 |
| P3 (LOW) | Azure role support | 4 hours | 2 |
| **TOTAL** | | **33 hours** | **18 policies** |

**Recommended approach:**
1. Start with P0 items (7 hours) - fixes 10 policies
2. Add P1 items (14 hours) - fixes 5 more policies
3. Add P2 items (8 hours) - fixes 3 more policies
4. P3 optional (4 hours) - documents Azure roles limitation

---

## Testing Strategy

For each fix, create test cases using the problematic policies:

1. **Test Parameter Enumeration**: recommender.pt should generate 17 permissions
2. **Test Resource Type Extraction**: unlabeled_resources.pt should generate compute.*.list permissions
3. **Test S3 Queries**: public_buckets.pt should extract s3:GetBucketAcl
4. **Test Azure Paths**: long_stopped_instances.pt should extract Microsoft.Compute/virtualMachines/delete
5. **Test JSON-RPC**: superseded_ebs_volumes.pt should extract pricing:GetProducts

