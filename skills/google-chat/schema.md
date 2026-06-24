# Google Chat Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `google-chat`

x402 availability: not enabled for this product.

## `add_reaction`

Action slug: `add-reaction`

Price: `5` credits

Add an emoji reaction to a message.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `emoji_unicode` | `string` | yes | Unicode emoji character to react with (e.g., '👍'). |
| `message_name` | `string` | yes | Message resource name or message ID (e.g., 'spaces/AAA/messages/BBB'). |
| `space` | `string` | no | Space name or ID, needed if message_name is a short ID. |

Sample parameters:

```json
{
  "emoji_unicode": "example emoji unicode",
  "message_name": "example message name",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "emoji_unicode": {
    "description": "Unicode emoji character to react with (e.g., '👍').",
    "required": true,
    "type": "string"
  },
  "message_name": {
    "description": "Message resource name or message ID (e.g., 'spaces/AAA/messages/BBB').",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Space name or ID, needed if message_name is a short ID.",
    "required": false,
    "type": "string"
  }
}
```

## `create_message`

Action slug: `create-message`

Price: `5` credits

Send a new message to a Google Chat space. Optionally post into an existing thread.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `cards_v2` | `array` | no | Cards v2 payload for rich card messages. Alternative to text. |
| `space` | `string` | yes | Space name or ID (e.g., 'spaces/AAA' or 'AAA'). |
| `text` | `string` | no | Message text content. Required if cards_v2 is not provided. |
| `thread_name` | `string` | no | Thread resource name (e.g., 'spaces/AAA/threads/CCC') to post into an existing thread. |

Sample parameters:

```json
{
  "cards_v2": [
    {}
  ],
  "space": "example space",
  "text": "example text",
  "thread_name": "example thread name"
}
```

Generated JSON parameter schema:

```json
{
  "cards_v2": {
    "description": "Cards v2 payload for rich card messages. Alternative to text.",
    "items": {
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "space": {
    "description": "Space name or ID (e.g., 'spaces/AAA' or 'AAA').",
    "required": true,
    "type": "string"
  },
  "text": {
    "description": "Message text content. Required if cards_v2 is not provided.",
    "required": false,
    "type": "string"
  },
  "thread_name": {
    "description": "Thread resource name (e.g., 'spaces/AAA/threads/CCC') to post into an existing thread.",
    "required": false,
    "type": "string"
  }
}
```

## `delete_message`

Action slug: `delete-message`

Price: `5` credits

Delete a message from a Google Chat space.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `message_name` | `string` | yes | Message resource name or message ID (e.g., 'spaces/AAA/messages/BBB'). |
| `space` | `string` | no | Space name or ID, needed if message_name is a short ID. |

Sample parameters:

```json
{
  "message_name": "example message name",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "message_name": {
    "description": "Message resource name or message ID (e.g., 'spaces/AAA/messages/BBB').",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Space name or ID, needed if message_name is a short ID.",
    "required": false,
    "type": "string"
  }
}
```

## `delete_reaction`

Action slug: `delete-reaction`

Price: `5` credits

Remove a reaction from a message.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `message_name` | `string` | no | Message resource name, needed if reaction_name is a short ID. |
| `reaction_name` | `string` | yes | Reaction resource name or reaction ID (e.g., 'spaces/AAA/messages/BBB/reactions/RRR'). |
| `space` | `string` | no | Space name or ID, needed if both reaction_name and message_name are short IDs. |

Sample parameters:

```json
{
  "message_name": "example message name",
  "reaction_name": "example reaction name",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "message_name": {
    "description": "Message resource name, needed if reaction_name is a short ID.",
    "required": false,
    "type": "string"
  },
  "reaction_name": {
    "description": "Reaction resource name or reaction ID (e.g., 'spaces/AAA/messages/BBB/reactions/RRR').",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Space name or ID, needed if both reaction_name and message_name are short IDs.",
    "required": false,
    "type": "string"
  }
}
```

