---
name: minecraft-custom-mod-builder
description: "Minecraft Custom Mod Builder: Deterministically generate, validate, preview, and test Minecraft Bedrock, Bedrock skin pack, Fabric, and NeoForge projects from structured. Use when an agent needs minecraft custom mod builder, create verified minecraft bedrock add ons (.mcaddon), build fabric and neoforge source projects and jars through async build jobs, generate bedrock skin packs (.mcpack), create items, create mod project, target platform, mod id through AgentPMT-hosted remote tool calls."
version: 1.0.4
homepage: https://www.agentpmt.com/marketplace/minecraft-custom-mod-builder
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/minecraft-custom-mod-builder"}}
---
# Minecraft Custom Mod Builder

## Freshness
Last updated: `2026-07-09`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Create structured Minecraft Bedrock add-ons, Bedrock skin packs, and Java Fabric/NeoForge mod projects with strict schemas, texture binding, validation, async build jobs, and install-readiness reporting. Use the verified async build path for anything a user should install; use source output and uploaded-source test jobs when an agent needs to edit code directly.

## Product Instructions
Use get_instructions as the canonical source before writing complex Minecraft specs. For final user-deliverable mods, call start_build_job, poll get_build_job, and ship only when result.ready_for_install is true and result.quality_gate.status is 'passed'. Synchronous create_mod_project is for quick unverified source/debug output; do not present it as a working final mod. If a requested behavior is beyond the declarative schema, use the agent-edited source loop: generate source, edit the code, upload the zip, then call start_build_job with source_archive_file_id, source_test_mode='test_only' while iterating, and a verification_contract.expected_checks list that states what the edited source must prove. Rerun with source_test_mode='test_and_package' only when the quality gate passes. Do not silently substitute a nearby mechanic for the user's intent; use fidelity_policy='acknowledged_approximation' only after explicit user approval. Placeholder/scaffolding-only actions require fidelity_policy='allow_explicit_stub' and always produce non-install-ready output until real source code is added and verified. Platform-mismatched features are validation failures, not warnings and not silently filtered.

## When To Use
- Use this skill for `Minecraft Custom Mod Builder` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: minecraft custom mod builder, create verified minecraft bedrock add ons (.mcaddon), build fabric and neoforge source projects and jars through async build jobs, generate bedrock skin packs (.mcpack), create items, create mod project, target platform, mod id.
- Supported action names: `create_mod_project`, `get_build_job`, `get_instructions`, `list_build_jobs`, `list_capabilities`, `render_preview_image`, `start_build_job`, `validate_mod_project`.

## Use Cases
- Create verified Minecraft Bedrock add-ons (.mcaddon)
- Build Fabric and NeoForge source projects and jars through async build jobs
- Generate Bedrock skin packs (.mcpack)
- Create items
- weapons
- tools
- armor
- blocks
- ores
- food
- mobs
- bosses
- recipes
- loot tables
- enchantments
- trades

