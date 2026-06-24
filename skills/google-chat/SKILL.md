---
name: google-chat
description: "Google Chat: Post to Google Chat spaces, send DMs, read messages. Supports reactions. Actions performed as connected user. Use when an agent needs google chat, send messages to spaces, reply in existing threads, list recent messages, filter message history, add reaction, message name, space through AgentPMT-hosted remote tool calls. Search keywords: google chat, send messages to spaces, reply in existing threads, list recent messages, filter message history, add reaction, message name, space."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/google-chat
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/google-chat"}}
---
# Google Chat

## Freshness
Last updated: `2026-06-24`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Bridge your agent to your Google Chat spaces—post updates, keep threads moving, and turn routine teamwork into quick, automated nudges that keep everyone in sync. Supports reactions, direct messaging, and posting and reading in spaces. All actions take place as the connected user.

## Product Instructions
### Google Chat

Send messages, manage spaces, react to messages, and read conversation history in Google Chat.

#### Actions

##### list_spaces
Lists all Google Chat spaces the authenticated user has access to.

**Required fields:** none

**Optional fields:** `page_size`, `page_token`, `filter`

**Example — list all spaces:**
```json
{"action": "list_spaces"}
```

**Example — filter to group spaces only:**
```json
{"action": "list_spaces", "page_size": 10, "filter": "spaceType = \"SPACE\""}
```

---

##### list_members
Lists members of a specific space.

**Required fields:** `space`

**Optional fields:** `page_size`, `page_token`, `filter`

**Example:**
```json
{"action": "list_members", "space": "spaces/AAA"}
```

---

##### list_messages
Lists messages in a space in reverse chronological order (newest first).

**Required fields:** `space`

**Optional fields:** `page_size`, `page_token`, `filter`

The `filter` parameter supports `createTime` and `thread.name` only. Full-text search is not supported.

**Example — recent messages:**
```json
{"action": "list_messages", "space": "spaces/AAA", "page_size": 20}
```

**Example — messages after a date:**
```json
{"action": "list_messages", "space": "spaces/AAA", "filter": "createTime > \"2025-01-01T00:00:00Z\""}
```

---

##### create_message
Sends a new message to a space. Optionally post into an existing thread.

**Required fields:** `space`, and one of `text` or `cards_v2`

**Optional fields:** `thread_name`

**Example — simple text message:**
```json
{"action": "create_message", "space": "spaces/AAA", "text": "Hello from the agent!"}
```

**Example — post into an existing thread:**
```json
{"action": "create_message", "space": "spaces/AAA", "text": "Continuing this thread", "thread_name": "spaces/AAA/threads/CCC"}
```

---

##### reply_message
Replies to an existing message in its thread. The thread is resolved automatically from the original message.

**Required fields:** `message_name`, and one of `text` or `cards_v2`

Use `message_name` (not `thread_name`) to identify the message you are replying to.

**Example:**
```json
{"action": "reply_message", "message_name": "spaces/AAA/messages/BBB", "text": "Got it, thanks!"}
```

---

##### update_message
Edits an existing message. Only the fields you provide (`text` and/or `cards_v2`) will be updated.

**Required fields:** `message_name`, and one of `text` or `cards_v2`

**Example:**
```json
{"action": "update_message", "message_name": "spaces/AAA/messages/BBB", "text": "Updated text"}
```

---

##### delete_message
Deletes a message.

**Required fields:** `message_name`

**Example:**
```json
{"action": "delete_message", "message_name": "spaces/AAA/messages/BBB"}
```

---

##### list_reactions
Lists all emoji reactions on a message.

**Required fields:** `message_name`

**Optional fields:** `page_size`, `page_token`

**Example:**
```json
{"action": "list_reactions", "message_name": "spaces/AAA/messages/BBB"}
```

---

##### add_reaction
Adds an emoji reaction to a message.

**Required fields:** `message_name`, `emoji_unicode`

**Example:**
```json
{"action": "add_reaction", "message_name": "spaces/AAA/messages/BBB", "emoji_unicode": "👍"}
```

---

##### delete_reaction
Removes a reaction from a message.

**Required fields:** `reaction_name`

When using a short reaction ID instead of a full resource name, also provide `message_name`.

**Example:**
```json
{"action": "delete_reaction", "reaction_name": "spaces/AAA/messages/BBB/reactions/RRR"}
```

---

##### get_attachment
Retrieves metadata for an attachment on a message.

**Required fields:** `attachment_name`

When using a short attachment ID instead of a full resource name, also provide `message_name`.

**Example:**
```json
{"action": "get_attachment", "attachment_name": "spaces/AAA/messages/BBB/attachments/ATT"}
```

---

#### Common Workflows

**Post a message and react to it:**
1. `create_message` with `space` and `text` — note the returned message name
2. `add_reaction` with the returned `message_name` and `emoji_unicode`

**Monitor a space for recent activity:**
1. `list_messages` with `space` and a `filter` on `createTime`
2. Page through results using `page_token` if needed

**Reply to the latest message in a space:**
1. `list_messages` with `space` and `page_size` of 1 to get the most recent message
2. `reply_message` with the returned `message_name` and your reply `text`

#### Resource Name Formats

