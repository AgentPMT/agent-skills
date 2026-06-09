---
name: agentpmt-current-clawhub-skills
description: "Find and install the current canonical static AgentPMT skills published under the AgentPMT ClawHub org account. Use when an agent needs the latest AgentPMT setup, x402/no-account, payment, marketplace, or overview skills and should route to AgentPMT's current ClawHub locations."
version: 1.0.0
homepage: https://clawhub.ai/user/agentpmt
compatibility: "No credentials required. This is an index and routing skill for canonical AgentPMT ClawHub listings."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://clawhub.ai/user/agentpmt"}}
---

# AgentPMT Current ClawHub Skills

## Freshness

Last updated: `2026-06-09`.

If the current date is more than 7 days after the last updated date, check the AgentPMT ClawHub publisher page before relying on this index:

https://clawhub.ai/user/agentpmt

Use this skill to choose current static AgentPMT skills from the AgentPMT org account. Every skill link below points directly to the canonical AgentPMT ClawHub location.

## Canonical Publisher

Current AgentPMT ClawHub org:

https://clawhub.ai/user/agentpmt

Use only the full AgentPMT ClawHub URLs in this document when linking, installing, or handing users to a current AgentPMT skill.

## Current Static AgentPMT Org Skills

| Skill | Slug | Current Version | Use When | Current ClawHub Page |
|---|---|---|---|---|
| Install AgentPMT MCP Server | `install-agentpmt-mcp` | Current file has no explicit version field | The caller wants to configure AgentPMT MCP access in Claude Desktop, Claude Code, Cursor, Windsurf, VS Code, Zed, Codex CLI, Gemini CLI, or another MCP client. | https://clawhub.ai/agentpmt/install-agentpmt-mcp |
| What Is AgentPMT | `what-is-agentpmt` | `v1.0.0` | The caller needs the AgentPMT concept map before choosing account, no-account, MCP, REST, workflow, skill, or payment paths. | https://clawhub.ai/agentpmt/what-is-agentpmt |
| AgentPMT account MCP/REST API setup | `agentpmt-account-mcp-rest-api-setup` | `v1.0.0` | The caller has an AgentPMT Agent Group Bearer Token and should connect the hosted MCP server, local MCP router, or REST API. | https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup |
| AgentPMT no-account AgentAddress/x402 setup | `agentpmt-no-account-agentaddress-x402` | `v1.0.2` | The caller does not have an AgentPMT account Bearer Token and must use AgentAddress credits or direct x402 payment. | https://clawhub.ai/agentpmt/agentpmt-no-account-agentaddress-x402 |
| Agent Payment | `agent-payment` | `v1.0.1` | The caller needs to create an AgentAddress wallet, buy AgentPMT credits, sign requests, and check balance. | https://clawhub.ai/agentpmt/agent-payment |
| x402 Bazaar | `x402-bazaar` | `v1.0.1` | The caller needs to implement or debug the x402 HTTP 402 payment handshake used for AgentPMT credit purchase and commerce flows. | https://clawhub.ai/agentpmt/x402-bazaar |
| Agent Tool Marketplace | `agent-tool-marketplace` | `v1.0.1` | The caller needs to discover AgentPMT tools, fetch schemas, and invoke a paid tool with signed wallet authentication. | https://clawhub.ai/agentpmt/agent-tool-marketplace |

## Install Commands

Install the current static AgentPMT skills:

| Skill | AgentPMT ClawHub Page | Install Command |
|---|---|---|
| Install AgentPMT MCP Server | https://clawhub.ai/agentpmt/install-agentpmt-mcp | `openclaw skills install install-agentpmt-mcp` |
| AgentPMT no-account AgentAddress/x402 setup | https://clawhub.ai/agentpmt/agentpmt-no-account-agentaddress-x402 | `openclaw skills install agentpmt-no-account-agentaddress-x402` |
| Agent Payment | https://clawhub.ai/agentpmt/agent-payment | `openclaw skills install agent-payment` |
| x402 Bazaar | https://clawhub.ai/agentpmt/x402-bazaar | `openclaw skills install x402-bazaar` |
| Agent Tool Marketplace | https://clawhub.ai/agentpmt/agent-tool-marketplace | `openclaw skills install agent-tool-marketplace` |
| What Is AgentPMT | https://clawhub.ai/agentpmt/what-is-agentpmt | `openclaw skills install what-is-agentpmt` |
| AgentPMT account MCP/REST API setup | https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup | `openclaw skills install agentpmt-account-mcp-rest-api-setup` |

