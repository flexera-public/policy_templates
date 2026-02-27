"""
Extract REST API calls from Flexera Policy Templates.

This script parses Flexera policy template (.pt) files and extracts information about
all REST API calls, including the HTTP method, endpoint URL, target service (AWS, Azure, 
GCP, Oracle, Flexera, etc.), and fields extracted from the response.

Usage:
    python pt_extract_calls
    
The script will process all policies listed in data/active_policy_list/active_policy_list.json
and output results to:
    - data/policy_api_list/policy_api_list.json
    - data/policy_api_list/policy_api_list.csv
"""

import sys
import re
import csv
import json
from pathlib import Path


class PolicyTemplateParser:
    """Parser for Flexera Policy Template files."""
    
    # Service patterns to identify which service/cloud the API call targets
    # Order matters - more specific patterns should come first
    SERVICE_PATTERNS = {
        'Turbonomic': [
            r'turbonomic',  # Turbonomic (IBM) instances
            r'^flexera$',  # Turbonomic API with flexera as placeholder host
        ],
        'AWS': [
            r'\.amazonaws\.com',
        ],
        'Azure': [
            r'management\.azure\.com',
            r'management\.chinacloudapi\.cn',
            r'\.azure\.com',
            r'\.azure\.cn',
            r'\.windows\.net',  # Azure Storage (blob, queue, table, file)
            r'monitor\.azure\.',  # Azure Monitor (handles malformed URLs missing .com)
        ],
        'GCP': [
            r'\.googleapis\.com',
        ],
        'Oracle': [
            r'\.oraclecloud\.com',
        ],
        'Flexera': [
            r'api\.flexera\.(com|eu|jp)',
            r'optima\.flexeraeng\.com',
            r'governance\.rightscale\.com',
            r'us-3\.rightscale\.com',
            r'us-4\.rightscale\.com',
            r'api\.rsc\.flexeraeng\.com',
            r'rs_optima_host',  # Flexera built-in variable
            r'rs_governance_host',  # Flexera built-in variable
            r'flexera_api_host',  # Common pattern for Flexera API hosts
            r'flexnetmanager',  # FlexNet Manager
            r'fnms',  # FlexNet Manager Service abbreviation
            r'FlexNet Manager',  # FlexNet Manager full name
            r'api\.app\.',  # Flexera API endpoints (partial domains)
            r'Entire Estate',  # Flexera internal estate references
            r'ComplianceAPIService',  # FlexNet Compliance API
            r'flexeraeng\.com',  # Flexera engineering domain
            r'^false/',  # Placeholder URLs that are actually Flexera internal
            r'^Monthly/',  # Flexera reporting URLs
        ],
        'Spot by NetApp': [
            r'api\.spotinst\.io',
        ],
        'GitHub': [
            r'api\.github\.com',
            r'raw\.githubusercontent\.com',
        ],
        'Okta': [
            r'\.okta\.com',
        ],
        'ServiceNow': [
            r'\.service-now\.com',
        ],
        'Microsoft Graph': [
            r'graph\.microsoft\.com',
        ],
    }
    
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.content = self.file_path.read_text()
        self.policy_name = self._extract_policy_name()
        
    def _extract_policy_name(self):
        """Extract the policy template name from the file."""
        match = re.search(r'^name\s+"([^"]+)"', self.content, re.MULTILINE)
        return match.group(1) if match else self.file_path.stem
    
    def _extract_host_from_param(self, host_pattern):
        """
        Extract actual host from parameter references.
        E.g., $param_azure_endpoint -> management.azure.com
        """
        if not host_pattern or not isinstance(host_pattern, str):
            return None
        
        # Check for parameter reference pattern
        param_match = re.search(r'\$param_(\w+)', host_pattern)
        if param_match:
            param_name = param_match.group(1)
            # Find the parameter definition and extract its default value
            param_pattern = rf'parameter\s+"param_{param_name}".*?default\s+"([^"]+)"'
            param_def = re.search(param_pattern, self.content, re.DOTALL)
            if param_def:
                return param_def.group(1)
        
        # Check for val() function pattern - e.g., val($ds_flexera_api_hosts, "flexera")
        # These typically resolve to Flexera endpoints - try to extract them
        if 'val(' in host_pattern:
            # Try to extract the datasource name and look up its value
            # For now, return the pattern as-is for further processing
            pass
        
        # For Flexera endpoints, we want to capture them now
        # No need to return None for rs_optima_host or rs_governance_host
        
        return None
    
    def _resolve_parameter_from_content(self, var_name):
        """
        Resolve a variable reference to its default value from parameter definitions.
        E.g., param_azure_endpoint -> management.azure.com
        """
        if not var_name:
            return None
        
        # Try to match parameter definition
        # Pattern: parameter "var_name" do ... default "value" ... end
        param_pattern = rf'parameter\s+"{var_name}".*?default\s+"([^"]+)"'
        param_match = re.search(param_pattern, self.content, re.DOTALL)
        
        if param_match:
            return param_match.group(1)
        
        return None
    
    def _determine_api_service(self, host):
        """Determine which service/cloud the API call is targeting based on the host.
        
        Returns:
            str: The service name (e.g., 'AWS', 'Azure', 'Flexera') or 'Unknown' if not recognized.
        """
        if not host:
            return 'Unknown'
        
        for service, patterns in self.SERVICE_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, host, re.IGNORECASE):
                    return service
        
        return 'Unknown'
    
    def _extract_datasources(self):
        """Extract all datasource blocks from the policy template."""
        datasources = []
        lines = self.content.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check if this line starts a datasource
            ds_match = re.match(r'datasource\s+"([^"]+)"\s+do\s*$', line)
            if ds_match:
                datasource_name = ds_match.group(1)
                datasource_lines = []
                i += 1
                depth = 1  # Track nesting depth
                
                # Collect lines until we find the matching 'end'
                while i < len(lines) and depth > 0:
                    current_line = lines[i]
                    
                    # Check for nested 'do' statements
                    if re.search(r'\bdo\s*$', current_line):
                        depth += 1
                    # Check for 'end' statements
                    elif re.match(r'^\s*end\s*$', current_line):
                        depth -= 1
                        if depth == 0:
                            break
                    
                    datasource_lines.append(current_line)
                    i += 1
                
                datasources.append({
                    'name': datasource_name,
                    'body': '\n'.join(datasource_lines)
                })
            
            i += 1
        
        return datasources
    
    def _extract_request_info(self, datasource_body):
        """Extract request information from a datasource body."""
        request_info = {
            'has_request': False,
            'method': 'GET',  # Default method
            'host': None,
            'path': None,
            'script_name': None,
            'query_params': {},
            'body_params': {}
        }
        
        # Check if datasource has a request block
        if 'request do' not in datasource_body:
            return request_info
        
        request_info['has_request'] = True
        
        # Extract HTTP verb/method
        verb_match = re.search(r'verb\s+"([^"]+)"', datasource_body, re.IGNORECASE)
        if verb_match:
            request_info['method'] = verb_match.group(1).upper()
        
        # Extract host (including join pattern)
        host_match = re.search(r'host\s+join\(\[([^\]]+)\]\)', datasource_body)
        if host_match:
            # Extract quoted strings from the join array
            host_parts = re.findall(r'["\']([^"\']+)["\']', host_match.group(1))
            # Look for patterns like val(iter_item, 'region'), $param_region, etc.
            has_dynamic = ('val(iter_item' in host_match.group(1) or 
                          'iter_item' in host_match.group(1) or
                          '$param_' in host_match.group(1) or
                          '$' in host_match.group(1))
            
            if has_dynamic:
                # Replace with wildcard - build host from parts with * for dynamic values
                if len(host_parts) > 1:
                    # Multiple parts - join with wildcard between them
                    request_info['host'] = '*'.join(host_parts)
                elif len(host_parts) == 1:
                    # Single part with dynamic variable
                    # E.g., ["optimizer.", $param, ".oci.oraclecloud.com"] might only extract last part
                    # Check position of strings in original
                    join_content = host_match.group(1)
                    # Count how many non-string items there are
                    items = [x.strip() for x in join_content.split(',')]
                    if len(items) > len(host_parts):
                        # Has variables - add wildcards
                        if join_content.startswith('"') or join_content.startswith("'"):
                            # Starts with string
                            request_info['host'] = host_parts[0] + '*'
                        elif join_content.endswith('"') or join_content.endswith("'"):
                            # Ends with string
                            request_info['host'] = '*' + host_parts[0]
                        else:
                            request_info['host'] = '*.' + host_parts[0]
                    else:
                        request_info['host'] = host_parts[0]
                else:
                    # No string parts found but has dynamic content
                    request_info['host'] = None
            else:
                # Static join - just concatenate
                request_info['host'] = ''.join(host_parts)
        else:
            # Try simple host pattern
            host_match = re.search(r'host\s+["\']([^"\']+)["\']', datasource_body)
            if host_match:
                request_info['host'] = host_match.group(1)
            else:
                # Try val() function pattern - e.g., host val($ds_flexera_api_hosts, "flexera")
                val_match = re.search(r'host\s+val\([^)]+\)', datasource_body)
                if val_match:
                    # This is a Flexera API call using dynamic host lookup
                    request_info['host'] = 'flexera_api_host'
                else:
                    # Try bare variable pattern (e.g., host rs_optima_host, host rs_governance_host)
                    bare_var_match = re.search(r'host\s+(rs_\w+)', datasource_body)
                    if bare_var_match:
                        request_info['host'] = bare_var_match.group(1)
                    else:
                        # Try parameter reference pattern (e.g., host $param_azure_endpoint)
                        host_param_match = re.search(r'host\s+(\$\w+)', datasource_body)
                        if host_param_match:
                            param_ref = host_param_match.group(1)
                            resolved_host = self._extract_host_from_param(param_ref)
                            if resolved_host:
                                request_info['host'] = resolved_host
        
        # Extract path (including join pattern and simple quotes)
        path_match = re.search(r'path\s+join\(\[([^\]]+)\]\)', datasource_body)
        if path_match:
            # Extract quoted strings from the join array
            path_parts = re.findall(r'["\']([^"\']+)["\']', path_match.group(1))
            request_info['path'] = ''.join(path_parts)
        else:
            # Try simple path pattern with single or double quotes
            path_match = re.search(r'path\s+["\']([^"\']+)["\']', datasource_body)
            if path_match:
                request_info['path'] = path_match.group(1)
            else:
                # Check for val() or other dynamic expressions - use placeholder
                path_val_match = re.search(r'path\s+(val\(|iter_item)', datasource_body)
                if path_val_match:
                    request_info['path'] = '/{dynamic}'
                else:
                    request_info['path'] = '/'
        
        # Check for run_script in request
        script_match = re.search(r'run_script\s+\$([^,\s]+)', datasource_body)
        if script_match:
            request_info['script_name'] = script_match.group(1)
        
        # Extract query parameters (with double or single quotes)
        for query_match in re.finditer(r'query\s+["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']', datasource_body):
            param_name = query_match.group(1)
            param_value = query_match.group(2)
            request_info['query_params'][param_name] = param_value
        
        return request_info
    
    def _extract_request_from_script(self, script_name):
        """Extract request information from a JavaScript script block."""
        # Find the script definition
        script_pattern = rf'script\s+"{script_name}".*?do\s+(.*?)\nend'
        script_match = re.search(script_pattern, self.content, re.DOTALL)
        
        if not script_match:
            return None
        
        script_body = script_match.group(1)
        
        # Extract the JavaScript code
        code_pattern = r'code\s+<<-[\'"]?EOS[\'"]?\s+(.*?)EOS'
        code_match = re.search(code_pattern, script_body, re.DOTALL)
        
        if not code_match:
            return None
        
        js_code = code_match.group(1)
        
        request_info = {
            'method': 'GET',
            'host': None,
            'path': None,
            'query_params': {},
            'body_params': {}
        }
        
        # Extract verb from JavaScript
        verb_match = re.search(r'verb:\s*["\']([^"\']+)["\']', js_code)
        if verb_match:
            request_info['method'] = verb_match.group(1).upper()
        
        # Extract host from JavaScript
        # Look for the entire host line first
        host_line_match = re.search(r'host:\s*([^,\n]+)', js_code)
        if host_line_match:
            host_line = host_line_match.group(1).strip()
            
            # Check if this is a function call (e.g., get_host_by_region)
            if '(' in host_line and ')' in host_line:
                # This is a function call - try to trace the function
                func_match = re.search(r'function\s+(\w+)\s*\([^)]*\)\s*\{([^}]+)\}', js_code, re.DOTALL)
                if func_match:
                    func_body = func_match.group(2)
                    # Look for return statements with string patterns
                    return_match = re.search(r'return\s+([^;]+)', func_body)
                    if return_match:
                        return_expr = return_match.group(1).strip()
                        # Extract string literals from the return expression
                        strings = re.findall(r'["\']([^"\']+)["\']', return_expr)
                        if strings:
                            # Build host pattern with wildcards
                            # E.g., region + ".metrics.monitor.azure.com" -> "*.metrics.monitor.azure.com"
                            request_info['host'] = '*.'.join(s.lstrip('.') for s in strings if s)
                        else:
                            # No strings found, use a generic pattern
                            request_info['host'] = '*.monitor.azure.com' if 'azure' in func_body.lower() else None
            # Check if this is a concatenated string (contains +)
            elif '+' in host_line:
                # Extract all string literals from the concatenation
                strings = re.findall(r'["\']([^"\']+)["\']', host_line)
                if strings and len(strings) > 1:
                    # Join them with * to indicate dynamic parts
                    # E.g., ["rds.", ".amazonaws.com"] -> "rds.*.amazonaws.com"
                    parts = []
                    for i, s in enumerate(strings):
                        if i == 0:
                            parts.append(s.rstrip('.'))
                        elif i == len(strings) - 1:
                            parts.append(s.lstrip('.'))
                        else:
                            parts.append(s.strip('.'))
                    request_info['host'] = '.*.'.join(parts)
                elif strings:
                    request_info['host'] = strings[0]
            else:
                # Check if it's an object/array access pattern first (e.g., ds_flexera_api_hosts["flexera"])
                if '[' in host_line and ']' in host_line:
                    # Extract the key being accessed
                    key_match = re.search(r'\["?([^"\]]+)"?\]', host_line)
                    if key_match:
                        key = key_match.group(1)
                        # If accessing with "flexera" key or similar, it's a Flexera API
                        if 'flexera' in key.lower() or 'flexera' in host_line.lower():
                            request_info['host'] = 'flexera_api_host'
                # Check if it's a simple string literal
                elif re.search(r'^["\'][^"\']+["\']$', host_line):
                    # Only match if the ENTIRE line is a quoted string
                    host_match = re.search(r'["\']([^"\']+)["\']', host_line)
                    if host_match:
                        request_info['host'] = host_match.group(1)
                else:
                    # It's a variable reference - check if it's a Flexera built-in
                    var_name = host_line.strip()
                    if var_name in ['rs_optima_host', 'rs_governance_host']:
                        # These are Flexera built-in variables
                        request_info['host'] = var_name
                    else:
                        # Try to resolve it from script parameters or policy file
                        param_resolved = self._resolve_parameter_from_content(var_name)
                        if param_resolved:
                            request_info['host'] = param_resolved
        
        # Extract path from JavaScript - handle both simple strings and array joins
        # Try array join pattern first: [ "/v3/projects/", projectId, "/timeSeries:query" ].join('')
        path_join_match = re.search(r'path:\s*\[\s*([^\]]+)\]\s*\.join\([^\)]*\)', js_code)
        if path_join_match:
            path_parts_str = path_join_match.group(1)
            # Extract string literals from the array
            strings = re.findall(r'["\']([^"\']+)["\']', path_parts_str)
            if strings:
                # Join them but replace variables with placeholders
                # Count commas to determine if there are variables
                parts_count = len(path_parts_str.split(','))
                strings_count = len(strings)
                if parts_count > strings_count:
                    # Has variables - insert placeholders
                    path_with_vars = ''
                    for s in strings:
                        path_with_vars += s + '/{dynamic}'
                    # Remove trailing placeholder if path ends with a string
                    if path_parts_str.strip().endswith('"') or path_parts_str.strip().endswith("'"):
                        if path_with_vars.endswith('/{dynamic}'):
                            path_with_vars = path_with_vars[:-10]  # Remove last '/{dynamic}'
                    request_info['path'] = path_with_vars
                else:
                    request_info['path'] = ''.join(strings)
        else:
            # Check if path uses concatenation
            path_line_match = re.search(r'path:\s*([^,\n]+)', js_code)
            if path_line_match:
                path_line = path_line_match.group(1).strip()
                if '+' in path_line:
                    # Try concatenation pattern: "string" + variable + "string"
                    # Extract all string literals from the concatenation
                    strings = re.findall(r'["\']([^"\']+)["\']', path_line)
                    if strings:
                        # Build path with placeholders for variables
                        # E.g., "subscriptions/" + var + "/metrics" -> "subscriptions/{dynamic}/metrics"
                        path_with_vars = ''
                        for s in strings:
                            path_with_vars += s + '/{dynamic}'
                        # Remove trailing placeholder if path ends with a string
                        if path_line.strip().endswith('"') or path_line.strip().endswith("'"):
                            if path_with_vars.endswith('/{dynamic}'):
                                path_with_vars = path_with_vars[:-10]  # Remove last '/{dynamic}'
                        request_info['path'] = path_with_vars
                else:
                    # Simple string literal
                    path_match = re.search(r'["\']([^"\']+)["\']', path_line)
                    if path_match:
                        request_info['path'] = path_match.group(1)
        
        # Extract query_params object from JavaScript
        query_params_match = re.search(r'query_params:\s*\{([^}]+)\}', js_code, re.DOTALL)
        if query_params_match:
            params_str = query_params_match.group(1)
            # Extract key-value pairs from the query_params object
            param_pattern = r'["\']([^"\']+)["\']\s*:\s*["\']([^"\']+)["\']'
            for param_match in re.finditer(param_pattern, params_str):
                key = param_match.group(1)
                value = param_match.group(2)
                request_info['query_params'][key] = value
        
        # Extract body_fields object from JavaScript
        body_fields_match = re.search(r'body_fields:\s*\{([^}]+)\}', js_code, re.DOTALL)
        if body_fields_match:
            params_str = body_fields_match.group(1)
            # Extract key-value pairs
            param_pattern = r'["\']([^"\']+)["\']'
            keys = re.findall(param_pattern, params_str)
            if keys:
                for key in keys:
                    request_info['body_params'][key] = '{dynamic}'
        
        # Extract body with JSON.stringify
        body_match = re.search(r'body:\s*JSON\.stringify\(\{([^}]+)\}\)', js_code)
        if body_match:
            params_str = body_match.group(1)
            # Extract key-value pairs
            param_pattern = r'["\']([^"\']+)["\']'
            keys = re.findall(param_pattern, params_str)
            if keys:
                for key in keys:
                    request_info['body_params'][key] = '{dynamic}'
        
        return request_info
    
    def _extract_fields_from_processing_script(self, datasource_body):
        """
        Extract fields that are accessed from the API response in subsequent processing scripts.
        These are fields accessed in scripts that process datasources.
        """
        fields = []
        
        # Look for patterns where the datasource is passed to a run_script after the request
        # This indicates the response is being processed
        # Pattern: datasource "ds_name" do ... end followed by another datasource that processes it
        
        # Find scripts that reference this datasource's output
        # Common patterns:
        # - entry['field_name'] or entry["field_name"]
        # - item['field_name'] or item["field_name"]
        # - result['field_name'] or result["field_name"]
        # - .pluck('field_name')
        
        # Look for JavaScript field access patterns in associated scripts
        script_refs = re.findall(r'run_script\s+\$(\w+)', datasource_body)
        
        for script_ref in script_refs:
            script_fields = self._extract_fields_from_script(script_ref)
            fields.extend(script_fields)
        
        return fields
    
    def _extract_fields_from_script(self, script_name):
        """Extract fields accessed in a JavaScript processing script."""
        fields = []
        
        # Find the script definition
        script_pattern = rf'script\s+"{script_name}".*?do\s+(.*?)\nend'
        script_match = re.search(script_pattern, self.content, re.DOTALL)
        
        if not script_match:
            return fields
        
        script_body = script_match.group(1)
        
        # Extract the JavaScript code
        code_pattern = r'code\s+<<-[\'"]?EOS[\'"]?\s+(.*?)EOS'
        code_match = re.search(code_pattern, script_body, re.DOTALL)
        
        if not code_match:
            return fields
        
        js_code = code_match.group(1)
        
        # Extract field access patterns
        # Patterns like: entry['fieldName'], item["fieldName"], result['fieldName']
        field_patterns = [
            r'(?:entry|item|result|metric|instance|data|col_item|response|obj)\[["\']([^"\']+)["\']\]',
            r'\.pluck\(["\']([^"\']+)["\']\)',
            # Also catch dot notation for nested objects
            r'(?:entry|item|result|metric|instance|data)\.(\w+)',
        ]
        
        seen_fields = set()
        for pattern in field_patterns:
            for match in re.finditer(pattern, js_code):
                field_name = match.group(1)
                # Filter out common programming keywords and loop variables
                if field_name not in ['i', 'j', 'k', 'index', 'length', 'key', 'value', 'each', 'map', 'forEach']:
                    if field_name not in seen_fields:
                        fields.append(field_name)
                        seen_fields.add(field_name)
        
        return fields
    
    def _extract_fields(self, datasource_body):
        """Extract fields from the result block of a datasource."""
        fields = []
        
        # Find result block - need to handle nested do/end
        result_start = datasource_body.find('result do')
        if result_start == -1:
            return fields
        
        # Extract the result block with proper nesting
        lines = datasource_body[result_start:].split('\n')
        result_lines = []
        depth = 0
        started = False
        
        for line in lines:
            if not started and 'result do' in line:
                started = True
                depth = 1
                continue
            
            if started:
                if re.search(r'\bdo\s*$', line):
                    depth += 1
                elif re.match(r'^\s*end\s*$', line):
                    depth -= 1
                    if depth == 0:
                        break
                result_lines.append(line)
        
        result_body = '\n'.join(result_lines)
        
        # Extract field definitions with xpath
        # Pattern: field "fieldName", xpath(col_item, "XPathValue")
        xpath_pattern = r'field\s+"([^"]+)",\s+xpath\([^,]+,\s+"([^"]+)"\)'
        for match in re.finditer(xpath_pattern, result_body):
            field_name = match.group(1)
            xpath_value = match.group(2)
            fields.append(xpath_value)  # Use the API field name, not our internal name
        
        # Extract field definitions with jmes_path
        # Pattern: field "fieldName", jmes_path(col_item, "jmesPath")
        jmes_pattern = r'field\s+"([^"]+)",\s+jmes_path\([^,]+,\s+"([^"]+)"\)'
        for match in re.finditer(jmes_pattern, result_body):
            field_name = match.group(1)
            jmes_path = match.group(2)
            # Extract the actual field name from jmes_path
            # e.g., "dimensions.vendor_account" -> "vendor_account"
            # e.g., "aws.accountId" -> "accountId"
            # e.g., "values[*]" -> "values"
            # Handle array notation
            if '[' in jmes_path:
                # Extract base field before array notation
                base_field = jmes_path.split('[')[0]
                if base_field:
                    fields.append(base_field)
                else:
                    fields.append(jmes_path)
            else:
                path_parts = jmes_path.split('.')
                if len(path_parts) > 1:
                    api_field = path_parts[-1]
                else:
                    api_field = jmes_path
                fields.append(api_field)
        
        # Extract field definitions with val()
        # Pattern: field "fieldName", val(...)
        # These typically reference iterator or parameter values, not API responses
        # We'll skip these as they're not from the API response
        
        return fields
    
    def _build_endpoint_url(self, request_info):
        """Build the full endpoint URL from request information."""
        if not request_info.get('host'):
            return None
        
        host = request_info['host']
        path = request_info.get('path', '/')
        
        # Wrap policy language constructs in curly braces
        policy_variables = ['rs_optima_host', 'rs_governance_host', 'flexera_api_host', 'rs_org_id', 'rs_project_id']
        for var in policy_variables:
            if var in host:
                host = host.replace(var, f'{{{var}}}')
        
        # Ensure path starts with /
        if not path.startswith('/'):
            path = '/' + path
        
        # Replace empty path segments with placeholders
        # Pattern: /orgs// or /orgs/{dynamic}/ -> /orgs/{org}/
        path = re.sub(r'/orgs/(?:\{dynamic\}|)/(?!$)', '/orgs/{org}/', path)
        path = re.sub(r'/projects/(?:\{dynamic\}|)/(?!$)', '/projects/{project}/', path)
        path = re.sub(r'/billing_centers/(?:\{dynamic\}|)/(?!$)', '/billing_centers/{billing_center}/', path)
        path = re.sub(r'/subscriptions/(?:\{dynamic\}|)/(?!$)', '/subscriptions/{subscription}/', path)
        path = re.sub(r'/resourceGroups/(?:\{dynamic\}|)/(?!$)', '/resourceGroups/{resource_group}/', path)
        
        # Replace generic double slashes with {id}
        path = re.sub(r'//+', '/{id}/', path)
        
        # Clean up multiple slashes that might have been created
        path = re.sub(r'/+', '/', path)
        
        # Build URL
        url = f"https://{host}{path}"
        
        # Add query parameters if any
        if request_info.get('query_params'):
            params = []
            for key, value in request_info['query_params'].items():
                params.append(f"{key}={value}")
            if params:
                url += "?" + "&".join(params)
        
        # Add body parameters if any
        if request_info.get('body_params'):
            params = []
            for key, value in request_info['body_params'].items():
                params.append(f"{key}={value}")
            if params:
                # Indicate body params in the URL using a special marker
                url += " [BODY: " + ", ".join(params) + "]"
        
        return url
    
    def extract_api_calls(self):
        """Extract all API calls from the policy template."""
        api_calls = []
        
        datasources = self._extract_datasources()
        
        for datasource in datasources:
            request_info = self._extract_request_info(datasource['body'])
            
            if not request_info['has_request']:
                continue
            
            # If request uses a script, extract info from the script
            if request_info['script_name']:
                script_request = self._extract_request_from_script(request_info['script_name'])
                if script_request:
                    # Merge script request info
                    if script_request['host']:
                        request_info['host'] = script_request['host']
                    if script_request['path']:
                        request_info['path'] = script_request['path']
                    if script_request['method']:
                        request_info['method'] = script_request['method']
                    if script_request['query_params']:
                        request_info['query_params'].update(script_request['query_params'])
                    if script_request.get('body_params'):
                        request_info['body_params'] = script_request['body_params']
            
            # Process all API calls (not just cloud providers)
            if request_info['host']:
                # Determine which service this API call targets
                api_service = self._determine_api_service(request_info['host'])
                
                # Extract fields from the response
                fields = self._extract_fields(datasource['body'])
                
                # Also extract fields from processing scripts
                processing_fields = self._extract_fields_from_processing_script(datasource['body'])
                fields.extend(processing_fields)
                
                # Deduplicate fields while preserving order
                seen = set()
                unique_fields = []
                for field in fields:
                    if field not in seen:
                        unique_fields.append(field)
                        seen.add(field)
                
                # Build the endpoint URL
                endpoint = self._build_endpoint_url(request_info)
                
                if endpoint:
                    # If no fields found, add at least one entry for the API call
                    if not unique_fields:
                        api_calls.append({
                            'policy_name': self.policy_name,
                            'method': request_info['method'],
                            'endpoint': endpoint,
                            'field': '',
                            'api_service': api_service
                        })
                    else:
                        # Add one entry per field
                        for field in unique_fields:
                            api_calls.append({
                                'policy_name': self.policy_name,
                                'method': request_info['method'],
                                'endpoint': endpoint,
                                'field': field,
                                'api_service': api_service
                            })
        
        return api_calls


