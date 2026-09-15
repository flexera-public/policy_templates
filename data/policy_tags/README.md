# Policy Tags Data

Canonical, manually maintained data assets describing the discrete tag
vocabulary used to classify policy templates by use case: cloud provider,
specific service, cost optimization pattern, compliance framework, internal
Flexera operations, and similar dimensions.

## Manually Maintained Files

### all_tags.json

**Description:** A JSON array of every approved tag that may be applied to a
policy template, along with a human-readable description of what the tag means
and when it should be used. This is the single source of truth for the tag
vocabulary; policy template authors should only use tags that appear in this
file when tagging a `.pt` file, and any new use case should be added here
first.

**Structure:** Array of objects, one per tag.

| Field | Type | Description |
| --- | --- | --- |
| `tag` | string | The exact, case-sensitive tag value to apply to a policy template. |
| `description` | string | A one or two sentence explanation of what kinds of policy templates the tag applies to. |

**Example:**

```json
{
  "tag": "EC2",
  "description": "Policy templates focused on Amazon EC2 compute instances."
}
```