- Space: `spaces/AAA`
- Message: `spaces/AAA/messages/BBB`
- Thread: `spaces/AAA/threads/CCC`
- Reaction: `spaces/AAA/messages/BBB/reactions/RRR`
- Attachment: `spaces/AAA/messages/BBB/attachments/ATT`

Short IDs (e.g., just `BBB`) are accepted when paired with the parent resource (`space` or `message_name`).

#### Important Notes

- The `filter` parameter for `list_messages` supports only `createTime` and `thread.name`. Full-text search of message content is not available.
- `reply_message` automatically resolves the thread from the original message — just provide `message_name`.
- To post into an existing thread without replying to a specific message, use `create_message` with `thread_name`.
- `cards_v2` can be used as an alternative to `text` for rich card messages in `create_message`, `reply_message`, and `update_message`.
- Pagination: use `page_size` (1-1000, default 50) and `page_token` from previous responses to page through results.

## When To Use
- Use this skill for `Google Chat` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: google chat, send messages to spaces, reply in existing threads, list recent messages, filter message history, add reaction, message name, space.
- Supported action names: `add_reaction`, `create_message`, `delete_message`, `delete_reaction`, `get_attachment`, `list_members`, `list_messages`, `list_reactions`, `list_spaces`, `reply_message`, `update_message`.

## Use Cases
- Send messages to spaces
- Reply in existing threads
- List recent messages
- Filter message history
- Add or remove reactions
- Retrieve space memberships
- Fetch attachment metadata
- Automate team notifications

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `11`.
x402 availability: not enabled for this product.

- `add_reaction` (action slug: `add-reaction`): Add an emoji reaction to a message. Price: `5` credits. Parameters: `emoji_unicode`, `message_name`, `space`.
- `create_message` (action slug: `create-message`): Send a new message to a Google Chat space. Optionally post into an existing thread. Price: `5` credits. Parameters: `cards_v2`, `space`, `text`, `thread_name`.
- `delete_message` (action slug: `delete-message`): Delete a message from a Google Chat space. Price: `5` credits. Parameters: `message_name`, `space`.
- `delete_reaction` (action slug: `delete-reaction`): Remove a reaction from a message. Price: `5` credits. Parameters: `message_name`, `reaction_name`, `space`.
- `get_attachment` (action slug: `get-attachment`): Retrieve metadata for an attachment on a message. Price: `5` credits. Parameters: `attachment_name`, `message_name`, `space`.
- `list_members` (action slug: `list-members`): List members of a specific Google Chat space. Price: `5` credits. Parameters: `filter`, `page_size`, `page_token`, `space`.
- `list_messages` (action slug: `list-messages`): List messages in a Google Chat space in reverse chronological order (newest first). The filter parameter supports createTime and thread.name only; full-text search is not supported. Price: `5` credits. Parameters: `filter`, `page_size`, `page_token`, `space`.
- `list_reactions` (action slug: `list-reactions`): List all emoji reactions on a message. Price: `5` credits. Parameters: `message_name`, `page_size`, `page_token`, `space`.
- `list_spaces` (action slug: `list-spaces`): List all Google Chat spaces the authenticated user has access to. Price: `5` credits. Parameters: `filter`, `page_size`, `page_token`.
- `reply_message` (action slug: `reply-message`): Reply to an existing message in its thread. The thread is resolved automatically from the original message. Price: `5` credits. Parameters: `cards_v2`, `message_name`, `space`, `text`.
- `update_message` (action slug: `update-message`): Edit an existing message. Only the fields provided (text and/or cards_v2) will be updated. Price: `5` credits. Parameters: `cards_v2`, `message_name`, `space`, `text`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "google-chat"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "google-chat"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "google-chat"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "google-chat"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "google-chat"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "google-chat"
  }
}
```

## Call This Tool
Product slug: `google-chat`

Marketplace page: https://www.agentpmt.com/marketplace/google-chat

- AgentPMT account route: first use `../agentpmt-account-mcp-rest-api-setup` to connect the main MCP server or REST API for an Agent Group where this tool is enabled.
- x402 route: not enabled for this product.
- AgentPMT overview: use `../what-is-agentpmt` for marketplace, Agent Group, workflow, MCP, REST, and payment concepts.

If those setup skills are not installed beside this product skill, use the downloads below.

Core AgentPMT setup skills:
- What AgentPMT is: ../what-is-agentpmt
  - ClawHub page: https://clawhub.ai/agentpmt/what-is-agentpmt
  - OpenClaw install: `openclaw skills install what-is-agentpmt`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup
  - ClawHub page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup
  - OpenClaw install: `openclaw skills install agentpmt-account-mcp-rest-api-setup`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`

skills.sh install script:

```bash
npx skills add AgentPMT/agent-skills --skill what-is-agentpmt
npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup
```

MCP call shape after the main AgentPMT MCP server is connected:

```json
{
  "method": "tools/call",
  "params": {
    "name": "Google-Chat",
    "arguments": {
      "action": "add_reaction",
      "emoji_unicode": "example emoji unicode",
      "message_name": "example message name",
      "space": "example space"
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "google-chat",
  "parameters": {
    "action": "add_reaction",
    "emoji_unicode": "example emoji unicode",
    "message_name": "example message name",
    "space": "example space"
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `add_reaction` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/google-chat
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