def main():
    """Main function to run the script."""
    # Get the repository root directory (two levels up from script location)
    script_path = Path(__file__).resolve() if '__file__' in globals() else Path.cwd()
    repo_root = script_path.parent.parent.parent if '__file__' in globals() else Path.cwd()
    
    # Path to active policy list
    active_policy_list_file = repo_root / 'data' / 'active_policy_list' / 'active_policy_list.json'
    
    if not active_policy_list_file.exists():
        print(f"Error: Active policy list not found: {active_policy_list_file}", file=sys.stderr)
        sys.exit(1)
    
    # Load active policy list
    with open(active_policy_list_file, 'r') as f:
        active_policies = json.load(f)
    
    policies = active_policies.get('policies', [])
    if not policies:
        print("Error: No policies found in active_policy_list.json", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing {len(policies)} policy templates...")
    
    # Collect all API calls
    all_api_calls = []
    processed_count = 0
    error_count = 0
    
    for policy_info in policies:
        policy_file = repo_root / policy_info['file_name']
        
        if not policy_file.exists():
            print(f"Warning: Policy file not found: {policy_file}", file=sys.stderr)
            error_count += 1
            continue
        
        try:
            # Parse the policy template
            parser = PolicyTemplateParser(str(policy_file))
            api_calls = parser.extract_api_calls()
            
            # Add policy metadata to each API call
            for call in api_calls:
                call['policy_file'] = policy_info['file_name']
                call['policy_version'] = policy_info.get('version', '')
            
            all_api_calls.extend(api_calls)
            processed_count += 1
            
            if processed_count % 50 == 0:
                print(f"  Processed {processed_count}/{len(policies)} policies...")
        
        except Exception as e:
            print(f"Error processing {policy_file}: {e}", file=sys.stderr)
            error_count += 1
    
    print(f"\nProcessed {processed_count} policies successfully, {error_count} errors")
    print(f"Extracted {len(all_api_calls)} total API call fields")
    
    # Create output directory if it doesn't exist
    output_dir = repo_root / 'data' / 'policy_api_list'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Write to JSON
    json_output_file = output_dir / 'policy_api_list.json'
    with open(json_output_file, 'w') as f:
        json.dump({
            'metadata': {
                'total_policies': processed_count,
                'total_api_calls': len(all_api_calls),
                'generated_at': Path(active_policy_list_file).stat().st_mtime
            },
            'api_calls': all_api_calls
        }, f, indent=2)
    
    print(f"JSON output written to: {json_output_file}")
    
    # Write to CSV
    csv_output_file = output_dir / 'policy_api_list.csv'
    with open(csv_output_file, 'w', newline='') as csvfile:
        fieldnames = ['policy_name', 'policy_file', 'policy_version', 'api_service', 'method', 'endpoint', 'field']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for call in all_api_calls:
            writer.writerow(call)
    
    print(f"CSV output written to: {csv_output_file}")


if __name__ == '__main__':
    main()