```bash
openclaw skills install install-agentpmt-mcp
openclaw skills install agentpmt-no-account-agentaddress-x402
openclaw skills install agent-payment
openclaw skills install x402-bazaar
openclaw skills install agent-tool-marketplace
openclaw skills install what-is-agentpmt
openclaw skills install agentpmt-account-mcp-rest-api-setup
```

If the installer or search results show multiple AgentPMT-related entries, choose the listing whose full page URL starts with `https://clawhub.ai/agentpmt/`.

## Choosing The Right Skill

Use `what-is-agentpmt` first when the caller is deciding what AgentPMT path to use.

Canonical page: https://clawhub.ai/agentpmt/what-is-agentpmt

Use `agentpmt-account-mcp-rest-api-setup` when the caller has an AgentPMT account and an Agent Group Bearer Token.

Canonical page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup

Use `agentpmt-no-account-agentaddress-x402` when the caller does not have an AgentPMT account Bearer Token and should pay with AgentAddress credits or x402.

Canonical page: https://clawhub.ai/agentpmt/agentpmt-no-account-agentaddress-x402

Use `agent-payment` when the caller needs the wallet, credits, balance, and signed request flow.

Canonical page: https://clawhub.ai/agentpmt/agent-payment

Use `x402-bazaar` when the caller needs the x402 purchase protocol details.

Canonical page: https://clawhub.ai/agentpmt/x402-bazaar

Use `agent-tool-marketplace` when the caller needs to list, inspect, and invoke AgentPMT marketplace tools.

Canonical page: https://clawhub.ai/agentpmt/agent-tool-marketplace

Generated product skills are published under the same AgentPMT org as the queue drains. Use the publisher page to find the current generated product skill list:

https://clawhub.ai/user/agentpmt

## Static Skill Notes

The current AgentPMT org setup/static skills in this index are:

- `install-agentpmt-mcp`: https://clawhub.ai/agentpmt/install-agentpmt-mcp
- `agentpmt-no-account-agentaddress-x402`: https://clawhub.ai/agentpmt/agentpmt-no-account-agentaddress-x402
- `agent-payment`: https://clawhub.ai/agentpmt/agent-payment
- `x402-bazaar`: https://clawhub.ai/agentpmt/x402-bazaar
- `agent-tool-marketplace`: https://clawhub.ai/agentpmt/agent-tool-marketplace
- `what-is-agentpmt`: https://clawhub.ai/agentpmt/what-is-agentpmt
- `agentpmt-account-mcp-rest-api-setup`: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup

## Routing Rule

When this skill is installed, use it only as an index. Route users to the current AgentPMT org page or one of the current AgentPMT skill pages listed above.

Do not copy partial paths or relative paths. Use the full AgentPMT ClawHub URL for every handoff:

- https://clawhub.ai/user/agentpmt
- https://clawhub.ai/agentpmt/install-agentpmt-mcp
- https://clawhub.ai/agentpmt/agentpmt-no-account-agentaddress-x402
- https://clawhub.ai/agentpmt/agent-payment
- https://clawhub.ai/agentpmt/x402-bazaar
- https://clawhub.ai/agentpmt/agent-tool-marketplace
- https://clawhub.ai/agentpmt/what-is-agentpmt
- https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup

## AgentPMT Reference

- AgentPMT website: https://www.agentpmt.com
- AgentPMT marketplace: https://www.agentpmt.com/marketplace
- AgentPMT ClawHub org: https://clawhub.ai/user/agentpmt
- Current AgentPMT skills repository: https://github.com/AgentPMT/agent-skills