## `get_attachment`

Action slug: `get-attachment`

Price: `5` credits

Retrieve metadata for an attachment on a message.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `attachment_name` | `string` | yes | Attachment resource name or attachment ID (e.g., 'spaces/AAA/messages/BBB/attachments/ATT'). |
| `message_name` | `string` | no | Message resource name, needed if attachment_name is a short ID. |
| `space` | `string` | no | Space name or ID, needed if both attachment_name and message_name are short IDs. |

Sample parameters:

```json
{
  "attachment_name": "example attachment name",
  "message_name": "example message name",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "attachment_name": {
    "description": "Attachment resource name or attachment ID (e.g., 'spaces/AAA/messages/BBB/attachments/ATT').",
    "required": true,
    "type": "string"
  },
  "message_name": {
    "description": "Message resource name, needed if attachment_name is a short ID.",
    "required": false,
    "type": "string"
  },
  "space": {
    "description": "Space name or ID, needed if both attachment_name and message_name are short IDs.",
    "required": false,
    "type": "string"
  }
}
```

## `list_members`

Action slug: `list-members`

Price: `5` credits

List members of a specific Google Chat space.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `filter` | `string` | no | Filter query for members. |
| `page_size` | `integer` | no | Maximum number of results per page. |
| `page_token` | `string` | no | Pagination token from a previous response. |
| `space` | `string` | yes | Space name or ID (e.g., 'spaces/AAA' or 'AAA'). |

Sample parameters:

```json
{
  "filter": "example filter",
  "page_size": 50,
  "page_token": "example page token",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "filter": {
    "description": "Filter query for members.",
    "required": false,
    "type": "string"
  },
  "page_size": {
    "default": 50,
    "description": "Maximum number of results per page.",
    "maximum": 1000,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token from a previous response.",
    "required": false,
    "type": "string"
  },
  "space": {
    "description": "Space name or ID (e.g., 'spaces/AAA' or 'AAA').",
    "required": true,
    "type": "string"
  }
}
```

## `list_messages`

Action slug: `list-messages`

Price: `5` credits

List messages in a Google Chat space in reverse chronological order (newest first). The filter parameter supports createTime and thread.name only; full-text search is not supported.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `filter` | `string` | no | Filter query. Supports createTime and thread.name only (e.g., 'createTime > "2025-01-01T00:00:00Z"'). |
| `page_size` | `integer` | no | Maximum number of results per page. |
| `page_token` | `string` | no | Pagination token from a previous response. |
| `space` | `string` | yes | Space name or ID (e.g., 'spaces/AAA' or 'AAA'). |

Sample parameters:

```json
{
  "filter": "example filter",
  "page_size": 50,
  "page_token": "example page token",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "filter": {
    "description": "Filter query. Supports createTime and thread.name only (e.g., 'createTime > \"2025-01-01T00:00:00Z\"').",
    "required": false,
    "type": "string"
  },
  "page_size": {
    "default": 50,
    "description": "Maximum number of results per page.",
    "maximum": 1000,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token from a previous response.",
    "required": false,
    "type": "string"
  },
  "space": {
    "description": "Space name or ID (e.g., 'spaces/AAA' or 'AAA').",
    "required": true,
    "type": "string"
  }
}
```

## `list_reactions`

Action slug: `list-reactions`

Price: `5` credits

List all emoji reactions on a message.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `message_name` | `string` | yes | Message resource name or message ID (e.g., 'spaces/AAA/messages/BBB'). |
| `page_size` | `integer` | no | Maximum number of results per page. |
| `page_token` | `string` | no | Pagination token from a previous response. |
| `space` | `string` | no | Space name or ID, needed if message_name is a short ID. |

Sample parameters:

```json
{
  "message_name": "example message name",
  "page_size": 50,
  "page_token": "example page token",
  "space": "example space"
}
```

Generated JSON parameter schema:

```json
{
  "message_name": {
    "description": "Message resource name or message ID (e.g., 'spaces/AAA/messages/BBB').",
    "required": true,
    "type": "string"
  },
  "page_size": {
    "default": 50,
    "description": "Maximum number of results per page.",
    "maximum": 1000,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token from a previous response.",
    "required": false,
    "type": "string"
  },
  "space": {
    "description": "Space name or ID, needed if message_name is a short ID.",
    "required": false,
    "type": "string"
  }
}
```

## `list_spaces`

Action slug: `list-spaces`

Price: `5` credits

List all Google Chat spaces the authenticated user has access to.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `filter` | `string` | no | Filter query (e.g., 'spaceType = "SPACE"'). |
| `page_size` | `integer` | no | Maximum number of results per page. |
| `page_token` | `string` | no | Pagination token from a previous response to fetch the next page. |

Sample parameters:

```json
{
  "filter": "example filter",
  "page_size": 50,
  "page_token": "example page token"
}
```

Generated JSON parameter schema:

```json
{
  "filter": {
    "description": "Filter query (e.g., 'spaceType = \"SPACE\"').",
    "required": false,
    "type": "string"
  },
  "page_size": {
    "default": 50,
    "description": "Maximum number of results per page.",
    "maximum": 1000,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token from a previous response to fetch the next page.",
    "required": false,
    "type": "string"
  }
}
```

## `reply_message`

Action slug: `reply-message`

Price: `5` credits

Reply to an existing message in its thread. The thread is resolved automatically from the original message.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `cards_v2` | `array` | no | Cards v2 payload for rich card replies. Alternative to text. |
| `message_name` | `string` | yes | Message resource name or message ID (e.g., 'spaces/AAA/messages/BBB'). The thread is resolved from this message. |
| `space` | `string` | no | Space name or ID, needed if message_name is a short ID rather than a full resource name. |
| `text` | `string` | no | Reply text content. Required if cards_v2 is not provided. |

Sample parameters:

```json
{
  "cards_v2": [
    {}
  ],
  "message_name": "example message name",
  "space": "example space",
  "text": "example text"
}
```

Generated JSON parameter schema:

```json
{
  "cards_v2": {
    "description": "Cards v2 payload for rich card replies. Alternative to text.",
    "items": {
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "message_name": {
    "description": "Message resource name or message ID (e.g., 'spaces/AAA/messages/BBB'). The thread is resolved from this message.",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Space name or ID, needed if message_name is a short ID rather than a full resource name.",
    "required": false,
    "type": "string"
  },
  "text": {
    "description": "Reply text content. Required if cards_v2 is not provided.",
    "required": false,
    "type": "string"
  }
}
```

## `update_message`

Action slug: `update-message`

Price: `5` credits

Edit an existing message. Only the fields provided (text and/or cards_v2) will be updated.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `cards_v2` | `array` | no | Updated cards v2 payload. Alternative to text. |
| `message_name` | `string` | yes | Message resource name or message ID (e.g., 'spaces/AAA/messages/BBB'). |
| `space` | `string` | no | Space name or ID, needed if message_name is a short ID. |
| `text` | `string` | no | Updated message text. Required if cards_v2 is not provided. |

Sample parameters:

```json
{
  "cards_v2": [
    {}
  ],
  "message_name": "example message name",
  "space": "example space",
  "text": "example text"
}
```

Generated JSON parameter schema:

```json
{
  "cards_v2": {
    "description": "Updated cards v2 payload. Alternative to text.",
    "items": {
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "message_name": {
    "description": "Message resource name or message ID (e.g., 'spaces/AAA/messages/BBB').",
    "required": true,
    "type": "string"
  },
  "space": {
    "description": "Space name or ID, needed if message_name is a short ID.",
    "required": false,
    "type": "string"
  },
  "text": {
    "description": "Updated message text. Required if cards_v2 is not provided.",
    "required": false,
    "type": "string"
  }
}
```
