# Flexera Policy Template Versioning

Flexera policy templates use [semantic versioning](https://semver.org/). This means all version numbers should contain three period-separated integers (example: `1.27.3`) that represent the MAJOR, MINOR, and PATCH versions respectively.

- MAJOR version should be changed if someone using automation to apply the updated policy template would run into an error or unexpected outcomes due to changes in parameters or fundamental changes in how the policy template works or what it does.
- MINOR version should be changed if new functionality or features are added in a way that does not fundamentally change what the policy template does and would not cause errors or problems for someone automating application of the policy template. For example, if new functionality were added with a parameter whose default value disables the new functionality.
- PATCH version should be changed for bug fixes or other minor changes that don't actually add new features or functionality, provided that the change does not meet the criteria for a MAJOR version change.

**Note:** Some existing policy templates will be missing a PATCH version. Semantic versioning was not officially adopted as a practice for the catalog until 2024, and some policies have not been updated since then. In such cases, the PATCH version should be considered `0`. For example, a policy template with version `4.2` would be equivalent to `4.2.0`, and should be incremented accordingly if an update is being made.