## Related Product Skills
- Icon Generator: ../product-icon-generator (ClawHub: `product-icon-generator`, page: https://clawhub.ai/agentpmt/product-icon-generator; skills.sh: `npx skills add AgentPMT/agent-skills --skill product-icon-generator`)
- File Management: ../file-management (ClawHub: `file-management`, page: https://clawhub.ai/agentpmt/file-management; skills.sh: `npx skills add AgentPMT/agent-skills --skill file-management`)

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `8`.
x402 action routes are enabled and listed in `./schema.md`.

- `create_mod_project` (action slug: `create-mod-project`): Synchronous unverified source/debug generation. Accepts only verification_level='off'; use start_build_job for install-ready final artifacts. Price: `15` credits. Parameters: `advanced_resources`, `allow_experimental_bedrock_features`, `assets`, `build_jar`, `compatibility_mode`, `description`, `features`, `fidelity_policy`, plus 11 more.
- `get_build_job` (action slug: `get-build-job`): Fetch one queued Minecraft build job by task_id. Poll after start_build_job until status is completed or failed; inspect result.ready_for_install and quality_gate. Price: `2` credits. Parameters: `task_id`, `timeout_seconds`.
- `get_instructions` (action slug: `get-instructions`): Return the canonical Minecraft Mod Builder instructions. Call before authoring complex specs or source-archive verification contracts. Price: `1` credits. Parameters: none.
- `list_build_jobs` (action slug: `list-build-jobs`): List recent Minecraft build jobs for the active budget to recover task_id values or inspect recent queued/completed builds. Price: `2` credits. Parameters: `limit`, `timeout_seconds`.
- `list_capabilities` (action slug: `list-capabilities`): Return supported platforms, pinned versions, feature/action matrices, implementation_status, quality-gate fields, and unsupported families. Price: `2` credits. Parameters: `target_platform`.
- `render_preview_image` (action slug: `render-preview-image`): Render and upload an enlarged PNG preview for an item, block, entity, texture, source archive, or direct image file. Price: `5` credits. Parameters: `features`, `mod_id`, `mod_name`, `preview_background`, `preview_size`, `preview_source_file_id`, `preview_target_id`, `preview_target_kind`, plus 3 more.
- `start_build_job` (action slug: `start-build-job`): Queue verified async generation or uploaded-source testing. Poll get_build_job and ship only when result.ready_for_install=true and quality_gate.status='passed'. Price: `15` credits. Parameters: `advanced_resources`, `allow_experimental_bedrock_features`, `assets`, `build_jar`, `compatibility_mode`, `description`, `features`, `fidelity_policy`, plus 14 more.
- `validate_mod_project` (action slug: `validate-mod-project`): Validate a structured Minecraft mod spec or a previously generated/uploaded source archive without writing install artifacts. Price: `5` credits. Parameters: `allow_experimental_bedrock_features`, `features`, `minecraft_version`, `mod_id`, `mod_name`, `skin_pack`, `source_archive_file_id`, `target_platform`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "minecraft-custom-mod-builder"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "minecraft-custom-mod-builder"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "minecraft-custom-mod-builder"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "minecraft-custom-mod-builder"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "minecraft-custom-mod-builder"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "minecraft-custom-mod-builder"
  }
}
```

## Call This Tool
Product slug: `minecraft-custom-mod-builder`

Marketplace page: https://www.agentpmt.com/marketplace/minecraft-custom-mod-builder

- AgentPMT account route: first use `../agentpmt-account-mcp-rest-api-setup` to connect the main MCP server or REST API for an Agent Group where this tool is enabled.
- No-account AgentAddress/x402 route: first use `../agentpmt-no-account-agentaddress-x402` for the canonical payment and wallet setup instructions.
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
- No-account AgentAddress/x402 setup: ../agentpmt-no-account-agentaddress-x402
  - ClawHub page: https://clawhub.ai/agentpmt/agentpmt-no-account-agentaddress-x402
  - OpenClaw install: `openclaw skills install agentpmt-no-account-agentaddress-x402`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill agentpmt-no-account-agentaddress-x402`

skills.sh install script:

```bash
npx skills add AgentPMT/agent-skills --skill what-is-agentpmt
npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup
npx skills add AgentPMT/agent-skills --skill agentpmt-no-account-agentaddress-x402
```

MCP call shape after the main AgentPMT MCP server is connected:

```json
{
  "method": "tools/call",
  "params": {
    "name": "Minecraft-Custom-Mod-Builder",
    "arguments": {
      "action": "create_mod_project",
      "advanced_resources": [
        {}
      ],
      "allow_experimental_bedrock_features": true,
      "assets": {},
      "build_jar": true,
      "compatibility_mode": "strict",
      "description": "example description",
      "features": {},
      "fidelity_policy": "preserve_intent"
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "minecraft-custom-mod-builder",
  "parameters": {
    "action": "create_mod_project",
    "advanced_resources": [
      {}
    ],
    "allow_experimental_bedrock_features": true,
    "assets": {},
    "build_jar": true,
    "compatibility_mode": "strict",
    "description": "example description",
    "features": {},
    "fidelity_policy": "preserve_intent"
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `create_mod_project` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- No-account AgentAddress/x402 setup: ../agentpmt-no-account-agentaddress-x402 (ClawHub: `agentpmt-no-account-agentaddress-x402`, page: https://clawhub.ai/agentpmt/agentpmt-no-account-agentaddress-x402; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-no-account-agentaddress-x402`)
- Marketplace product: https://www.agentpmt.com/marketplace/minecraft-custom-mod-builder
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
