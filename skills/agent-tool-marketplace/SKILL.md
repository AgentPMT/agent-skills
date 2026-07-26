---
name: agent-tool-marketplace
description: "AgentPMT tool marketplace guide for discovering tools, selecting actions, reading schemas, and invoking products through the current account or no-account setup skills. Use when an agent needs marketplace discovery and product-specific invocation identity without stale payment instructions."
version: 1.0.3
homepage: https://www.agentpmt.com/external-agent-api
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/external-agent-api"}}
---

# Agent Tool Marketplace

## Freshness

Last updated: `2026-06-11`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

Use this skill when an agent needs to discover AgentPMT tools, inspect schemas and prices, choose the right product/action, and route invocation through the current setup skill.

## Required Setup

- Account route: use `../agentpmt-account-mcp-rest-api-setup` for AgentPMT account, MCP server, REST API, Agent Group, API key, and budget key setup.
- No-account route: use `../agentpmt-no-account-agentaddress-x402` for AgentAddress wallet, x402 funding, wallet-signed external API access, and payment troubleshooting.
- Overview: use `../what-is-agentpmt` for marketplace, credits, workflows, Agent Groups, MCP, REST, AgentAddress, and x402 concepts.

Install the current setup skills:

```bash
npx skills add AgentPMT/agent-skills --skill what-is-agentpmt
npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup
npx skills add AgentPMT/agent-skills --skill agentpmt-no-account-agentaddress-x402
```

## Discover Tools

Use the AgentPMT marketplace or the authenticated Tool Search skill to find products by name, category, use case, action, schema fields, and pricing.

- Marketplace: https://www.agentpmt.com/marketplace
- Tool search skill: `../agentpmt-tool-search-and-execution`
- Tool search ClawHub page: https://clawhub.ai/agentpmt/agentpmt-tool-search-and-execution

Catalog entries identify the product slug, available actions, action schemas, pricing, availability, and setup route. Choose the product whose schema and price match the task.

## Invoke A Product

1. Identify the product slug and action slug from the marketplace, generated product skill, or live schema.
2. Read the adjacent product skill for product-specific behavior, schema details, sample parameters, response handling, and marketplace URL.
3. Use `../agentpmt-account-mcp-rest-api-setup` for account MCP/REST calls, or `../agentpmt-no-account-agentaddress-x402` for no-account external calls.
4. Keep product-specific parameters aligned with the live schema. If the schema is unclear, fetch live instructions before invoking.
5. Treat returned JSON as the source of truth. If validation fails, correct parameters from the schema before retrying.

## Product Skill Links

Generated product skills live under `skills/<product-skill-slug>` in `AgentPMT/agent-skills` and under the AgentPMT ClawHub account:

```bash
npx skills add AgentPMT/agent-skills --skill <product-skill-slug>
openclaw skills install <product-skill-slug>
```

ClawHub URL pattern:

```text
https://clawhub.ai/agentpmt/<product-skill-slug>
```

## Error Handling

- Product schema error: rebuild parameters from the product skill or live schema.
- Authentication or setup error: return to the account setup skill or no-account setup skill, depending on the route.
- Insufficient credits or payment setup error: use `../agentpmt-no-account-agentaddress-x402`.
- Tool or platform error: preserve product slug, action slug, request identifiers, response body, and retry only after the setup or schema issue is fixed.

## Canonical Links

- AgentPMT overview: https://clawhub.ai/agentpmt/what-is-agentpmt
- Account MCP/REST setup: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup
- No-account AgentAddress/x402 setup: https://clawhub.ai/agentpmt/agentpmt-no-account-agentaddress-x402
- AgentPMT marketplace: https://www.agentpmt.com/marketplace

## Maintenance Rule

This marketplace skill describes discovery and routing only. Do not add wallet creation, payment challenge, signature, balance-check, canonicalization, or retry procedures here; update the canonical no-account setup skill instead.
