"""
Extract REST API calls from Flexera Policy Templates.

This script parses Flexera policy template (.pt) files and extracts information about
all REST API calls, including the HTTP method, endpoint URL, target service (AWS, Azure,
GCP, Oracle, Flexera, etc.), and fields extracted from the response.

Usage:
    python policy_api_list_generator.py [--output-dir DIR]

    --output-dir DIR  Write output files to DIR instead of the default
                      data/policy_api_list/ directory. Useful for writing to
                      a temporary location (e.g. /tmp) in CI pipelines.

The script will process all policies listed in data/active_policy_list/active_policy_list.json
and output results to:
    - <output-dir>/policy_api_list.json
    - <output-dir>/policy_api_list.csv
"""

import sys
import re
import csv
import json
import argparse
import urllib.parse
from pathlib import Path


class PolicyTemplateParser:
    """Parser for Flexera Policy Template files."""

    # Service patterns to identify which service/cloud the API call targets
    # Order matters - more specific patterns should come first
    SERVICE_PATTERNS = {
        'Turbonomic': [
            r'turbonomic',  # Turbonomic (IBM) instances
            r'turbonomic_host',  # Turbonomic host variable
            r'^flexera$',  # Turbonomic API with flexera as placeholder host
        ],
        'AWS': [
            r'amazonaws\.com',
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
            r'^api_host$',  # CWF variable resolved from dict field (e.g. $policy["api_host"])
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

    # Maps common CWF host variable expressions to resolved host values
    CWF_HOST_MAP = {
        'rs_optima_host': 'rs_optima_host',
        '$rs_optima_host': 'rs_optima_host',
        '$$rs_optima_host': 'rs_optima_host',
        'optima_host': 'rs_optima_host',
        'rs_governance_host': 'rs_governance_host',
        '$governance_host': 'rs_governance_host',
        '$$governance_host': 'rs_governance_host',
        'governance_host': 'rs_governance_host',
        '$param_azure_endpoint': 'management.azure.com',
        'param_azure_endpoint': 'management.azure.com',
        '$$flexera_api_host': 'flexera_api_host',
        'flexera_api_host': 'flexera_api_host',
        '$flexera_api_host': 'flexera_api_host',
        'api_host': 'flexera_api_host',
        'turbonomic_endpoint': 'turbonomic_host',
        'param_turbonomic_host': 'turbonomic_host',
        '$param_turbonomic_host': 'turbonomic_host',
    }

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.content = self.file_path.read_text()
        self.policy_name = self._extract_policy_name()

    def _extract_policy_name(self):
        """Extract the policy template name from the file."""
        match = re.search(r'^name\s+"([^"]+)"', self.content, re.MULTILINE)
        return match.group(1) if match else self.file_path.stem

    def _get_semantic_placeholder(self, var_name):
        """Map a variable name to a semantic placeholder.

        Args:
            var_name: Variable name (e.g., 'region', 'account_id', 'subscription')

        Returns:
            Semantic placeholder string (e.g., '{region}', '{account}', '{subscription}')
        """
        var_lower = var_name.lower()

        # Map common variable names to placeholders
        if 'region' in var_lower or 'homeregion' in var_lower:
            return '{region}'
        elif 'subscription' in var_lower:
            return '{subscription}'
        elif 'account' in var_lower:
            return '{account}'
        elif 'bucket' in var_lower:
            return '{bucket}'
        elif 'org' in var_lower:
            return '{org}'
        elif 'project' in var_lower:
            return '{project}'
        elif 'zone' in var_lower:
            return '{zone}'
        else:
            return '{id}'

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
            # Escape special characters in parameter name (should be safe with \w+ but defensive)
            escaped_param_name = re.escape(param_name)
            # Find the parameter definition and extract its default value
            param_pattern = rf'parameter\s+"param_{escaped_param_name}".*?default\s+"([^"]+)"'
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

        # Escape special regex characters in the variable name
        escaped_var_name = re.escape(var_name)

        # Match parameter block and extract default value from within it only.
        # We stop at 'end' to avoid bleeding across parameter boundaries.
        param_pattern = rf'parameter\s+"{escaped_var_name}"\s+do(.*?)^end\b'
        param_match = re.search(param_pattern, self.content, re.DOTALL | re.MULTILINE)

        if param_match:
            block_body = param_match.group(1)
            default_match = re.search(r'default\s+"([^"]+)"', block_body)
            if default_match:
                return default_match.group(1)

        return None

    def _determine_api_service(self, host, path=None):
        """Determine which service/cloud the API call is targeting based on the host.

        Returns:
            str: The service name (e.g., 'AWS', 'Azure', 'Flexera') or 'Unknown' if not recognized.
        """
        if not host:
            return 'Unknown'

        # Databricks uses dynamic workspace URLs; /api/2.0/ paths indicate Azure Databricks
        if host == '{dynamic_host}' and path and '/api/2.0/' in path:
            return 'Azure'

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

                    # Ignore commented lines for depth tracking
                    if not re.match(r'^\s*#', current_line):
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
            'body_params': {},
            'headers': {}
        }

        # Check if datasource has a request block OR uses run_script directly
        has_request_block = 'request do' in datasource_body
        has_direct_script = re.search(r'^\s*run_script\s+\$', datasource_body, re.MULTILINE)

        if not has_request_block and not has_direct_script:
            return request_info

        request_info['has_request'] = True

        # Extract HTTP verb/method
        verb_match = re.search(r'verb\s+"([^"]+)"', datasource_body, re.IGNORECASE)
        if verb_match:
            request_info['method'] = verb_match.group(1).upper()
        else:
            # Handle ternary expressions like: verb ds_parent_policy_terminated ? "DELETE" : "GET"
            ternary_match = re.search(r'\bverb\s+\w+\s*\?\s*"([^"]+)"\s*:\s*"([^"]+)"', datasource_body)
            if ternary_match:
                request_info['method'] = ternary_match.group(1).upper()

        # Extract host (including join pattern)
        host_match = re.search(r'host\s+join\(\[([^\]]+)\]\)', datasource_body)
        if host_match:
            join_content = host_match.group(1)

            try:
                # Extract quoted strings from the join array, but exclude strings inside function calls
                # First, temporarily replace val() calls with placeholders
                temp_content = re.sub(r'val\([^)]+\)', 'VAL_PLACEHOLDER', join_content)
                # Now extract string literals (these are the actual hostname parts)
                host_parts = re.findall(r'["\']([^"\']+)["\']', temp_content)
            except re.error as e:
                # If regex fails, skip this datasource
                return request_info

            # Extract variable names from the join array
            # Look for variable patterns: $param_region, val(iter_item, 'region'), etc.
            variables = []

            # Extract $param_xxx variables
            param_vars = re.findall(r'\$param_(\w+)', join_content)
            variables.extend(param_vars)

            # Extract val(iter_item, 'xxx') patterns
            val_vars = re.findall(r'val\(iter_item,\s*["\']([^"\']+)["\']', join_content)
            variables.extend(val_vars)

            # Extract other $variable patterns
            other_vars = re.findall(r'\$(\w+)', join_content)
            variables.extend([v for v in other_vars if not v.startswith('param_')])

            has_dynamic = len(variables) > 0 or 'iter_item' in join_content

            if has_dynamic:
                # Build host with semantic placeholders based on variable names
                if len(host_parts) > 1:
                    # Multiple parts - join with placeholders between them
                    host_with_vars = ''
                    var_idx = 0
                    for i, part in enumerate(host_parts):
                        host_with_vars += part
                        # Add placeholder between parts (except after last part)
                        if i < len(host_parts) - 1:
                            if var_idx < len(variables):
                                var_name = variables[var_idx]
                                # Map variable name to semantic placeholder
                                placeholder = self._get_semantic_placeholder(var_name)
                                var_idx += 1
                            else:
                                placeholder = '{dynamic}'
                            host_with_vars += placeholder
                    request_info['host'] = host_with_vars
                elif len(host_parts) == 1:
                    # Single part with dynamic variable
                    items = [x.strip() for x in join_content.split(',')]
                    if len(items) > len(host_parts):
                        # Has variables - add placeholders
                        if variables:
                            placeholder = self._get_semantic_placeholder(variables[0])
                        else:
                            placeholder = '{dynamic}'

                        if join_content.startswith('"') or join_content.startswith("'"):
                            # Starts with string: "ec2." + region + ...
                            request_info['host'] = host_parts[0] + placeholder
                        elif join_content.endswith('"') or join_content.endswith("'"):
                            # Ends with string: ... + region + ".amazonaws.com"
                            request_info['host'] = placeholder + host_parts[0]
                        else:
                            request_info['host'] = placeholder + '.' + host_parts[0]
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
                    val_content = val_match.group(0)
                    # Check if it's val(iter_item, ...) - this means dynamic host from iteration
                    if 'iter_item' in val_content:
                        # This is iterating over data from previous datasource
                        # Try to infer the service from auth or other context
                        if 'auth $auth_aws' in datasource_body:
                            # AWS authentication - likely S3 bucket host
                            request_info['host'] = '{bucket}.s3.amazonaws.com'
                        elif 'auth $auth_azure' in datasource_body or 'auth $auth_google' in datasource_body:
                            # Other cloud - use generic placeholder
                            request_info['host'] = '{dynamic_host}'
                        else:
                            # Unknown - use generic placeholder
                            request_info['host'] = '{dynamic_host}'
                    else:
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
            try:
                join_content = path_match.group(1)

                # Parse the join array to maintain proper order of strings and val() calls
                # Split by comma but be careful with nested function calls
                parts = []
                current_part = ''
                depth = 0

                for char in join_content + ',':
                    if char in '([':
                        depth += 1
                        current_part += char
                    elif char in ')]':
                        depth -= 1
                        current_part += char
                    elif char == ',' and depth == 0:
                        part = current_part.strip()
                        if part:
                            parts.append(part)
                        current_part = ''
                    else:
                        current_part += char

                # Now process each part to extract strings or val() placeholders
                path_result = ''
                for part in parts:
                    part = part.strip()
                    # Check if it's a val(iter_item, "xxx") call
                    val_match = re.search(r'val\(iter_item,\s*["\']([^"\']+)["\']\)', part)
                    if val_match:
                        path_result += '{' + val_match.group(1) + '}'
                    else:
                        # Check if it's a quoted string
                        string_match = re.search(r'^["\']([^"\']+)["\']$', part)
                        if string_match:
                            path_result += string_match.group(1)
                        elif 'val(' in part:
                            # Other val() patterns (not iter_item) - use generic placeholder
                            path_result += '{dynamic}'
                        # Skip other patterns (variables, etc.)

                request_info['path'] = path_result

                # If path starts with '{id}' the datasource path is relative to the iterator's
                # resource ID (e.g. join([val(iter_item, "id"), "/configurations/", ...])).
                # Resolve the iterate parent's full ARM path and build the complete path.
                if path_result.startswith('{id}') and '/providers/' not in path_result:
                    iter_ds_m = re.search(r'\biterate\s+\$(ds_\w+)', datasource_body)
                    if iter_ds_m:
                        try:
                            parent_h, parent_p = self._trace_datasource_api(
                                iter_ds_m.group(1), 1, set()
                            )
                            if parent_h and parent_p and '/providers/' in (parent_p or ''):
                                rest = re.sub(r'^\{id\}', '', path_result)
                                request_info['path'] = parent_p.rstrip('/') + '/{id}' + rest
                        except Exception:
                            pass
            except Exception as e:
                # If parsing fails, use placeholder
                request_info['path'] = '/{dynamic}'
        else:
            # Try simple path pattern with single or double quotes
            path_match = re.search(r'path\s+["\']([^"\']+)["\']', datasource_body)
            if path_match:
                request_info['path'] = path_match.group(1)
            else:
                # Check for val() or other dynamic expressions - use placeholder
                path_val_match = re.search(r'path\s+(val\(|iter_item)', datasource_body)
                if path_val_match:
                    # When the field name hints at a known ARM resource type, synthesize the path.
                    arm_field_match = re.search(
                        r'path\s+val\s*\([^,]+,\s*["\'](\w+)["\']\s*\)', datasource_body)
                    FIELD_TO_ARM_PATH = {
                        'vmId': '/subscriptions/{id}/resourceGroups/{rg}/providers/'
                                'Microsoft.Compute/virtualMachines/{name}',
                    }
                    if arm_field_match and arm_field_match.group(1) in FIELD_TO_ARM_PATH:
                        request_info['path'] = FIELD_TO_ARM_PATH[arm_field_match.group(1)]
                    else:
                        request_info['path'] = '/{dynamic}'
                else:
                    request_info['path'] = '/'

        # Check for run_script in request
        script_match = re.search(r'run_script\s+\$([^,\s]+)', datasource_body)
        if script_match:
            request_info['script_name'] = script_match.group(1)

        # Extract query parameters (with double or single quotes, allow empty values)
        for query_match in re.finditer(r'query\s+["\']([^"\']+)["\']\s*,\s*["\']([^"\']*)["\']', datasource_body):
            param_name = query_match.group(1)
            param_value = query_match.group(2)
            request_info['query_params'][param_name] = param_value
        # Also capture query directives with dynamic values (val(), variables, etc.)
        for query_match in re.finditer(r'query\s+["\']([^"\']+)["\']\s*,\s*(?!["\'])([^\n]+)', datasource_body):
            param_name = query_match.group(1)
            if param_name not in request_info['query_params']:
                request_info['query_params'][param_name] = '{dynamic}'

        # Extract headers (with double or single quotes)
        for header_match in re.finditer(r'header\s+["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']', datasource_body):
            header_name = header_match.group(1)
            header_value = header_match.group(2)
            request_info['headers'][header_name] = header_value

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
            'body_params': {},
            'headers': {}
        }

        # Extract verb from JavaScript
        verb_match = re.search(r'verb:\s*["\']([^"\']+)["\']', js_code)
        if verb_match:
            request_info['method'] = verb_match.group(1).upper()
        else:
            # Handle ternary: verb: condition ? "DELETE" : "GET"
            ternary_match = re.search(r'\bverb:\s*\w+\s*\?\s*"([^"]+)"\s*:\s*"([^"]+)"', js_code)
            if ternary_match:
                request_info['method'] = ternary_match.group(1).upper()

        # Extract host from JavaScript
        # Look for the entire host line first
        # Handle array.join() pattern: [ "tagging.", region, ".amazonaws.com" ].join('')
        host_array_join_match = re.search(r'host:\s*\[\s*([^\]]+)\]\s*\.join\([^\)]*\)', js_code)
        if host_array_join_match:
            array_content = host_array_join_match.group(1)
            # Extract string literals
            strings = re.findall(r'["\']([^"\']+)["\']', array_content)
            # Extract variable names
            variables = re.findall(r'(?:,\s*)(\w+)(?:\s*,|\s*$)', array_content)

            if strings:
                # Build host with semantic placeholders
                host_with_vars = ''
                var_idx = 0
                for i, s in enumerate(strings):
                    # Don't strip dots from strings, just use as-is
                    host_with_vars += s
                    # Add placeholder between parts
                    if i < len(strings) - 1:
                        if var_idx < len(variables):
                            placeholder = self._get_semantic_placeholder(variables[var_idx])
                            var_idx += 1
                        else:
                            placeholder = '{dynamic}'
                        host_with_vars += placeholder
                request_info['host'] = host_with_vars
        else:
            # Fall back to simpler patterns
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
                            # Extract variable names
                            variables = re.findall(r'\b(\w+)\s*\+', return_expr)

                            if strings:
                                # Build host with semantic placeholders
                                host_with_vars = ''
                                var_idx = 0
                                for i, s in enumerate(strings):
                                    s_clean = s.lstrip('.')
                                    host_with_vars += s_clean
                                    # Add placeholder between parts
                                    if i < len(strings) - 1:
                                        if var_idx < len(variables):
                                            placeholder = self._get_semantic_placeholder(variables[var_idx])
                                            var_idx += 1
                                        else:
                                            placeholder = '{dynamic}'
                                        host_with_vars += placeholder
                                request_info['host'] = host_with_vars
                            else:
                                # No strings found, use a generic pattern
                                request_info['host'] = '{region}.monitor.azure.com' if 'azure' in func_body.lower() else None
                # Check if this is a concatenated string (contains +)
                elif '+' in host_line:
                    # Extract all string literals from the concatenation
                    strings = re.findall(r'["\']([^"\']+)["\']', host_line)
                    # Extract variable names
                    variables = re.findall(r'\+\s*(\w+)\s*\+', host_line)

                    if strings and len(strings) > 1:
                        # Join them with semantic placeholders between
                        parts = []
                        var_idx = 0
                        for i, s in enumerate(strings):
                            if i == 0:
                                parts.append(s.rstrip('.'))
                            elif i == len(strings) - 1:
                                parts.append(s.lstrip('.'))
                            else:
                                parts.append(s.strip('.'))

                            # Add placeholder between parts (except after last)
                            if i < len(strings) - 1:
                                if var_idx < len(variables):
                                    placeholder = self._get_semantic_placeholder(variables[var_idx])
                                    var_idx += 1
                                else:
                                    placeholder = '{dynamic}'
                                parts.append(placeholder)

                        request_info['host'] = '.'.join(parts)
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
                            elif 'turbonomic' in var_name.lower():
                                request_info['host'] = 'turbonomic_host'

        # Extract path from JavaScript - handle both simple strings and array joins
        # Try array join pattern first: [ "/v3/projects/", projectId, "/timeSeries:query" ].join('')
        # Use a pattern that tolerates inner brackets from object-property accesses like obj['key'].
        path_join_match = re.search(
            r'path:\s*\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\s*\.join\([^\)]*\)', js_code)
        if path_join_match:
            path_parts_str = path_join_match.group(1)
            # Strip dict/array access brackets (e.g. ['subscriptionId'] or ["id"]) before
            # extracting string literals so inner keys are not mistaken for path segments.
            path_parts_clean = re.sub(r'\[["\'][^"\']*["\']\]', '', path_parts_str)
            # Extract string literals from the array
            strings = re.findall(r'["\']([^"\']+)["\']', path_parts_clean)
            # Extract variable names from the array
            variables = re.findall(r'(?:,\s*)(\w+)(?:\s*,|\s*$)', path_parts_clean)

            if strings:
                # Join them but replace variables with placeholders
                # Count commas to determine if there are variables
                parts_count = len(path_parts_clean.split(','))
                strings_count = len(strings)
                if parts_count > strings_count:
                    # Has variables - insert semantic placeholders
                    path_with_vars = ''
                    var_idx = 0

                    for i, s in enumerate(strings):
                        path_with_vars += s
                        # Add placeholder for variable between this and next string
                        if i < len(strings) - 1 or not (path_parts_str.strip().endswith('"') or path_parts_str.strip().endswith("'")):
                            # Determine the placeholder based on variable name if available
                            if var_idx < len(variables):
                                var_name = variables[var_idx]
                                # Map common variable names to semantic placeholders
                                if 'org' in var_name.lower():
                                    placeholder = '{org}'
                                elif 'project' in var_name.lower():
                                    placeholder = '{project}'
                                elif 'subscription' in var_name.lower():
                                    placeholder = '{subscription}'
                                elif 'billing' in var_name.lower() or 'bc' in var_name.lower():
                                    placeholder = '{billing_center}'
                                elif 'region' in var_name.lower():
                                    placeholder = '{region}'
                                else:
                                    placeholder = '{id}'
                                var_idx += 1
                            else:
                                placeholder = '{id}'
                            path_with_vars += placeholder

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
                    # Extract all string literals and variable names from the concatenation
                    strings = re.findall(r'["\']([^"\']+)["\']', path_line)

                    # Also extract variable names to provide better placeholders
                    # Look for common variable patterns between the strings
                    variables = re.findall(r'\+\s*(\w+)\s*\+', path_line)

                    if strings:
                        # Build path with placeholders for variables
                        # Use semantic placeholders based on variable names
                        path_with_vars = ''
                        var_idx = 0

                        for i, s in enumerate(strings):
                            path_with_vars += s
                            # Add placeholder for variable between this and next string
                            if i < len(strings) - 1 or not (path_line.strip().endswith('"') or path_line.strip().endswith("'")):
                                # Determine the placeholder based on variable name if available
                                if var_idx < len(variables):
                                    var_name = variables[var_idx]
                                    # Map common variable names to semantic placeholders
                                    if 'org' in var_name.lower():
                                        placeholder = '{org}'
                                    elif 'project' in var_name.lower():
                                        placeholder = '{project}'
                                    elif 'subscription' in var_name.lower():
                                        placeholder = '{subscription}'
                                    elif 'billing' in var_name.lower() or 'bc' in var_name.lower():
                                        placeholder = '{billing_center}'
                                    elif 'region' in var_name.lower():
                                        placeholder = '{region}'
                                    else:
                                        placeholder = '{id}'
                                    var_idx += 1
                                else:
                                    placeholder = '{id}'
                                path_with_vars += placeholder

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
            # Match both quoted keys ("key": "value") and unquoted JS keys (key: "value").
            # Values may be empty strings.
            param_pattern = r'(?:["\']([^"\']+)["\']\s*|(\w+)\s*):\s*["\']([^"\']*)["\']'
            for param_match in re.finditer(param_pattern, params_str):
                key = param_match.group(1) or param_match.group(2)
                value = param_match.group(3)
                if key:
                    request_info['query_params'][key] = value

        # Fallback: also look for Action in variable-assigned query_params dicts
        # Handles: query_params = { "Action": "DescribeVolumes", ... }
        if 'Action' not in request_info['query_params']:
            action_match = re.search(r'"Action"\s*:\s*"([^"]+)"', js_code)
            if action_match:
                request_info['query_params']['Action'] = action_match.group(1)

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

        # Extract headers from JavaScript (e.g., "headers": { "X-Amz-Target": "..." })
        headers_match = re.search(r'["\']?headers["\']?\s*:\s*\{([^}]+)\}', js_code, re.DOTALL)
        if headers_match:
            headers_str = headers_match.group(1)
            # Extract key-value pairs from headers object
            header_pairs = re.findall(r'["\']([^"\']+)["\']\s*:\s*["\']([^"\']+)["\']', headers_str)
            for key, value in header_pairs:
                request_info['headers'][key] = value

        # When host couldn't be extracted, infer from auth field in the JS request object.
        if not request_info['host']:
            js_auth_match = re.search(r'\bauth:\s*["\'](\w+)["\']', js_code)
            if js_auth_match and 'aws' in js_auth_match.group(1).lower():
                _S3_SPECIFIC = {'acl', 'logging', 'encryption', 'uploadId', 'uploads',
                                'tagging', 'versioning', 'publicAccessBlock', 'lifecycle'}
                if request_info['query_params'].keys() & _S3_SPECIFIC:
                    request_info['host'] = '{bucket}.s3.amazonaws.com'
                else:
                    request_info['host'] = 'amazonaws.com'

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
            # Clean up XPath notation - remove leading // and convert paths to field names
            # Examples:
            #   //LocationConstraint -> LocationConstraint
            #   //PublicAccessBlockConfiguration/BlockPublicAcls -> BlockPublicAcls
            #   //VersioningConfiguration/Status -> Status
            clean_field = xpath_value.lstrip('/')
            # If it's a path with /, take the last segment (the actual field name)
            if '/' in clean_field:
                clean_field = clean_field.split('/')[-1]
            fields.append(clean_field)  # Use the cleaned field name

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

        # Skip malformed Monthly/ hosts (broken Flexera CBI URLs with no real hostname)
        if host.startswith('Monthly'):
            return None

        # Wrap policy language constructs in curly braces
        policy_variables = ['rs_optima_host', 'rs_governance_host', 'flexera_api_host', 'turbonomic_host', 'rs_org_id', 'rs_project_id']
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

        return url


    def _get_url_path(self, endpoint):
        """Extract the path portion of a URL, handling various edge cases.

        Returns:
            The path portion of the URL (empty string if no path or just '/')
        """
        # Parse URL to get just the path component
        parsed = urllib.parse.urlparse(endpoint)
        path = parsed.path

        # Normalize: empty or '/' becomes ''
        if not path or path == '/':
            return ''

        # Remove trailing slash
        if path.endswith('/'):
            path = path[:-1]

        return path

    def _format_resource_name(self, name):
        """Format a resource name to be human-readable.

        Converts kebab-case, snake_case, camelCase to Title Case.
        """
        import re
        # Convert camelCase to spaces
        name = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
        # Replace separators with spaces
        name = name.replace('-', ' ').replace('_', ' ')
        # Capitalize each word
        words = name.split()
        return ' '.join(word.capitalize() for word in words)

    def _get_generic_operation_from_method(self, method):
        """Get a generic operation name based on HTTP method.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, PATCH, etc.)

        Returns:
            Generic operation name like 'Get Resource', 'Create Resource', etc.
        """
        method_upper = method.upper()
        if method_upper == 'GET':
            return 'Get Resource'
        elif method_upper == 'POST':
            return 'Create Resource'
        elif method_upper in ('PUT', 'PATCH'):
            return 'Update Resource'
        elif method_upper == 'DELETE':
            return 'Delete Resource'
        else:
            return f'{method_upper} Resource'

    def _extract_operation_name(self, endpoint, method, api_service, request_info):
        """Extract a human-readable operation name from the endpoint and request information.

        Returns the operation being performed (e.g., 'List VirtualNetworkGateways', 'ListAccounts').
        """
        # Known abbreviations and their expansions for various services
        RESOURCE_MAPPINGS = {
            'GCP': {
                'b': 'Buckets',
                'o': 'Objects',
                'iam': 'IAM Policies',
            },
            'AWS': {
                'acls': 'ACLs',
                'cors': 'CORS',
                'encryption': 'Encryption Configuration',
                'lifecycle': 'Lifecycle Configuration',
                'logging': 'Logging Configuration',
                'tagging': 'Tags',
                'versioning': 'Versioning Configuration',
                'location': 'Location',
                'policy': 'Policy',
            },
            'Oracle': {
                'o': 'Object',
                'b': 'Bucket',
            }
        }

        # Placeholder names to skip (these are variable placeholders, not resource names)
        SKIP_PLACEHOLDERS = {
            'name', 'id', 'type', 'value', 'key', 'username', 'account',
            'project', 'subscription', 'resource', 'region', 'zone'
        }

        # AWS: Extract from X-Amz-Target header
        if api_service == 'AWS':
            if request_info.get('headers'):
                for key, value in request_info['headers'].items():
                    if key.lower() == 'x-amz-target':
                        # Format: "AWSOrganizationsV20161128.ListAccounts"
                        if '.' in value:
                            operation = value.split('.')[-1]
                            return operation

            # Check for Action query parameter (only for query-action style AWS services)
            QUERY_ACTION_SERVICES_OP = {
                'ec2', 'sts', 'iam', 'autoscaling', 'elasticloadbalancing', 'elb',
                'monitoring', 'cloudwatch', 'sqs', 'rds', 'sns', 'cloudformation',
                'organizations', 'ecs', 'route53', 'tagging', 'support', 'cloudtrail',
                'elasticache', 'kms', 'redshift',
            }
            if '?Action=' in endpoint or '&Action=' in endpoint:
                # Only use Action= for services that natively use query-action API style
                _op_host = urllib.parse.urlparse(endpoint).netloc
                _op_svc = self._aws_service_from_host(_op_host) if _op_host else None
                if _op_svc in QUERY_ACTION_SERVICES_OP:
                    parsed = urllib.parse.urlparse(endpoint)
                    params = urllib.parse.parse_qs(parsed.query)
                    if 'Action' in params:
                        action = params['Action'][0]
                        return action

            # For AWS S3, check for operations in query parameters
            # Query params can be in the URL or in request_info
            parsed_url = urllib.parse.urlparse(endpoint)
            path = parsed_url.path

            # Combine query params from URL and request_info
            params_dict = {}
            if parsed_url.query:
                params_dict.update(urllib.parse.parse_qs(parsed_url.query))
            if request_info.get('query_params'):
                # Add query params from request_info (these are single values, not lists)
                for k, v in request_info['query_params'].items():
                    params_dict[k] = [v] if v else ['']

            # Check if it's an S3 bucket operation (path contains bucket name or is simple)
            # Common S3 query parameters that indicate operations
            s3_ops = RESOURCE_MAPPINGS.get('AWS', {})
            for param_key in params_dict.keys():
                param_lower = param_key.lower()
                if param_lower in s3_ops:
                    return f'Get Bucket {s3_ops[param_lower]}'
                # Handle special S3 operations
                elif param_lower == 'intelligent-tiering':
                    return 'Get Bucket Intelligent Tiering Configuration'
                # If no mapping, use the parameter name itself (but skip common filters and AWS action params)
                elif param_lower not in ['maxkeys', 'prefix', 'delimiter', 'marker', 'api-version', 'view', 'action', 'version', 'filter']:
                    return f'Get Bucket {self._format_resource_name(param_key)}'

            # If path is just hostname or '/', and no useful query params
            if not path or path == '/' or path == '/{name}':
                # If no useful query params, it's a bucket list operation
                return 'List Buckets'

            # Fallback: Try to infer from URL path
            if path.endswith('/'):
                path = path[:-1]

            # Check if it's an S3 object operation (path has multiple segments with placeholders)
            path_segments = [s for s in path.split('/') if s]
            placeholder_count = sum(1 for s in path_segments if '{' in s)

            # If path has 2+ placeholders (e.g., /{bucket}/{key}), it's likely an object operation
            if placeholder_count >= 2:
                # Check if there's a query parameter that indicates the operation
                if params_dict:
                    for param_key in params_dict.keys():
                        param_lower = param_key.lower()
                        if param_lower == 'uploadid':
                            return 'List Multipart Upload Parts'
                        elif param_lower not in ['maxkeys', 'prefix', 'delimiter', 'marker', 'api-version', 'view']:
                            return f'Get Object {self._format_resource_name(param_key)}'
                # No query params, assume it's getting the object
                return 'Get Object'

            segments = [s for s in path.split('/') if s and '{' not in s.lower()]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                # Check if it's a known abbreviation
                if resource.lower() in RESOURCE_MAPPINGS.get('AWS', {}):
                    resource = RESOURCE_MAPPINGS['AWS'][resource.lower()]
                    return f'Get {resource}'
                return self._format_operation_from_method(method, resource)

        # Azure: Extract from URL path
        elif api_service == 'Azure':
            # Parse Azure REST API URLs
            # Format: /subscriptions/{id}/providers/Microsoft.Network/virtualNetworkGateways
            path = self._get_url_path(endpoint)

            # Check if it's Azure Storage (blob.core.windows.net, etc.)
            if 'blob.core.windows.net' in endpoint or 'file.core.windows.net' in endpoint or 'queue.core.windows.net' in endpoint or 'table.core.windows.net' in endpoint:
                # Azure Storage APIs use 'restype' and 'comp' parameters
                parsed = urllib.parse.urlparse(endpoint)
                params_dict = {}
                if parsed.query:
                    params_dict.update(urllib.parse.parse_qs(parsed.query))
                if request_info.get('query_params'):
                    for k, v in request_info['query_params'].items():
                        params_dict[k] = [v] if v else ['']

                if 'restype' in params_dict:
                    restype = params_dict['restype'][0] if params_dict['restype'] else ''
                    comp = params_dict.get('comp', [''])[0]
                    if comp:
                        return f'List {self._format_resource_name(restype)} {self._format_resource_name(comp)}'
                    return f'List {self._format_resource_name(restype)}'

                # Infer from path
                if path:
                    # Path like /{container} for blob storage
                    return f'{method.upper()} Storage'

            # Handle fully dynamic or empty paths
            if not path or path == '{dynamic}':
                # Check query parameters for operation hints (both in URL and request_info)
                parsed = urllib.parse.urlparse(endpoint)
                params_dict = {}
                if parsed.query:
                    params_dict.update(urllib.parse.parse_qs(parsed.query))
                if request_info.get('query_params'):
                    for k, v in request_info['query_params'].items():
                        params_dict[k] = [v] if v else ['']

                # Azure Storage APIs use 'restype' and 'comp' parameters
                if 'restype' in params_dict:
                    restype = params_dict['restype'][0] if params_dict['restype'] else ''
                    comp = params_dict.get('comp', [''])[0]
                    if comp:
                        return f'List {self._format_resource_name(restype)} {self._format_resource_name(comp)}'
                    return f'List {self._format_resource_name(restype)}'

                # No useful info, return generic based on method
                method_upper = method.upper()
                if method_upper == 'GET':
                    return 'List Resources'
                elif method_upper == 'POST':
                    return 'Create Resource'
                elif method_upper in ('PUT', 'PATCH'):
                    return 'Update Resource'
                elif method_upper == 'DELETE':
                    return 'Delete Resource'
                else:
                    return f'{method_upper} Resource'

            # Look for provider resources
            if '/providers/' in path:
                # Extract everything after the last provider
                after_provider = path.split('/providers/')[-1]
                segments = after_provider.split('/')

                # Find the resource type (skip Microsoft.*, get the actual resource)
                for i, seg in enumerate(segments):
                    if '.' in seg:  # Skip Microsoft.Network, etc.
                        continue
                    if seg and '{' not in seg.lower() and seg.lower() not in SKIP_PLACEHOLDERS:
                        # This is the resource type
                        return self._format_operation_from_method(method, seg)

            # Fallback: Use last non-variable segment
            segments = [s for s in path.split('/') if s and '{' not in s.lower()]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                return self._format_operation_from_method(method, resource)

        # GCP: Extract from URL path
        elif api_service == 'GCP':
            path = self._get_url_path(endpoint)

            # Handle fully dynamic or empty paths - use HTTP method as fallback
            if not path or path == '{dynamic}':
                return self._get_generic_operation_from_method(method)

            # GCP often uses :operation patterns (e.g., /projects:search)
            if path and ':' in path.split('/')[-1]:  # Check only the last segment
                last_segment = path.split('/')[-1]
                resource, operation = last_segment.split(':', 1)
                # Format: "Search Projects"
                operation_name = operation.title().replace('_', ' ')
                resource_name = resource.title().replace('_', ' ')
                return f'{operation_name} {resource_name}'

            segments = [s for s in path.split('/') if s and '{' not in s.lower() and s not in ('v1', 'v2', 'v3')]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                # Check if it's a known GCP abbreviation
                if resource.lower() in RESOURCE_MAPPINGS.get('GCP', {}):
                    resource = RESOURCE_MAPPINGS['GCP'][resource.lower()]
                    # Already in final form (e.g., 'Buckets'), just add method prefix
                    method_upper = method.upper()
                    if method_upper == 'GET':
                        return f'List {resource}'
                    elif method_upper == 'POST':
                        return f'Create {resource}'
                    elif method_upper in ('PUT', 'PATCH'):
                        return f'Update {resource}'
                    elif method_upper == 'DELETE':
                        return f'Delete {resource}'
                    else:
                        return f'{method_upper} {resource}'
                return self._format_operation_from_method(method, resource)

        # Flexera: Extract from URL path
        elif api_service == 'Flexera':
            path = self._get_url_path(endpoint)

            # Handle fully dynamic or empty paths - use HTTP method as fallback
            if not path or path == '{dynamic}':
                return self._get_generic_operation_from_method(method)

            # Special handling for bill-analysis API
            if '/bill-analysis/' in path and '/costs/' in path:
                # Handle /costs/aggregated and /costs/select patterns
                if '/costs/aggregated' in path:
                    return 'Request Aggregated Costs'
                elif '/costs/select' in path:
                    return 'Request Selected Costs'

            segments = [s for s in path.split('/') if s and '{' not in s.lower() and s not in ('v1', 'v2', 'v3')]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                # Clean up common patterns
                resource = resource.replace('-', ' ').replace('_', ' ')
                return self._format_operation_from_method(method, resource)


        # Oracle: Extract from URL path
        elif api_service == 'Oracle':
            path = self._get_url_path(endpoint)

            if not path:
                return self._get_generic_operation_from_method(method)

            segments = [s for s in path.split('/') if s and '{' not in s.lower()]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                # Check if it's a known Oracle abbreviation
                if resource.lower() in RESOURCE_MAPPINGS.get('Oracle', {}):
                    resource = RESOURCE_MAPPINGS['Oracle'][resource.lower()]
                return self._format_operation_from_method(method, resource)

        # GitHub: Extract from URL path
        elif api_service == 'GitHub':
            if 'raw.githubusercontent.com' in endpoint:
                return 'Get Raw Content'

            path = self._get_url_path(endpoint)

            if not path:
                return self._get_generic_operation_from_method(method)

            segments = [s for s in path.split('/') if s and '{' not in s.lower()]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                return self._format_operation_from_method(method, resource)

        # Default: Extract from URL path
        else:
            path = self._get_url_path(endpoint)

            if not path:
                return self._get_generic_operation_from_method(method)

            segments = [s for s in path.split('/') if s and '{' not in s.lower()]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                return self._format_operation_from_method(method, resource)

        # Ultimate fallback - use HTTP method to provide generic operation
        return self._get_generic_operation_from_method(method)

    # ------------------------------------------------------------------ #
    #  IAM permission resolution                                           #
    # ------------------------------------------------------------------ #

    def _determine_api_permission(self, endpoint, method, api_service, request_info, operation):
        """Return the IAM permission string for an API call, or None if undetermined."""
        if api_service == 'AWS':
            return self._aws_permission(endpoint, method, request_info, operation)
        elif api_service == 'Azure':
            return self._azure_permission(endpoint, method, request_info, operation)
        elif api_service == 'GCP':
            return self._gcp_permission(endpoint, method, request_info, operation)
        return None

    def _aws_service_from_host(self, host):
        """Map an AWS hostname to its IAM service prefix."""
        HOST_TO_SERVICE = {
            'monitoring': 'cloudwatch',
            'organizations': 'organizations',
            'sts': 'sts',
            'ec2': 'ec2',
            'iam': 'iam',
            'cloudtrail': 'cloudtrail',
            'kms': 'kms',
            'savingsplans': 'savingsplans',
            'eks': 'eks',
            'lambda': 'lambda',
            's3': 's3',
            's3-external-1': 's3',
            'config': 'config',
            'ce': 'ce',
            'compute-optimizer': 'compute-optimizer',
            'fsx': 'fsx',
            'elasticloadbalancing': 'elasticloadbalancing',
            'rds': 'rds',
            'elasticache': 'elasticache',
            'redshift': 'redshift',
            'access-analyzer': 'access-analyzer',
            'tagging': 'tag',
            'ecs': 'ecs',
        }
        # Map AWS API version strings (date) to service prefixes for bare amazonaws.com calls
        VERSION_TO_SERVICE = {
            '2016-11-15': 'ec2',
            '2014-10-31': 'rds',
            '2015-02-02': 'elasticache',
            '2012-12-01': 'redshift',
            '2010-05-08': 'iam',
            '2011-06-15': 'sts',
            '2015-12-01': 'elasticloadbalancing',
            '2012-06-01': 'elasticloadbalancing',
        }

        if not host:
            return None

        # S3 virtual-hosted / path-style detection
        if '.s3.' in host or host.startswith('s3.') or host.startswith('s3-'):
            return 's3'

        if 'execute-api' in host:
            return None

        # Bare amazonaws.com — return sentinel; caller will infer from Version= param
        if host in ('amazonaws.com',):
            return '__bare__'

        # Extract first subdomain part, strip placeholders
        first = host.split('.')[0].strip('{}')
        return HOST_TO_SERVICE.get(first)

    def _aws_infer_service_from_version(self, endpoint):
        """Infer AWS service from Version= query parameter (used for bare amazonaws.com calls)."""
        VERSION_TO_SERVICE = {
            '2016-11-15': 'ec2',
            '2014-10-31': 'rds',
            '2015-02-02': 'elasticache',
            '2012-12-01': 'redshift',
            '2010-05-08': 'iam',
            '2011-06-15': 'sts',
        }
        params = urllib.parse.parse_qs(urllib.parse.urlparse(endpoint).query)
        version = params.get('Version', [None])[0]
        return VERSION_TO_SERVICE.get(version)

    def _aws_rest_permission(self, service, path, method, endpoint):
        """Return a permission for REST-style AWS APIs that have no Action param."""
        # Access Analyzer (REST-based, not query-action)
        if service == 'access-analyzer':
            if re.search(r'/analyzer/?$', path) or re.search(r'/analyzer\?', endpoint):
                return 'access-analyzer:ListAnalyzers'
            if re.search(r'/analyzer/[^/]+$', path):
                return 'access-analyzer:GetAnalyzer'

        if service == 'lambda':
            if re.search(r'/functions/?$', path):
                return 'lambda:ListFunctions'
            if re.search(r'/tags/', path):
                return 'lambda:ListTags'
            if re.search(r'/functions/[^/]+/versions', path):
                return 'lambda:ListVersionsByFunction'
            if re.search(r'/provisioned-concurrency', path):
                return 'lambda:GetProvisionedConcurrencyConfig'

        # EKS
        if service == 'eks':
            if re.search(r'/clusters/[^/]+/node-groups/[^/]+', path):
                return 'eks:DescribeNodegroup'
            if re.search(r'/clusters/[^/]+/node-groups', path):
                return 'eks:ListNodegroups'
            if re.search(r'/clusters/[^/]+', path):
                return 'eks:DescribeCluster'
            if re.search(r'/clusters/?$', path):
                return 'eks:ListClusters'

        # S3
        if service == 's3':
            qs = urllib.parse.urlparse(endpoint).query
            qs_keys = set(urllib.parse.parse_qs(qs).keys()) | set(k.rstrip('=') for k in qs.split('&') if k)
            if 'location' in qs_keys or qs.startswith('location'):
                return 's3:GetBucketLocation'
            if 'logging' in qs_keys:
                return 's3:PutBucketLogging' if method == 'PUT' else 's3:GetBucketLogging'
            if 'acl' in qs_keys:
                return 's3:PutBucketAcl' if method == 'PUT' else 's3:GetBucketAcl'
            if 'policy' in qs_keys:
                return 's3:DeleteBucketPolicy' if method == 'DELETE' else 's3:GetBucketPolicy'
            if 'encryption' in qs_keys:
                return 's3:PutEncryptionConfiguration' if method == 'PUT' else 's3:GetEncryptionConfiguration'
            if 'tagging' in qs_keys:
                return 's3:GetBucketTagging'
            if 'versioning' in qs_keys:
                return 's3:GetBucketVersioning'
            if 'publicAccessBlock' in qs_keys:
                return 's3:GetBucketPublicAccessBlock'
            if 'intelligent-tiering' in qs_keys:
                return 's3:GetIntelligentTieringConfiguration'
            if 'lifecycle' in qs_keys:
                return 's3:GetLifecycleConfiguration'
            if 'uploadId' in qs_keys:
                return 's3:ListMultipartUploadParts' if method == 'GET' else 's3:AbortMultipartUpload'
            if 'uploads' in qs_keys:
                return 's3:ListBucketMultipartUploads'
            # Root list
            if path in ('/', '') or not path.strip('/'):
                return 's3:ListAllMyBuckets'
            # Object operations
            if method in ('GET', 'HEAD'):
                return 's3:GetObject'
            if method == 'PUT':
                return 's3:PutObject'
            if method == 'DELETE':
                # Bucket-level DELETE has only one path segment (the bucket name / placeholder).
                # Object-level DELETE has two or more segments (bucket + key).
                all_segs = [p for p in path.strip('/').split('/') if p]
                if len(all_segs) <= 1:
                    return 's3:DeleteBucket'
                return 's3:DeleteObject'

        # CloudWatch
        if service == 'cloudwatch':
            return 'cloudwatch:GetMetricData' if method == 'POST' else 'cloudwatch:ListMetrics'

        return None

    def _aws_permission(self, endpoint, method, request_info, operation):
        """Determine the IAM permission for an AWS API call."""
        host = request_info.get('host', '') if request_info else ''
        service = self._aws_service_from_host(host)
        # For bare amazonaws.com, try to infer service from Version= param
        if service == '__bare__':
            service = self._aws_infer_service_from_version(endpoint)
        # When host is dynamic, try to identify service from X-Amz-Target header.
        # e.g. AWSPriceListService.GetProducts -> pricing:GetProducts
        if not service and request_info and request_info.get('headers'):
            TARGET_HEADER_SERVICE_MAP = {
                'AWSPriceListService': 'pricing',
            }
            for _k, _v in request_info['headers'].items():
                if _k.lower() == 'x-amz-target' and '.' in _v:
                    _mapped = TARGET_HEADER_SERVICE_MAP.get(_v.split('.')[0])
                    if _mapped:
                        return f"{_mapped}:{_v.split('.')[-1]}"

        # When service cannot be determined from host or headers, fall back to detecting
        # S3 from the presence of S3-specific query-string keys in the endpoint URL.
        if not service:
            _S3_QS_KEYS = {
                'acl', 'logging', 'encryption', 'uploadId', 'uploads',
                'tagging', 'versioning', 'publicAccessBlock', 'intelligent-tiering',
                'lifecycle', 'policy', 'location',
            }
            _qs = urllib.parse.urlparse(endpoint).query
            _qs_keys = (set(urllib.parse.parse_qs(_qs).keys()) |
                        set(k.rstrip('=') for k in _qs.split('&') if k))
            if _qs_keys & _S3_QS_KEYS:
                service = 's3'

        if not service:
            return None

        parsed = urllib.parse.urlparse(endpoint)

        # 1. Query-string Action param — only for services that use the query-action API style
        QUERY_ACTION_SERVICES = {
            'ec2', 'sts', 'iam', 'autoscaling', 'elasticloadbalancing', 'elb',
            'monitoring', 'cloudwatch', 'sqs', 'rds', 'sns', 'cloudformation',
            'organizations', 'ecs', 'route53', 'tagging', 'support', 'cloudtrail',
            'elasticache', 'kms', 'redshift',
        }
        params = urllib.parse.parse_qs(parsed.query)
        if 'Action' in params and service in QUERY_ACTION_SERVICES:
            return f"{service}:{params['Action'][0]}"

        # 2. X-Amz-Target header (JSON services like Organizations, CE)
        if request_info and request_info.get('headers'):
            for key, value in request_info['headers'].items():
                if key.lower() == 'x-amz-target' and '.' in value:
                    return f"{service}:{value.split('.')[-1]}"

        # 3. Path-based PascalCase action  (e.g., /DescribeSavingsPlans)
        path_parts = [p for p in parsed.path.split('/') if p and not p.startswith('{')]
        last = path_parts[-1] if path_parts else ''
        if re.match(r'^[A-Z][a-zA-Z]+$', last):
            return f"{service}:{last}"

        # 4. REST API lookup (before operation fallback to avoid false matches)
        rest = self._aws_rest_permission(service, parsed.path, method, endpoint)
        if rest:
            return rest

        # 5. Operation name fallback
        clean_op = operation.replace(' ', '') if operation else ''
        if re.match(r'^[A-Z][a-zA-Z]+$', clean_op):
            return f"{service}:{clean_op}"

        return None

    def _azure_permission(self, endpoint, method, request_info, operation):
        """Determine the ARM permission for an Azure API call."""

        def _verb(m):
            m = m.upper()
            if m == 'GET':
                return 'read'
            if m in ('PUT', 'PATCH'):
                return 'write'
            if m == 'DELETE':
                return 'delete'
            return 'action'

        # Blob / Queue / Table data-plane
        if '.blob.core.windows.net' in endpoint:
            parsed_q = urllib.parse.urlparse(endpoint).query
            qs = urllib.parse.parse_qs(parsed_q)
            comp = qs.get('comp', [''])[0].lower()
            if comp == 'list':
                restype = qs.get('restype', [''])[0].lower()
                if restype == 'container':
                    # List blobs within a container; ARM permission applies
                    return 'Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read'
                # Root-level container listing
                return 'Microsoft.Storage/storageAccounts/blobServices/containers/list'
            if method.upper() == 'DELETE':
                return 'Microsoft.Storage/storageAccounts/blobServices/containers/blobs/delete'
            if method.upper() in ('PUT', 'PATCH'):
                return 'Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write'
            # Other blob data-plane calls (e.g. ?restype=service&comp=properties) — RBAC, not ARM
            return None

        if '.queue.core.windows.net' in endpoint:
            # Queue data-plane — requires Storage Queue Data Reader RBAC role, not an ARM permission
            return None

        if '.table.core.windows.net' in endpoint:
            # Table data-plane — requires Storage Table Data Reader RBAC role, not an ARM permission
            return None

        # Pricing API — no ARM permission
        if 'prices.azure.com' in endpoint:
            return None

        parsed = urllib.parse.urlparse(endpoint)
        path = parsed.path

        # Azure Monitor batch metrics
        if 'metrics:getBatch' in endpoint or path.endswith('metrics:getBatch'):
            return 'microsoft.insights/metrics/read'

        # Blob tier change: PUT /{id}?comp=tier
        parsed_qs = urllib.parse.parse_qs(parsed.query)
        if parsed_qs.get('comp', [''])[0].lower() == 'tier':
            return 'Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write'

        # Storage management policy (path has no {id} prefix — script lost container context)
        if re.search(r'/managementPolicies/default', path, re.IGNORECASE):
            return 'Microsoft.Storage/storageAccounts/managementPolicies/' + _verb(method)

        # Special top-level ARM paths without /providers/
        path_lower = path.lower()

        if re.match(r'^/subscriptions/?$', path_lower) or re.match(r'^/subscriptions/\{[^}]+\}/?$', path_lower):
            return 'Microsoft.Resources/subscriptions/read'

        if re.search(r'/subscriptions/[^/]+/resourcegroups/?$', path_lower):
            return 'Microsoft.Resources/subscriptions/resourceGroups/read'

        if 'savingsplanorder' in path_lower:
            if 'savingsplan' in path_lower and re.search(r'savingsplanorder[^/]*/savingsplan', path_lower):
                return 'Microsoft.BillingBenefits/savingsPlanOrders/savingsPlans/read'
            return 'Microsoft.BillingBenefits/savingsPlanOrders/read'

        if 'savingsPlan' in path or 'savingsplan' in path_lower:
            return 'Microsoft.BillingBenefits/savingsPlanOrders/savingsPlans/read'

        if 'microsoft.insights/metrics' in path_lower or '/metrics' in path_lower and 'monitor' in endpoint.lower():
            return 'microsoft.insights/metrics/read'

        # Activity Log events: 'management' is a fixed path segment, not an instance name
        if re.search(r'/providers/microsoft\.insights/eventtypes/management/values', path, re.IGNORECASE):
            return 'Microsoft.Insights/eventtypes/management/values/read'

        # ARM management.azure.com calls
        m = re.search(r'/providers/([^/?]+)/([^/?/]+)', path, re.IGNORECASE)
        if m:
            namespace = m.group(1)
            resource_type = m.group(2)
            after_provider = path[m.end():]

            sub_match = re.match(r'/[^/]+/([^/?]+)', after_provider)
            if sub_match:
                sub = sub_match.group(1)
                if not sub.startswith('{') and not re.match(r'^[0-9a-f-]{32,}$', sub, re.I):
                    after_sub = after_provider[sub_match.end():]
                    sub2_match = re.match(r'/([^/]+)/([^/?]+)', after_sub)
                    if sub2_match:
                        sub2_name = sub2_match.group(1)
                        sub2_type = sub2_match.group(2)
                        if not sub2_type.startswith('{'):
                            return f"{namespace}/{resource_type}/{sub}/{sub2_type}/{_verb(method)}"
                    return f"{namespace}/{resource_type}/{sub}/{_verb(method)}"

            return f"{namespace}/{resource_type}/{_verb(method)}"

        # Sub-resource paths where {id} is the full ARM resource URI.
        # Map the trailing sub-resource pattern to the most common permission.
        SUB_RESOURCE_MAP = {
            'agentPools':                        'Microsoft.ContainerService/managedClusters/agentPools/read',
            'blobServices/default':              'Microsoft.Storage/storageAccounts/blobServices/read',
            'elasticPools':                      'Microsoft.Sql/servers/elasticPools/read',
            'databases':                         'Microsoft.Sql/servers/databases/read',
            'instanceView':                      'Microsoft.Compute/virtualMachines/instanceView/read',
            'configurations/tls_version':        'Microsoft.DBforMySQL/flexibleServers/configurations/read',
            'configurations/log_retention_days': 'Microsoft.DBForPostgreSql/servers/configurations/read',
            'configurations/connection_throttling': 'Microsoft.DBForPostgreSql/servers/configurations/read',
            'transparentDataEncryption/current': 'Microsoft.Sql/servers/databases/transparentDataEncryption/read',
            'vulnerabilityAssessments/default':  'Microsoft.Sql/servers/vulnerabilityAssessments/read',
            'auditingSettings/default':          'Microsoft.Sql/servers/auditingSettings/read',
            'administrators':                    'Microsoft.Sql/servers/administrators/read',
            'securityAlertPolicies/Default':     'Microsoft.Sql/servers/securityAlertPolicies/read',
            'managementPolicies/default':        'Microsoft.Storage/storageAccounts/managementPolicies/read',
            'sites':                             'Microsoft.Web/serverfarms/sites/read',
            'connections':                       'Microsoft.Network/virtualNetworkGateways/connections/read',
            'config/web':                        'Microsoft.Web/sites/config/read',
        }
        # Normalize the path to extract the sub-resource suffix after any /{id} segment
        sub_path_match = re.match(r'^/\{[^}]+\}/(.+?)(?:\?.*)?$', path)
        if sub_path_match:
            sub_suffix = sub_path_match.group(1).rstrip('/')
            # Try exact match first, then prefix match
            if sub_suffix in SUB_RESOURCE_MAP:
                perm = SUB_RESOURCE_MAP[sub_suffix]
                # Adjust verb for non-GET calls
                if method.upper() != 'GET':
                    perm = perm.rsplit('/', 1)[0] + '/' + _verb(method)
                return perm
            # Try matching by first segment (e.g. 'configurations/tls_version' → 'configurations')
            # Only when sub_suffix is fully literal (no variable placeholders like {setting})
            first_seg = sub_suffix.split('/')[0]
            if '{' not in sub_suffix and first_seg + '/' in '\n'.join(SUB_RESOURCE_MAP.keys()) + '\n':
                for k, v in SUB_RESOURCE_MAP.items():
                    if k.startswith(first_seg + '/'):
                        perm = v
                        if method.upper() != 'GET':
                            perm = perm.rsplit('/', 1)[0] + '/' + _verb(method)
                        return perm

        # blob container listing — path is /{container} on blob endpoint (handled above)
        # data lake blob listing: path is / or /{container} on blob host
        if '.blob.core.windows.net' in endpoint or '.blob.' in endpoint:
            return 'Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read'

        if re.search(r'/subscriptions/[^/]+/resources/?$', path_lower):
            return 'Microsoft.Resources/subscriptions/resources/read'

        if re.search(r'/tenants/?$', path_lower):
            return 'Microsoft.Resources/tenants/read'

        if re.search(r'/subscriptions/[^/]+/metrics:getBatch', path_lower):
            return 'microsoft.insights/metrics/read'

        return None

    def _gcp_permission(self, endpoint, method, request_info, operation):
        """Determine the IAM permission for a GCP API call."""
        GCP_HOST_SERVICE = {
            'compute.googleapis.com': 'compute',
            'www.googleapis.com': 'compute',
            'storage.googleapis.com': 'storage',
            'bigquery.googleapis.com': 'bigquery',
            'sqladmin.googleapis.com': 'cloudsql',
            'cloudresourcemanager.googleapis.com': 'resourcemanager',
            'recommender.googleapis.com': 'recommender',
            'logging.googleapis.com': 'logging',
            'monitoring.googleapis.com': 'monitoring',
        }

        host = request_info.get('host', '') if request_info else ''
        # Normalise – strip port
        host_clean = host.split(':')[0].lower()
        service = GCP_HOST_SERVICE.get(host_clean)
        if not service:
            return None

        parsed = urllib.parse.urlparse(endpoint)
        path = parsed.path

        # Recommender — map literal recommender IDs to specific IAM permissions
        if service == 'recommender':
            RECOMMENDER_ID_MAP = {
                'google.compute.commitment.UsageCommitmentRecommender':         'recommender.usageCommitmentRecommendations.list',
                'google.compute.instance.MachineTypeRecommender':               'recommender.computeInstanceMachineTypeRecommendations.list',
                'google.compute.instance.IdleResourceRecommender':              'recommender.computeInstanceIdleResourceRecommendations.list',
                'google.compute.disk.IdleResourceRecommender':                  'recommender.computeDiskIdleResourceRecommendations.list',
                'google.compute.address.IdleResourceRecommender':               'recommender.computeAddressIdleResourceRecommendations.list',
                'google.compute.image.IdleResourceRecommender':                 'recommender.computeImageIdleResourceRecommendations.list',
                'google.compute.instanceGroupManager.MachineTypeRecommender':   'recommender.computeInstanceGroupManagerMachineTypeRecommendations.list',
                'google.cloudsql.instance.IdleRecommender':                     'recommender.cloudsqlIdleInstanceRecommendations.list',
                'google.cloudsql.instance.OverprovisionedRecommender':          'recommender.cloudsqlOverprovisionedInstanceRecommendations.list',
                'google.cloudsql.instance.OutOfDiskRecommender':                'recommender.cloudsqlInstanceOutOfDiskRecommendations.list',
                'google.iam.policy.Recommender':                                'recommender.iamPolicyRecommendations.list',
                'google.container.DiagnosisRecommender':                        'recommender.containerDiagnosisRecommendations.list',
                'google.logging.ProductSuggestionRecommender':                  'recommender.loggingProductSuggestionContainerRecommendations.list',
                'google.monitoring.ProductSuggestionRecommender':               'recommender.monitoringProductSuggestionComputeRecommendations.list',
                'google.resourcemanager.ProjectUtilizationRecommender':         'recommender.resourcemanagerProjectUtilizationRecommendations.list',
                'google.run.service.SecurityRecommender':                       'recommender.runServiceSecurityRecommendations.list',
                'google.cloudsql.security.GeneralRecommender':                  'recommender.cloudSecurityGeneralRecommendations.list',
            }
            rec_match = re.search(r'/recommenders/([^/{}]+)/recommendations', path)
            if rec_match:
                rec_id = rec_match.group(1)
                if rec_id in RECOMMENDER_ID_MAP:
                    return RECOMMENDER_ID_MAP[rec_id]
            # Dynamic recommender type — cannot determine specific permission
            return None

        # Cloud SQL
        if service == 'cloudsql':
            if re.search(r'/instances/?', path):
                return 'cloudsql.instances.list'
            return None

        # Resource Manager
        if service == 'resourcemanager':
            if re.search(r'/projects:search', path):
                return 'resourcemanager.projects.search'
            if re.search(r'/projects/[^/]+$', path):
                return 'resourcemanager.projects.get'
            if re.search(r'/projects/?$', path) or re.search(r'/projects$', path):
                return 'resourcemanager.projects.list'
            return None

        # Logging
        if service == 'logging':
            if 'entries' in path:
                return 'logging.logEntries.list'
            return None

        # Monitoring
        if service == 'monitoring':
            if 'timeSeries' in path or 'timeseries' in path.lower():
                return 'monitoring.timeSeries.list'
            return None

        # Storage
        if service == 'storage':
            if re.search(r'/b/[^/]+/iam', path):
                return 'storage.buckets.getIamPolicy'
            if re.search(r'/b/[^/]+/o', path):
                return 'storage.objects.list'
            if re.search(r'/b/?$', path) or re.search(r'/b\?', endpoint):
                return 'storage.buckets.list'
            return 'storage.buckets.list'

        # BigQuery
        if service == 'bigquery':
            if re.search(r'/datasets/[^/]+/tables', path):
                return 'bigquery.tables.list'
            if re.search(r'/datasets', path):
                return 'bigquery.datasets.list'
            return None

        # Compute
        if service == 'compute':
            # Aggregated list: /compute/v1/projects/{id}/aggregated/{resource}
            m_agg = re.search(r'/aggregated/([^/?]+)', path)
            if m_agg:
                resource = m_agg.group(1).rstrip('/')
                return f'compute.{resource}.aggregatedList'

            # /compute/v1/projects/{id}/regions
            if re.search(r'/projects/[^/]+/regions/?$', path):
                return 'compute.regions.list'

            # /compute/v1/projects/{id}/zones  (list or single zone listing)
            if re.search(r'/projects/[^/]+/zones/?$', path):
                return 'compute.zones.list'

            # /compute/v1/projects/{id}/zones/{zone}/{resource}
            m_zone = re.search(r'/zones/[^/]+/([^/?]+)/?$', path)
            if m_zone:
                resource = m_zone.group(1)
                if not resource.startswith('{'):
                    return f'compute.{resource}.list'

            # /compute/v1/projects/{id}/regions/{region}/{resource}
            m_region = re.search(r'/regions/[^/]+/([^/?]+)/?$', path)
            if m_region:
                resource = m_region.group(1)
                if not resource.startswith('{'):
                    return f'compute.{resource}.list'

            # /compute/v1/projects/{id}/global/{resource}
            m_global = re.search(r'/global/([^/?]+)/?$', path)
            if m_global:
                resource = m_global.group(1)
                # Include variable resources as placeholders (e.g. compute.{type}.list)
                return f'compute.{resource}.list'

            return None

        return None

    def _format_operation_from_method(self, method, resource):
        """Format an operation name from HTTP method and resource type.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, PATCH)
            resource: Resource name from URL

        Returns:
            Formatted operation name
        """
        # Clean up resource name - handle camelCase, snake_case, and kebab-case
        # Convert camelCase to spaces: virtualNetworkGateways -> virtual Network Gateways
        import re
        # Insert space before capital letters (except at start)
        resource = re.sub(r'([a-z])([A-Z])', r'\1 \2', resource)

        # Replace separators with spaces
        resource = resource.replace('-', ' ').replace('_', ' ')

        # Capitalize each word
        resource_words = resource.split()
        resource = ' '.join(word.capitalize() for word in resource_words)

        # Map method to operation prefix
        method = method.upper()
        if method == 'GET':
            # If plural, use List, otherwise use Get
            if resource.endswith('s') and len(resource) > 1:
                return f'List {resource}'
            else:
                return f'Get {resource}'
        elif method == 'POST':
            return f'Create {resource}'
        elif method == 'PUT':
            return f'Update {resource}'
        elif method == 'PATCH':
            return f'Update {resource}'
        elif method == 'DELETE':
            return f'Delete {resource}'
        else:
            return f'{method} {resource}'

    def _cwf_path_is_specific(self, host, path):
        """Return True only if the path identifies a specific cloud resource type.

        Used to avoid stopping a datasource trace at overly generic paths
        like /subscriptions or /v1/projects that don't reveal a resource type.
        """
        if not path:
            return False
        if 'googleapis.com' in host:
            return any(s in path for s in ['/compute/', '/sql/', '/v1/', '/storage/', '/bigtable/'])
        if 'azure.com' in host or 'management.azure' in host:
            return '/providers/' in path
        # For other hosts (AWS, etc.) any non-trivial path is specific
        return path not in ('/', '/subscriptions', '/subscriptions/')

    def _trace_datasource_api(self, ds_name, depth=0, visited=None):
        """Recursively trace a datasource chain to find its underlying API host and path.

        Returns (host, path) or (None, None).
        """
        if visited is None:
            visited = set()
        if depth > 10 or ds_name in visited:
            return None, None
        visited.add(ds_name)

        pat = re.compile(
            r'datasource\s+"' + re.escape(ds_name) + r'"\s+do(.*?)^end',
            re.MULTILINE | re.DOTALL
        )
        m = pat.search(self.content)
        if not m:
            return None, None
        ds_body = m.group(1)

        # Check for a request block with explicit host (literal string or parameter variable)
        host_m = re.search(r'\bhost\s+"([^"]+)"', ds_body)
        if host_m:
            host = host_m.group(1)
        else:
            # Try host with a $param_ variable: host $param_azure_endpoint
            param_host_m = re.search(r'\bhost\s+\$+param_(\w+)', ds_body)
            if param_host_m:
                param_name = 'param_' + param_host_m.group(1)
                host = self._resolve_parameter_from_content(param_name)
            else:
                host = None

        if host:
            # path join([...])
            pj = re.search(r'path\s+join\(\s*\[([^\]]+)\]\s*\)', ds_body)
            if pj:
                lits = re.findall(r'"([^"]+)"', pj.group(1))
                path = ''.join(lits)
                if self._cwf_path_is_specific(host, path):
                    return host, path
                # Pattern: join([val(iter_item, "id"), "/suffix"]) — literal suffix appended to
                # the iterate datasource's path. Detect a leading val(iter_item,...) + literal suffix.
                val_suffix = re.search(
                    r'val\s*\(\s*iter_item.*?\)\s*,\s*"(/[^"]*)"', pj.group(1)
                )
                if val_suffix:
                    suffix = val_suffix.group(1)
                    iter_ds = re.search(r'\biterate\s+\$(ds_\w+)', ds_body)
                    if iter_ds:
                        parent_h, parent_p = self._trace_datasource_api(
                            iter_ds.group(1), depth + 1, visited.copy()
                        )
                        if parent_h and parent_p and '/providers/' in (parent_p or ''):
                            combined = parent_p.rstrip('/') + '/{id}' + suffix
                            return parent_h, combined
            # literal path "..."
            pl = re.search(r'\bpath\s+"([^"]+)"', ds_body)
            if pl:
                path = pl.group(1)
                if self._cwf_path_is_specific(host, path):
                    return host, path
            # Host found but no specific path — fall through to trace dependencies

        # Trace all $ds_ references (run_script inputs and iterate)
        all_ds_refs = re.findall(r'\$(ds_\w+)', ds_body)
        seen_deps = visited.copy()
        for dep in all_ds_refs:
            h, p = self._trace_datasource_api(dep, depth + 1, seen_deps.copy())
            if h and self._cwf_path_is_specific(h, p or ''):
                return h, p

        # Return host with no path if we know the cloud provider but found no specific path
        if host:
            return host, None

        return None, None

    def _build_cwf_define_context(self):
        """Build a mapping of define_name -> (api_host, arm_or_gcp_path).

        Traces: escalation 'NAME' do run "DEFINE" -> validate_each $ds_X do escalate $NAME
        -> datasource $ds_X -> (host, path)
        """
        content = self.content

        # Step 1: escalation_name -> [define_names it calls via run "..."]
        esc_to_defines = {}
        for m in re.finditer(r'escalation\s+"(\w+)"\s+do(.*?)^end', content, re.MULTILINE | re.DOTALL):
            esc_name = m.group(1)
            body = m.group(2)
            defines = re.findall(r'run\s+"(\w+)"', body)
            if defines:
                esc_to_defines[esc_name] = defines

        # Step 2: define_name -> datasource_name (from validate_each blocks in policy blocks)
        define_to_ds = {}
        for pol_m in re.finditer(r'^policy\s+"[^"]+"\s+do(.*?)^end', content, re.MULTILINE | re.DOTALL):
            pol_body = pol_m.group(1)
            for ve_m in re.finditer(
                r'validate(?:_each)?\s+(\S+)\s+do(.*?)(?=^\s+(?:validate|end)\b)',
                pol_body, re.MULTILINE | re.DOTALL
            ):
                ds_ref = ve_m.group(1).lstrip('$')
                ve_body = ve_m.group(2)
                esc_refs = re.findall(r'escalate\s+\$(\w+)', ve_body)
                for esc_ref in esc_refs:
                    if esc_ref in esc_to_defines:
                        for define_name in esc_to_defines[esc_ref]:
                            if define_name not in define_to_ds:
                                define_to_ds[define_name] = ds_ref

        # Step 3: trace each datasource to find its API host and path
        define_context = {}
        for define_name, ds_name in define_to_ds.items():
            host, path = self._trace_datasource_api(ds_name)
            if host:
                define_context[define_name] = (host, path)

        # Step 4: propagate context from top-level defines to nested helper defines
        # (e.g. downsize_instances calls downsize_instance — propagate context to the callee)
        changed = True
        while changed:
            changed = False
            for caller_name, ctx in list(define_context.items()):
                define_pat = re.compile(
                    r'^define\s+' + re.escape(caller_name) + r'\b[^\n]*\bdo\b(.*?)^end',
                    re.MULTILINE | re.DOTALL
                )
                dm = define_pat.search(content)
                if not dm:
                    continue
                body = dm.group(1)

                # Build resourceType → callee mapping for if/elsif dispatch blocks:
                # if ($instance["resourceType"] == "X")
                #   call callee_name(...)
                rt_dispatch = {}  # {callee_name: resource_type_string}
                pending_rt = None
                for line in body.splitlines():
                    m_rt = re.search(r'\b(?:if|elsif)\b.*\["resourceType"\]\s*==\s*"([^"]+)"', line)
                    if m_rt:
                        pending_rt = m_rt.group(1)
                    m_call = re.search(r'\bcall\s+(\w+)\b', line)
                    if m_call:
                        if pending_rt:
                            rt_dispatch[m_call.group(1)] = pending_rt
                            pending_rt = None
                    # Reset pending_rt at end/else/end keywords
                    if re.match(r'\s*(end|else)\s*$', line):
                        pending_rt = None

                for callee in re.findall(r'\bcall\s+(\w+)', body):
                    if callee in define_context:
                        continue
                    if callee in rt_dispatch:
                        # Use the resource type from the if/elsif guard.
                        # Compound types like "Microsoft.Sql/servers/elasticPools" need
                        # intermediate /{id} segments: /providers/Microsoft.Sql/servers/{id}/elasticPools/{id}
                        rt = rt_dispatch[callee]
                        ctx_host = ctx[0] if ctx else 'management.azure.com'
                        rt_parts = rt.split('/')
                        ns = rt_parts[0]
                        sub_parts = []
                        for part in rt_parts[1:]:
                            sub_parts.append(part)
                            sub_parts.append('{id}')
                        arm_path = (
                            '/subscriptions/{id}/resourceGroups/{id}/providers/'
                            + ns + '/' + '/'.join(sub_parts)
                        )
                        define_context[callee] = (ctx_host, arm_path)
                    else:
                        define_context[callee] = ctx
                    changed = True

        return define_context

    def _gcp_cwf_permission(self, resource_var, method, action_suffix, is_cloudsql=False):
        """Return the GCP IAM permission for a CWF http_* call.

        Args:
            resource_var: Variable name holding the resource (e.g. 'instance', 'disk', 'snapshot')
            method: HTTP method (GET, POST, PATCH, DELETE, PUT)
            action_suffix: Literal suffix appended to selfLink (e.g. '/stop', '/setMachineType', '')
            is_cloudsql: True if the resource is a Cloud SQL instance (sqladmin.googleapis.com)
        """
        action = action_suffix.lstrip('/')
        # Normalize variable name: try original then strip trailing 's' (instances→instance, disks→disk)
        # Try original first to avoid corrupting words like 'address' → 'addres'
        hint_orig = resource_var.lower()
        hint_stripped = hint_orig.rstrip('s')

        if is_cloudsql:
            if method == 'DELETE':
                return 'cloudsql.instances.delete'
            if action == 'setMachineType' or method in ('PATCH', 'PUT'):
                return 'cloudsql.instances.update'
            if method == 'GET':
                return 'cloudsql.instances.get'
            if method == 'POST':
                return 'cloudsql.instances.update'
            return None

        # Compute Engine lookup table
        COMPUTE = {
            ('instance', 'DELETE', ''):              'compute.instances.delete',
            ('instance', 'POST', 'setMachineType'):  'compute.instances.setMachineType',
            ('instance', 'POST', 'start'):           'compute.instances.start',
            ('instance', 'POST', 'stop'):            'compute.instances.stop',
            ('instance', 'GET', ''):                 'compute.instances.get',
            ('instance', 'POST', 'setLabels'):       'compute.instances.setLabels',
            ('disk', 'DELETE', ''):                  'compute.disks.delete',
            ('disk', 'POST', 'createSnapshot'):      'compute.disks.createSnapshot',
            ('snapshot', 'DELETE', ''):              'compute.snapshots.delete',
            ('address', 'DELETE', ''):               'compute.addresses.delete',
            ('operation', 'GET', ''):                'compute.zoneOperations.get',
        }
        # Try original name first, then singularized form
        for hint in [hint_orig, hint_stripped]:
            key = (hint, method, action)
            if key in COMPUTE:
                return COMPUTE[key]

        # Generic fallback: use the original var name (plural), strip trailing 's' for singular
        # Skip generic variable names that don't map to a specific GCP resource type.
        GENERIC_NAMES = {'resource', 'item', 'data', 'object', 'result', 'response'}
        if hint_orig in GENERIC_NAMES or hint_stripped in GENERIC_NAMES:
            return None
        hint = hint_orig
        resource_plural = hint if hint.endswith('s') else hint + 's'
        if method == 'DELETE':
            return f'compute.{resource_plural}.delete'
        if method in ('PATCH', 'PUT'):
            return f'compute.{resource_plural}.update'
        if method == 'POST' and action:
            return f'compute.{resource_plural}.{action}'
        if method == 'GET':
            return f'compute.{resource_plural}.get'
        return None

    def _resolve_azure_cwf_href(self, href_expr, define_body, define_name, cwf_context):
        """Attempt to resolve an Azure CWF href variable expression to a full ARM path.

        For href: $href where $href = $instance["id"] + "/powerOff", returns
        the ARM collection path from the datasource + "/{id}/powerOff".

        Returns a resolved path string, or None if not resolvable.
        """
        action_suffix = ''
        href_expr = href_expr.strip().rstrip(',').strip()
        inline_m = re.match(
            r'\$(\w+)\[["\'][\w]+["\']\]\s*\+\s*"(/[^"]*)"', href_expr
        )
        if not inline_m:
            inline_m = re.match(r"\$(\w+)\['[\w]+'\]\s*\+\s*'(/[^']*)'", href_expr)
        if inline_m:
            action_suffix = inline_m.group(2)
        else:
            # Simple dict access: $instance["id"] with no suffix
            inline_simple = re.match(r'\$(\w+)\[["\'][\w]+["\']\]$', href_expr.rstrip())
            if not inline_simple:
                inline_simple = re.match(r"\$(\w+)\['[\w]+'\]$", href_expr.rstrip())
            if inline_simple:
                action_suffix = ''
            else:
                # --- Case 2: href is a simple variable $href — look backward for assignment
                var_name = href_expr.lstrip('$').split('[')[0].split("'")[0]
                # Find ALL assignments of this variable; use the last meaningful one
                all_assignments = re.findall(
                    r'\$' + re.escape(var_name) + r'\s*=\s*(.+)',
                    define_body
                )
                if not all_assignments:
                    # href is a function parameter with no body assignment.
                    # Check variable name for resource type hints before falling back to context.
                    # e.g. $snapshotId → snapshots, $snapshotName → snapshots
                    VAR_NAME_TO_ARM = {
                        'snapshot': 'Microsoft.Compute/snapshots',
                    }
                    var_lower = var_name.lower()
                    for hint_str, arm_type in VAR_NAME_TO_ARM.items():
                        if var_lower.startswith(hint_str):
                            return (
                                '/subscriptions/{id}/resourceGroups/{id}/providers/'
                                + arm_type + '/{id}'
                            )
                    # Fall back to using the context's ARM path directly
                    context = cwf_context.get(define_name)
                    if context:
                        _, arm_path = context
                        if arm_path and '/providers/' in arm_path:
                            return arm_path.rstrip('/') + '/{id}'
                    return None

                # Check all RHS values; prefer join( patterns for synthesizing ARM paths
                join_rhs = next((r for r in all_assignments if 'join(' in r), None)
                rhs = (join_rhs or all_assignments[-1]).strip()

                # Parse assignment: $param["field"] + "/action" or just $param["field"]
                am = re.match(r'\$\w+\[["\'][\w]+["\']\]\s*\+\s*"(/[^"]*)"', rhs)
                if not am:
                    am = re.match(r"\$\w+\['[\w]+'\]\s*\+\s*'(/[^']*)'", rhs)
                if am:
                    action_suffix = am.group(1)
                elif re.match(r'\$\w+\[["\'][\w]+["\']\]', rhs):
                    # Check if the field name hints at a different resource type than context.
                    # e.g. $item['attached_vm'] → virtualMachines, $item['disk_id'] → disks
                    field_m = re.match(r"\$\w+\[['\"]([\w]+)['\"]\]", rhs)
                    if field_m:
                        field_name = field_m.group(1).lower()
                        FIELD_TYPE_MAP = {
                            'vm': 'virtualMachines',
                            'virtual_machine': 'virtualMachines',
                            'attached_vm': 'virtualMachines',
                        }
                        for hint_key, arm_type in FIELD_TYPE_MAP.items():
                            if hint_key in field_name:
                                sub_id = (
                                    '/subscriptions/{id}/resourceGroups/{id}/providers/'
                                    f'Microsoft.Compute/{arm_type}' + '/{id}'
                                )
                                return sub_id
                    action_suffix = ''
                else:
                    # Handle join([..., "Microsoft.X", "/type/", ...]) patterns
                    if 'join(' in rhs or 'join([' in rhs:
                        # Extract all string literals from the join call
                        literals = re.findall(r'"(Microsoft\.[^"]+)"', define_body)
                        type_hints = re.findall(r'"(/[^"]+/)"', define_body)
                        if literals and type_hints:
                            ns = literals[0]  # e.g. "Microsoft.Compute"
                            type_part = type_hints[0].strip('/')  # e.g. "snapshots"
                            synthetic_path = (
                                '/subscriptions/{id}/resourceGroups/{id}/providers/'
                                + ns + '/' + type_part + '/{id}'
                            )
                            return synthetic_path
                    return None

                # Store a hint from the RHS base variable for fallback context synthesis below
                # e.g. $instance["resourceID"] → hint = "instance"
                base_var_m = re.match(r'\$(\w+)\[', rhs)
                _base_var_hint = base_var_m.group(1).lower() if base_var_m else ''

        # Look up the ARM path from the escalation context
        context = cwf_context.get(define_name)
        host, arm_path = context if context else (None, None)
        if not arm_path or '/providers/' not in arm_path:
            # Context is missing or invalid (e.g. wrong datasource traced for this define).
            # Try to synthesise the ARM path from:
            # 1. Action suffix (e.g. /start, /deallocate → virtualMachines)
            # 2. Variable-name hint (e.g. $instance["resourceID"] → virtualMachines)
            ACTION_TO_ARM_TYPE = {
                '/start':      'Microsoft.Compute/virtualMachines',
                '/deallocate': 'Microsoft.Compute/virtualMachines',
                '/powerOff':   'Microsoft.Compute/virtualMachines',
                '/restart':    'Microsoft.Compute/virtualMachines',
                '/redeploy':   'Microsoft.Compute/virtualMachines',
            }
            VAR_HINT_TO_ARM_TYPE = {
                'instance':         'Microsoft.Compute/virtualMachines',
                'vm':               'Microsoft.Compute/virtualMachines',
                'virtual_machine':  'Microsoft.Compute/virtualMachines',
            }
            synthetic_type = (
                ACTION_TO_ARM_TYPE.get(action_suffix)
                or VAR_HINT_TO_ARM_TYPE.get(locals().get('_base_var_hint', ''))
            )
            if synthetic_type:
                return (
                    '/subscriptions/{id}/resourceGroups/{id}/providers/'
                    + synthetic_type + '/{id}' + action_suffix
                )
            return None

        # Strip any trailing slashes and build: arm_path + /{id} + action_suffix
        return arm_path.rstrip('/') + '/{id}' + action_suffix

    def _extract_define_blocks(self):
        """Extract all CWF define...do...end blocks from the policy template."""
        define_blocks = []
        lines = self.content.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            # Match define header that starts with 'define name' and ends with 'do'
            define_match = re.match(r'^define\s+(\w+)', line)
            if define_match and re.search(r'\bdo\s*$', line):
                define_name = define_match.group(1)
                define_lines = []
                depth = 1  # header line opens with 'do'
                i += 1
                while i < len(lines) and depth > 0:
                    current_line = lines[i]
                    stripped = current_line.strip()
                    if not stripped.startswith('#'):
                        # Each CWF block maps to exactly one 'end'.
                        # Count a line as ONE opener if it ends with 'do'
                        # (covers: foreach/while/sub/standalone do blocks).
                        # Count a line as ONE opener if it starts with 'if' or 'case'
                        # (these use end without a leading 'do').
                        # Never double-count (e.g. "foreach x do" is one opener, not two).
                        if re.match(r'^end\s*$', stripped):
                            depth -= 1
                            if depth == 0:
                                break
                        elif re.search(r'\bdo\s*$', stripped):
                            depth += 1
                        elif re.match(r'\b(if|case)\b', stripped):
                            depth += 1
                    define_lines.append(current_line)
                    i += 1
                define_blocks.append({
                    'name': define_name,
                    'body': '\n'.join(define_lines)
                })
            i += 1
        return define_blocks

    def _resolve_cwf_host(self, host_expr, define_body):
        """Resolve a CWF host expression to an actual hostname or placeholder.

        Tries the CWF_HOST_MAP first, then backwards variable lookup in the define block,
        then parameter resolution.  Also handles inline string-concatenation expressions
        like: "ec2." + $instance["region"] + ".amazonaws.com"
        """
        host_expr = host_expr.strip().rstrip(',')

        # Direct map lookup (handles $param_azure_endpoint, $$rs_optima_host, etc.)
        if host_expr in self.CWF_HOST_MAP:
            return self.CWF_HOST_MAP[host_expr]

        # Inline concatenation: expression contains "+" and quoted string parts
        # e.g.  "ec2." + $instance["region"] + ".amazonaws.com"
        # Strip dict-key accesses like ["region"] or ['region'] so they don't get picked up as strings.
        if '+' in host_expr:
            expr_stripped = re.sub(r'\[["\'][^"\']*["\']\]', '', host_expr)
            strings = re.findall(r'["\']([^"\']+)["\']', expr_stripped)
            if strings:
                full = ''.join(strings)
                if 'amazonaws.com' in full:
                    parts = []
                    for j, s in enumerate(strings):
                        parts.append(s)
                        if j < len(strings) - 1:
                            parts.append('{region}')
                    return ''.join(parts)
                else:
                    parts = []
                    for j, s in enumerate(strings):
                        parts.append(s)
                        if j < len(strings) - 1:
                            parts.append('{id}')
                    return ''.join(parts)

        # Backwards variable lookup: look for $varname = "..." + $var + "..." in define body
        var_name = re.sub(r'^\$+', '', host_expr)
        if var_name:
            assign_match = re.search(
                rf'\${re.escape(var_name)}\s*=\s*(.+)',
                define_body
            )
            if assign_match:
                rhs = assign_match.group(1).strip()
                # If the RHS is a string concatenation (contains '+'), recurse on it first.
                # This handles patterns like "ec2." + $instance["region"] + ".amazonaws.com"
                if '+' in rhs:
                    resolved = self._resolve_cwf_host(rhs, define_body)
                    if resolved:
                        return resolved
                # If RHS is a pure dict/array field access with no string literals,
                # skip — the extracted key is not a hostname; let auth-fallback handle it.
                elif re.search(r'\$\w+\[', rhs):
                    # When the variable holds a bucket's host field (e.g. $bucket["host"]),
                    # it resolves to an S3 virtual-hosted URL at runtime.
                    if re.search(r'\$(?:\w*bucket\w*)\["host"\]', rhs, re.IGNORECASE):
                        return '{bucket}.s3.amazonaws.com'
                    pass
                else:
                    strings = re.findall(r'"([^"]+)"', rhs)
                    if strings:
                        full = ''.join(strings)
                        if 'amazonaws.com' in full:
                            # Build host with {region} placeholder between string literals
                            parts = []
                            for j, s in enumerate(strings):
                                parts.append(s)
                                if j < len(strings) - 1:
                                    parts.append('{region}')
                            return ''.join(parts)
                        # If the resolved string is in CWF_HOST_MAP, return the mapped value
                        resolved_str = strings[0] if len(strings) == 1 else None
                        if resolved_str and resolved_str in self.CWF_HOST_MAP:
                            return self.CWF_HOST_MAP[resolved_str]
                        else:
                            parts = []
                            for j, s in enumerate(strings):
                                parts.append(s)
                                if j < len(strings) - 1:
                                    parts.append('{id}')
                            return ''.join(parts)

        # Try resolving $param_xxx from parameter definitions
        param_match = re.match(r'^\$+param_(\w+)', host_expr)
        if param_match:
            param_name = 'param_' + param_match.group(1)
            resolved = self._resolve_parameter_from_content(param_name)
            if resolved:
                return resolved

        return None

    def _extract_cwf_calls(self):
        """Extract HTTP API calls from CWF define...do...end blocks.

        Handles both http_request(...) and GCP-style http_get/post/patch/put/delete(...) calls.
        For Azure, resolves dynamic href variables using escalation context.
        For GCP, determines permission from selfLink variable name and action suffix.
        """
        api_calls = []
        define_blocks = self._extract_define_blocks()

        # Pre-build context: define_name -> (api_host, arm_or_gcp_path)
        cwf_context = self._build_cwf_define_context()

        for define_block in define_blocks:
            define_name = define_block['name']
            define_body = define_block['body']

            pos = 0
            while pos < len(define_body):
                # Match http_request OR GCP helper functions
                http_match = re.search(
                    r'\b(http_(?:request|get|post|patch|put|delete))\s*\(',
                    define_body[pos:]
                )
                if not http_match:
                    break

                func_name = http_match.group(1)
                # Determine method from function name for GCP helpers
                FUNC_METHOD = {
                    'http_get': 'GET', 'http_post': 'POST',
                    'http_patch': 'PATCH', 'http_put': 'PUT', 'http_delete': 'DELETE',
                }
                method_from_func = FUNC_METHOD.get(func_name)

                start = pos + http_match.end()
                depth = 1
                call_end = start
                while call_end < len(define_body) and depth > 0:
                    c = define_body[call_end]
                    if c == '(':
                        depth += 1
                    elif c == ')':
                        depth -= 1
                    call_end += 1

                call_body = define_body[start:call_end - 1]
                pos = call_end

                # Parse verb (explicit verb: field takes precedence, else infer from func name)
                verb_match = re.search(r'\bverb:\s*"([^"]+)"', call_body, re.IGNORECASE)
                method = verb_match.group(1).upper() if verb_match else (method_from_func or 'GET')

                # Parse auth for cloud provider inference
                auth_match = re.search(r'\bauth:\s*(\$\$\w+)', call_body)
                auth_name = auth_match.group(1) if auth_match else None

                # ----------------------------------------------------------------
                # Handle url: field (GCP http_delete/post/etc. or Azure full-URL style)
                # ----------------------------------------------------------------
                url_field_match = re.search(
                    r'\burl:\s*(.+?)(?=\s*,\s*\n|\s*\n)', call_body, re.MULTILINE
                )
                if url_field_match:
                    raw_url_expr = url_field_match.group(1).strip().rstrip(',')

                    # Resolve variable if needed
                    url_expr = raw_url_expr
                    if url_expr.startswith('$') and '[' not in url_expr and '+' not in url_expr:
                        var_name = url_expr.lstrip('$')
                        assign_m = re.search(
                            r'\$' + re.escape(var_name) + r'\s*=\s*(.+)',
                            define_body
                        )
                        if assign_m:
                            url_expr = assign_m.group(1).strip()

                    # Pattern: $var['selfLink'] or $var['selfLink'] + '/action'
                    sl_m = re.match(
                        r"\$(\w+)\[[\'\"]selfLink[\'\"]\](?:\s*\+\s*['\"]([^'\"]*)['\"])?",
                        url_expr
                    )
                    if sl_m:
                        resource_var = sl_m.group(1)
                        action_suffix = sl_m.group(2) or ''

                        # Determine if Cloud SQL by checking template datasources (not context,
                        # which may point to a wrong/unrelated datasource)
                        is_cloudsql = bool(re.search(r'sqladmin\.googleapis\.com', self.content))

                        permission = self._gcp_cwf_permission(
                            resource_var, method, action_suffix, is_cloudsql
                        )
                        if permission:
                            if is_cloudsql:
                                ep_host = 'sqladmin.googleapis.com'
                                ep_path = f'/sql/v1beta4/projects/{{id}}/instances/{{id}}{action_suffix}'
                            else:
                                ep_host = 'compute.googleapis.com'
                                ep_path = (
                                    f'/compute/v1/projects/{{id}}/zones/{{id}}'
                                    f'/{resource_var}s/{{id}}{action_suffix}'
                                )
                            endpoint = f'https://{ep_host}{ep_path}'
                            api_calls.append({
                                'policy_name': self.policy_name,
                                'datasource_name': 'define_' + define_name,
                                'method': method,
                                'endpoint': endpoint,
                                'operation': action_suffix.lstrip('/') or resource_var,
                                'field': '{entire response}',
                                'api_service': 'GCP',
                                'permission': permission,
                            })
                        continue

                    # Pattern: full static URL string containing management.azure.com
                    azure_url_m = re.search(r'management\.azure\.com', url_expr)
                    if azure_url_m:
                        ctx = cwf_context.get(define_name)
                        if ctx:
                            _, arm_path = ctx
                            if arm_path and '/providers/' in arm_path:
                                full_path = arm_path.rstrip('/') + '/{id}'
                                host = 'management.azure.com'
                                request_info = {
                                    'host': host, 'path': full_path,
                                    'method': method, 'query_params': {},
                                    'body_params': {}, 'headers': {},
                                }
                                endpoint = self._build_endpoint_url(request_info)
                                if endpoint:
                                    api_service = 'Azure'
                                    operation = self._extract_operation_name(endpoint, method, api_service, request_info)
                                    permission = self._determine_api_permission(endpoint, method, api_service, request_info, operation)
                                    api_calls.append({
                                        'policy_name': self.policy_name,
                                        'datasource_name': 'define_' + define_name,
                                        'method': method, 'endpoint': endpoint,
                                        'operation': operation, 'field': '{entire response}',
                                        'api_service': api_service, 'permission': permission,
                                    })
                        continue

                    # Unrecognised url: pattern — skip.
                    # However, if the URL variable contains $param_azure_endpoint or
                    # $azure_endpoint, treat it as management.azure.com and derive from context.
                    if re.search(r'\$(?:param_)?azure_endpoint\b', url_expr):
                        ctx = cwf_context.get(define_name)
                        if ctx:
                            _, arm_path = ctx
                            if arm_path and '/providers/' in arm_path:
                                full_path = arm_path.rstrip('/') + '/{id}'
                                host = 'management.azure.com'
                                request_info = {
                                    'host': host, 'path': full_path,
                                    'method': method, 'query_params': {},
                                    'body_params': {}, 'headers': {},
                                }
                                endpoint = self._build_endpoint_url(request_info)
                                if endpoint:
                                    api_service = 'Azure'
                                    operation = self._extract_operation_name(endpoint, method, api_service, request_info)
                                    permission = self._determine_api_permission(endpoint, method, api_service, request_info, operation)
                                    api_calls.append({
                                        'policy_name': self.policy_name,
                                        'datasource_name': 'define_' + define_name,
                                        'method': method, 'endpoint': endpoint,
                                        'operation': operation, 'field': '{entire response}',
                                        'api_service': api_service, 'permission': permission,
                                    })
                    continue

                # ----------------------------------------------------------------
                # Standard http_request path: parse host + href/path
                # ----------------------------------------------------------------
                host_match = re.search(r'\bhost:\s*(.+?)(?:\s*,\s*$|\s*\n)', call_body, re.MULTILINE)
                raw_host = host_match.group(1).strip().rstrip(',') if host_match else None

                host = None
                if raw_host:
                    host = self._resolve_cwf_host(raw_host, define_body)

                # Fallback: infer host from auth credential name
                if not host and auth_name:
                    auth_lower = auth_name.lower()
                    if 'azure' in auth_lower:
                        host = 'management.azure.com'
                    elif 'aws' in auth_lower:
                        host = 'amazonaws.com'
                    elif 'google' in auth_lower:
                        host = 'googleapis.com'
                    elif 'flexera' in auth_lower:
                        host = 'rs_optima_host'

                if not host:
                    continue
                if host == 'false' or host.startswith('false/'):
                    continue

                # Parse href or path
                path = None
                href_match = re.search(r'\b(?:href|path):\s*"([^"]+)"', call_body)
                if href_match:
                    path = href_match.group(1)
                else:
                    join_match = re.search(r'\b(?:href|path):\s*join\(\[([^\]]+)\]\)', call_body)
                    if join_match:
                        strings = re.findall(r'"([^"]+)"', join_match.group(1))
                        path = '/{id}'.join(strings) if strings else '/{id}'
                    else:
                        var_match = re.search(r'\b(?:href|path):\s*(\$\S+)', call_body)
                        if var_match:
                            var_expr = var_match.group(1).rstrip(',')
                            # Try to resolve simple string variable ($href = "/")
                            vname = re.escape(var_expr.lstrip('$'))
                            lit_m = re.search(r'\$' + vname + r'\s*=\s*"([^"]*)"', define_body)
                            if lit_m:
                                # If the assignment is actually a concatenation (e.g. "/" + $var),
                                # the literal match only captures the prefix — use /{id} instead.
                                concat_m = re.search(r'\$' + vname + r'\s*=\s*"[^"]*"\s*\+', define_body)
                                if concat_m:
                                    path = '/{id}'
                                else:
                                    path = lit_m.group(1) or '/'
                            elif 'azure' in (host or '').lower() or host == 'management.azure.com':
                                # For Azure, try to resolve the href expression to a full ARM path
                                resolved = self._resolve_azure_cwf_href(
                                    var_expr, define_body, define_name, cwf_context
                                )
                                if resolved:
                                    path = resolved
                            if not path:
                                path = '/{id}'

                if not path:
                    path = '/'

                # Parse query_strings: { "key": "value", ... }
                # Values may be empty strings or variable references (e.g. $var["field"]).
                query_params = {}
                qs_match = re.search(r'query_strings:\s*\{([^}]+)\}', call_body, re.DOTALL)
                if qs_match:
                    qs_str = qs_match.group(1)
                    # Quoted key with quoted value (value may be empty)
                    for kv in re.finditer(r'"([^"]+)"\s*:\s*"([^"]*)"', qs_str):
                        query_params[kv.group(1)] = kv.group(2)
                    # Quoted key with non-quoted (variable) value — just record the key
                    for km in re.finditer(r'"([^"]+)"\s*:\s*\$\w', qs_str):
                        if km.group(1) not in query_params:
                            query_params[km.group(1)] = '{dynamic}'

                # Parse headers: { "key": "value", ... }
                # Supports both `headers:` (plural) and `header:` (singular) CWF keyword
                headers = {}
                h_match = re.search(r'\bheaders?:\s*\{([^}]+)\}', call_body, re.DOTALL)
                if h_match:
                    for kv in re.finditer(r'"([^"]+)"\s*:\s*"([^"]+)"', h_match.group(1)):
                        headers[kv.group(1)] = kv.group(2)

                # Parse query_strings: { ... } or query_strings: $var_name
                # If the value is a variable, trace the first assignment in the define body
                if not query_params:
                    qs_var_match = re.search(r'query_strings:\s*(\$\w+)', call_body)
                    if qs_var_match:
                        qvar = re.escape(qs_var_match.group(1).lstrip('$'))
                        qs_assign = re.search(
                            r'\$' + qvar + r'\s*=\s*\{([^}]+)\}',
                            define_body
                        )
                        if qs_assign:
                            for kv in re.finditer(r'"([^"]+)"\s*:\s*"([^"]+)"', qs_assign.group(1)):
                                query_params[kv.group(1)] = kv.group(2)

                request_info = {
                    'host': host, 'path': path, 'method': method,
                    'query_params': query_params, 'body_params': {}, 'headers': headers,
                }

                endpoint = self._build_endpoint_url(request_info)
                if not endpoint:
                    continue

                api_service = self._determine_api_service(host, path)
                operation = self._extract_operation_name(endpoint, method, api_service, request_info)
                permission = self._determine_api_permission(endpoint, method, api_service, request_info, operation)

                api_calls.append({
                    'policy_name': self.policy_name,
                    'datasource_name': 'define_' + define_name,
                    'method': method, 'endpoint': endpoint,
                    'operation': operation, 'field': '{entire response}',
                    'api_service': api_service, 'permission': permission,
                })

        return api_calls

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
                    if script_request.get('headers'):
                        request_info['headers'].update(script_request['headers'])

            # Process all API calls (not just cloud providers)
            # When host is dynamic/unknown but an X-Amz-Target header is present (e.g. the AWS
            # Pricing API whose host comes from a runtime parameter), synthesize a bare
            # amazonaws.com host so the call is not silently skipped.
            if not request_info['host']:
                headers_lower = {k.lower(): v for k, v in request_info.get('headers', {}).items()}
                if 'x-amz-target' in headers_lower:
                    request_info = dict(request_info)
                    request_info['host'] = 'amazonaws.com'

            if request_info['host']:
                # Skip boolean-default parameters (false host means no URL configured)
                host_val = request_info['host']
                if host_val == 'false' or host_val.startswith('false/'):
                    continue

                # Determine which service this API call targets
                api_service = self._determine_api_service(request_info['host'], request_info.get('path'))

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

                # Extract operation name
                operation = self._extract_operation_name(endpoint, request_info['method'], api_service, request_info)
                permission = self._determine_api_permission(endpoint, request_info['method'], api_service, request_info, operation)

                if endpoint:
                    # If no fields found, add at least one entry for the API call
                    if not unique_fields:
                        api_calls.append({
                            'policy_name': self.policy_name,
                            'datasource_name': datasource['name'],
                            'method': request_info['method'],
                            'endpoint': endpoint,
                            'operation': operation,
                            'field': '{entire response}',
                            'api_service': api_service,
                            'permission': permission
                        })
                    else:
                        # Add one entry per field
                        for field in unique_fields:
                            api_calls.append({
                                'policy_name': self.policy_name,
                                'datasource_name': datasource['name'],
                                'method': request_info['method'],
                                'endpoint': endpoint,
                                'operation': operation,
                                'field': field,
                                'api_service': api_service,
                                'permission': permission
                            })

        # Also extract API calls from CWF define blocks (remediation/action calls)
        cwf_calls = self._extract_cwf_calls()
        api_calls.extend(cwf_calls)

        # Expand placeholder GCP permissions where resource type is a runtime variable.
        # Scans the template source for literal 'types = [...]' JS arrays and replaces
        # e.g. compute.{type}.aggregatedList with compute.addresses.aggregatedList, etc.
        api_calls = self._expand_dynamic_gcp_type_permissions(api_calls)

        # Add implicit companion GCP permissions that are always required alongside
        # a specific permission (e.g. compute.snapshots.create paired with createSnapshot).
        api_calls = self._add_gcp_implicit_paired_permissions(api_calls)

        # Add GCP Recommender API permissions extracted from recommender_map dicts and
        # inline type-suffix patterns in run_script calls.
        recommender_calls = self._extract_gcp_recommender_permissions()
        if recommender_calls:
            existing = {(c['policy_name'], c.get('permission')) for c in api_calls}
            for rc in recommender_calls:
                if (rc['policy_name'], rc['permission']) not in existing:
                    api_calls.append(rc)

        return api_calls

    def _extract_gcp_recommender_permissions(self):
        """Extract GCP Recommender API permissions from static patterns in the template.

        Handles two patterns:
        1. A JS `recommender_map = { "Label": "google.xxx.RecommenderType", ... }` dict —
           the full recommender type ID is a string literal value in the map.
        2. A path built as `"google.prefix." + type` where `type` suffix is passed as a
           string literal to run_script (e.g. "IdleResourceRecommender").

        Each extracted recommender type ID is looked up in a static table to produce the
        corresponding GCP IAM permission name.
        """
        RECOMMENDER_TYPE_TO_PERMISSION = {
            'google.accounts.security.SecurityKeyRecommender':
                'recommender.cloudSecurityGeneralRecommendations.list',
            'google.cloudsql.instance.IdleRecommender':
                'recommender.cloudsqlIdleInstanceRecommendations.list',
            'google.cloudsql.instance.OutOfDiskRecommender':
                'recommender.cloudsqlInstanceOutOfDiskRecommendations.list',
            'google.cloudsql.instance.OverprovisionedRecommender':
                'recommender.cloudsqlOverprovisionedInstanceRecommendations.list',
            'google.compute.address.IdleResourceRecommender':
                'recommender.computeAddressIdleResourceRecommendations.list',
            'google.compute.commitment.UsageCommitmentRecommender':
                'recommender.usageCommitmentRecommendations.list',
            'google.compute.disk.IdleResourceRecommender':
                'recommender.computeDiskIdleResourceRecommendations.list',
            'google.compute.image.IdleResourceRecommender':
                'recommender.computeImageIdleResourceRecommendations.list',
            'google.compute.instance.IdleResourceRecommender':
                'recommender.computeInstanceIdleResourceRecommendations.list',
            'google.compute.instance.MachineTypeRecommender':
                'recommender.computeInstanceMachineTypeRecommendations.list',
            'google.compute.instanceGroupManager.MachineTypeRecommender':
                'recommender.computeInstanceGroupManagerMachineTypeRecommendations.list',
            'google.container.DiagnosisRecommender':
                'recommender.containerDiagnosisRecommendations.list',
            'google.iam.policy.Recommender':
                'recommender.iamPolicyRecommendations.list',
            'google.logging.productSuggestion.ContainerRecommender':
                'recommender.loggingProductSuggestionContainerRecommendations.list',
            'google.monitoring.productSuggestion.ComputeRecommender':
                'recommender.monitoringProductSuggestionComputeRecommendations.list',
            'google.resourcemanager.projectUtilization.Recommender':
                'recommender.resourcemanagerProjectUtilizationRecommendations.list',
            'google.run.service.SecurityRecommender':
                'recommender.runServiceSecurityRecommendations.list',
        }

        found_type_ids = set()

        # Pattern 1: recommender_map = { "Label": "google.xxx.yyy.RecommenderType", ... }
        map_match = re.search(r'recommender_map\s*=\s*\{([^}]+)\}', self.content, re.DOTALL)
        if map_match:
            for kv in re.finditer(
                r'["\']([^"\']+)["\']\s*:\s*["\']([^"\']+)["\']', map_match.group(1)
            ):
                type_id = kv.group(2)
                if type_id.startswith('google.'):
                    found_type_ids.add(type_id)

        # Pattern 2: path built as "google.prefix." + type where type suffix is a string
        # literal passed to run_script (e.g. "IdleResourceRecommender"). Extract the
        # prefix from the path and all Recommender suffix literals from the template, then
        # combine. Invalid combinations are filtered out by the lookup table.
        for prefix_match in re.finditer(
            r'recommenders/(google\.[^"]+)"\s*\+\s*type', self.content
        ):
            prefix = prefix_match.group(1).rstrip('.')
            for suffix in re.findall(r',\s*"(\w+Recommender)"', self.content):
                found_type_ids.add(f'{prefix}.{suffix}')

        result = []
        for type_id in sorted(found_type_ids):
            perm = RECOMMENDER_TYPE_TO_PERMISSION.get(type_id)
            if perm:
                result.append({
                    'policy_name': self.policy_name,
                    'datasource_name': 'recommender_' + type_id.split('.')[-1],
                    'method': 'GET',
                    'endpoint': (
                        'https://recommender.googleapis.com/v1/projects/{id}'
                        f'/locations/{{region}}/recommenders/{type_id}/recommendations'
                    ),
                    'operation': f'List {type_id.split(".")[-1]} Recommendations',
                    'field': '{entire response}',
                    'api_service': 'GCP',
                    'permission': perm,
                })
        return result

    def _add_gcp_implicit_paired_permissions(self, api_calls):
        """Add GCP permissions implicitly required alongside another permission.

        Some GCP operations require permissions on two different resources. The canonical
        example is disk snapshot creation: compute.disks.createSnapshot (on the source disk)
        always requires compute.snapshots.create (on the destination snapshot resource).
        These companion permissions cannot be derived from the API call alone, but they are
        a fixed GCP IAM invariant with no exceptions.
        """
        # Map: source permission -> list of implicit companion permissions
        IMPLICIT_PAIRS = {
            'compute.disks.createSnapshot': ['compute.snapshots.create'],
        }

        existing = {(c['policy_name'], c.get('permission')) for c in api_calls}

        additions = []
        for call in api_calls:
            perm = call.get('permission')
            if perm in IMPLICIT_PAIRS:
                for companion in IMPLICIT_PAIRS[perm]:
                    key = (call['policy_name'], companion)
                    if key not in existing:
                        new_call = dict(call)
                        new_call['permission'] = companion
                        new_call['datasource_name'] = call['datasource_name'] + '_implicit'
                        additions.append(new_call)
                        existing.add(key)

        return api_calls + additions

    def _expand_dynamic_gcp_type_permissions(self, api_calls):
        """
        Replace placeholder GCP compute permissions that contain a variable resource type
        (e.g. compute.{type}.aggregatedList or compute.{type}.list) with one entry per
        literal type found in the template source.

        When multiple 'types = [...]' JS arrays exist (e.g. separate arrays for /global/
        and /aggregated/ paths), this method traces the chain:
          JS script (types) → generator datasource (run_script) → consumer datasource (iterate, path)
        to associate each type list with the correct suffix (aggregatedList vs list).
        Falls back to using all types for all placeholders when the chain cannot be traced.
        """
        placeholder_re = re.compile(r'^compute\.\{[^}]+\}\.(aggregatedList|list)$')
        if not any(placeholder_re.match(c.get('permission') or '') for c in api_calls):
            return api_calls

        # --- Step 1: Collect type arrays per named JS script ---
        js_types = {}  # script_name -> [type, ...]
        for m in re.finditer(
            r'\bscript\s+"([^"]+)".*?^end\b',
            self.content, re.MULTILINE | re.DOTALL
        ):
            sname = m.group(1)
            body = m.group(0)
            types = []
            for raw in re.findall(r'\btypes\s*=\s*\[([^\]]+)\]', body, re.DOTALL):
                types.extend(re.findall(r'["\']([A-Za-z][A-Za-z0-9_]+)["\']', raw))
            if types:
                js_types[sname] = list(dict.fromkeys(types))

        if not js_types:
            return api_calls

        # --- Step 2: Map generator datasource → script name ---
        gen_ds_map = {}  # ds_name -> script_name
        for m in re.finditer(
            r'\bdatasource\s+"([^"]+)".*?^end\b',
            self.content, re.MULTILINE | re.DOTALL
        ):
            ds_name = m.group(1)
            body = m.group(0)
            for sname in js_types:
                if re.search(r'\$' + re.escape(sname) + r'\b', body):
                    gen_ds_map[ds_name] = sname
                    break

        # --- Step 3: Map suffix → types by tracing iterate → path ---
        suffix_types = {'aggregatedList': [], 'list': []}
        for m in re.finditer(
            r'\bdatasource\s+"[^"]*".*?^end\b',
            self.content, re.MULTILINE | re.DOTALL
        ):
            body = m.group(0)
            iter_m = re.search(r'\biterate\s+\$(\w+)', body)
            if not iter_m or iter_m.group(1) not in gen_ds_map:
                continue
            sname = gen_ds_map[iter_m.group(1)]
            types = js_types[sname]
            # Identify suffix from path string inside this datasource
            path_src = ' '.join(re.findall(r'"(/compute/v1[^"]+)"', body))
            path_src += ' '.join(re.findall(r"'(/compute/v1[^']+)'", body))
            for join_args in re.findall(r'join\(\s*\[([^\]]+)\]', body):
                path_src += ''.join(re.findall(r'"([^"]+)"', join_args))
                path_src += ''.join(re.findall(r"'([^']+)'", join_args))
            if '/aggregated/' in path_src:
                suffix_types['aggregatedList'].extend(types)
            elif '/global/' in path_src:
                suffix_types['list'].extend(types)

        for k in suffix_types:
            suffix_types[k] = list(dict.fromkeys(suffix_types[k]))

        # Fallback: if tracing failed, combine all types for all suffixes
        all_types = list(dict.fromkeys(
            [t for tl in js_types.values() for t in tl]
        ))

        expanded = []
        for call in api_calls:
            perm = call.get('permission') or ''
            m = placeholder_re.match(perm)
            if m:
                suffix = m.group(1)
                types = suffix_types.get(suffix) or all_types
                if not types:
                    expanded.append(call)
                    continue
                for resource_type in types:
                    expanded_call = dict(call)
                    expanded_call['permission'] = f'compute.{resource_type}.{suffix}'
                    expanded.append(expanded_call)
            else:
                expanded.append(call)
        return expanded


def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(description='Extract REST API calls from Flexera Policy Templates.')
    parser.add_argument(
        '--output-dir',
        metavar='DIR',
        default=None,
        help='Write output files to DIR instead of the default data/policy_api_list/ directory.'
    )
    args = parser.parse_args()

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

        # Skip meta parent policies
        if '_meta_parent.pt' in str(policy_file):
            continue

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
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = repo_root / 'data' / 'policy_api_list'
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write to JSON
    json_output_file = output_dir / 'policy_api_list.json'
    with open(json_output_file, 'w') as f:
        json.dump({
            'api_calls': all_api_calls
        }, f, indent=2)

    print(f"JSON output written to: {json_output_file}")

    # Write to CSV
    csv_output_file = output_dir / 'policy_api_list.csv'
    with open(csv_output_file, 'w', newline='') as csvfile:
        fieldnames = ['policy_name', 'policy_file', 'policy_version', 'datasource_name', 'api_service', 'method', 'endpoint', 'operation', 'field', 'permission']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for call in all_api_calls:
            writer.writerow(call)

    print(f"CSV output written to: {csv_output_file}")


if __name__ == '__main__':
    main()
