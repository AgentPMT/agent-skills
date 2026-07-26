---
name: agent-payment
description: "Compatibility pointer for AgentPMT payment setup. Use this when an older workflow or agent asks for agent-payment; it routes agents to the current account setup and no-account AgentAddress/x402 setup skills without duplicating payment implementation details."
version: 1.0.3
homepage: https://www.agentpmt.com/external-agent-api
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/external-agent-api"}}
---

# Agent Payment

## Freshness

Last updated: `2026-06-11`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

This is a compatibility landing skill. The current AgentPMT payment and setup instructions live in the canonical setup skills below.

## Choose The Current Setup Skill

- Use `../agentpmt-account-mcp-rest-api-setup` when the agent has an AgentPMT account, API key, budget key, Agent Group, or MCP server connection.
- Use `../agentpmt-no-account-agentaddress-x402` when the agent needs no-account AgentAddress wallet setup, direct x402 credit funding, or wallet-signed external API access.
- Use `../what-is-agentpmt` when the agent needs the marketplace, credits, workflows, Agent Groups, MCP, REST, AgentAddress, or x402 concepts before setup.

## Install Current Setup Skills

```bash
npx skills add AgentPMT/agent-skills --skill what-is-agentpmt
npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup
npx skills add AgentPMT/agent-skills --skill agentpmt-no-account-agentaddress-x402
```

OpenClaw:

```bash
openclaw skills install what-is-agentpmt
openclaw skills install agentpmt-account-mcp-rest-api-setup
openclaw skills install agentpmt-no-account-agentaddress-x402
```

## Canonical Links

- AgentPMT overview: https://clawhub.ai/agentpmt/what-is-agentpmt
- Account MCP/REST setup: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup
- No-account AgentAddress/x402 setup: https://clawhub.ai/agentpmt/agentpmt-no-account-agentaddress-x402
- AgentPMT marketplace: https://www.agentpmt.com

## Rule For Generated Skills

Generated product and workflow skills should link to the setup skills above. They should not copy wallet creation, payment, signature, balance-check, canonicalization, or retry procedures into each generated skill.
