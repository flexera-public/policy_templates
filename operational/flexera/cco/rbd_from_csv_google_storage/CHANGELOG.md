# Changelog

## v0.1.1

- Improved performance of CSV parser by collecting characters into an array and joining at field boundaries, avoiding repeated string concatenation in a tight loop
- Improved performance of dimension header resolution by building ID and name lookup tables up front instead of scanning the dimensions list for each header
- Improved performance of RBD column index resolution by building an index map instead of calling `_.indexOf` in a loop
- Replaced full `$ds_create_rbds` response array passed to `js_apply_rbds` with a lightweight boolean sentinel to reduce per-invocation memory load
- Eliminated the trivial `ds_incident_findings` passthrough datasource; the policy block now references `ds_csv_validated` directly
- Extracted RBD name derivation logic in `js_incident_rbds` into a named helper function to remove inline duplication

## v0.1.0

- Initial release
