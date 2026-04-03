# Catalog Management

Policy templates for managing the Flexera Public Policy Catalog. These templates are designed to be applied in a Flexera organization to keep the catalog synchronized with the policy templates in this repository.

## Templates

### [Policy Template Synchronization](./policy_sync/)

Synchronizes the policy templates published in a Flexera organization's catalog with the active policy list in this repository. It publishes new templates, updates out-of-date published templates, and optionally unpublishes defunct templates that are no longer in the active list.

### [Hidden Policy Templates](./hidden_policies/)

Reports on policy templates in the catalog that are flagged as `hidden`. Can optionally unhide or delete them. This template is intended to be used alongside Policy Template Synchronization because updated templates may be temporarily hidden in the catalog during the publish process; automatically unhiding them ensures updates are not inadvertently suppressed.

## Recommended Setup

Deploy both templates together in the same Flexera organization:

1. Apply **Hidden Policy Templates** with automatic actions enabled to unhide (or delete) hidden templates.
1. Apply **Policy Template Synchronization** with automatic actions enabled to publish new and updated templates.

This ensures that the catalog stays in sync with the repository on an ongoing basis without manual intervention.
