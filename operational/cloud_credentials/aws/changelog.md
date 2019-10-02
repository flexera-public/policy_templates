v1.6
----
- Added Approval block

v1.5
----
- Simplified logic such that the policy checks to see if there are already more than one keys for the IAM user and then removes a key before trying to create a new key.
  - This removes the generation of an API error about hitting the key quota when creating the key.
- User-specifiable rotation period units (days, hours, minutes) option.
  
v1.4
----
- Added logic to deactivate the previously used key.

v1.3
----
- Fixed typo in call to "log()" definition.

v1.2
----
- Upating Policy Template Name

v1.1
----
- Update email subject with account name and ID. Issue #75

v1.0
----
- initial release
