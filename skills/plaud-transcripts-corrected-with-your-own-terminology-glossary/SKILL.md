---
name: plaud-transcripts-corrected-with-your-own-terminology-glossary
description: "Plaud Transcripts Corrected With Your Own Terminology Glossary: Fixes the words your transcription keeps getting wrong, by giving the pipeline your vocabulary instead of hoping a bigger model guesses right. Every speech model mangles terms it has never seen: cell line and reagent names, drug and device names, case and matter numbers, part numbers, local spelling and number conventions, team and client names. Swapping to a different model does not fix this, because none of them have your terms e."
version: 1.0.0
homepage: https://www.agentpmt.com/agent-workflow-skills/plaud-transcripts-corrected-with-your-own-terminology-glossary
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/agent-workflow-skills/plaud-transcripts-corrected-with-your-own-terminology-glossary"}}
---
# Plaud Transcripts Corrected With Your Own Terminology Glossary

## Freshness
Last updated: `2026-07-25`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Workflow Does
Fixes the words your transcription keeps getting wrong, by giving the pipeline your vocabulary instead of hoping a bigger model guesses right. Every speech model mangles terms it has never seen: cell line and reagent names, drug and device names, case and matter numbers, part numbers, local spelling and number conventions, team and client names. Swapping to a different model does not fix this, because none of them have your terms either. Keep a plain Google Sheet glossary of the terms that matter, each with the spelling you want and the misfires it usually comes back as ("HEK293" for "heck two ninety three"), plus any formatting rules you need enforced, such as Swiss German ss instead of eszett or 1'000.00 number style. On each run the workflow reads the glossary, pulls the transcript of every new Plaud recording, applies the corrections to the transcript first, and only then writes the summary and action items from the corrected text, so your terminology is right everywhere downstream instead of only in the raw transcript. The corrected transcript and summary land in a Google Doc, and every correction made is listed so you can see what changed and keep tuning the glossary. Unknown terms are flagged, never silently normalized into something that looks plausible.

## Required Setup
- AgentPMT overview: `../what-is-agentpmt`.
- Account MCP/REST setup: `../agentpmt-account-mcp-rest-api-setup`.

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

## Workflow Session Management
Call `AgentPMT-Workflow-Skills` with `start_workflow` before the first step and `end_workflow` after the final step.

```json
{"action":"start_workflow","skill_id":"plaud-transcripts-corrected-with-your-own-terminology-glossary"}
```

```json
{"action":"end_workflow","skill_id":"plaud-transcripts-corrected-with-your-own-terminology-glossary","rating":5,"comment":"completed"}
```

## Workflow Process
1. Read Terminology Glossary
   - Tool product: Google Sheets.
   - Tool skill: `../google-sheets`.
   - ClawHub page: https://clawhub.ai/agentpmt/google-sheets.
   - skills.sh install: `npx skills add AgentPMT/agent-skills --skill google-sheets`.
   - Marketplace: https://www.agentpmt.com/marketplace/google-sheets-api.
   - Tool instructions: Read the glossary tab: each row carries the correct term, the misheard variants it usually comes back as, and optional notes. Also read any formatting rules rows (spelling conventions, number formats). This sheet is the single source of the user's vocabulary.
2. List Plaud Recordings
   - Tool product: Plaud.
   - Tool skill: `../plaud`.
   - ClawHub page: https://clawhub.ai/agentpmt/plaud.
   - skills.sh install: `npx skills add AgentPMT/agent-skills --skill plaud`.
   - Marketplace: https://www.agentpmt.com/marketplace/plaud.
   - Tool instructions: List the user's recordings and carry forward only those whose recording id is not already in the processed log, so the workflow is safe to schedule.
3. Each New Recording
   - Iterate over the configured collection, then continue through the connected workflow path.
4. Fetch Transcript
   - Tool product: Plaud.
   - Tool skill: `../plaud`.
   - ClawHub page: https://clawhub.ai/agentpmt/plaud.
   - skills.sh install: `npx skills add AgentPMT/agent-skills --skill plaud`.
   - Marketplace: https://www.agentpmt.com/marketplace/plaud.
   - Tool instructions: Fetch the full transcript for this recording, reusing Plaud's existing transcript when one exists.
5. Summarize the Run
   - Prompt: Report which recordings were corrected and which terms the glossary is still missing.
6. Apply Glossary to Transcript
   - Prompt: Correct the transcript against the user's glossary and formatting rules before any summary is produced.
7. Summarize From Corrected Text
   - Prompt: Produce the summary and action items from the corrected transcript so the user's terminology is right downstream, not just in the raw text.
8. Write Corrected Doc
   - Tool product: Google Docs Connector.
   - Tool skill: `../google-docs-connector`.
   - ClawHub page: https://clawhub.ai/agentpmt/google-docs-connector.
   - skills.sh install: `npx skills add AgentPMT/agent-skills --skill google-docs-connector`.
   - Marketplace: https://www.agentpmt.com/marketplace/google-docs-connector.
   - Tool instructions: Create a document for this recording containing the summary and action items, then the corrected transcript, then a corrections table listing each change and the glossary row behind it, and finally any unknown terms flagged for the user to add to the glossary.
9. Log the Run
   - Tool product: Google Sheets.
   - Tool skill: `../google-sheets`.
   - ClawHub page: https://clawhub.ai/agentpmt/google-sheets.
   - skills.sh install: `npx skills add AgentPMT/agent-skills --skill google-sheets`.
   - Marketplace: https://www.agentpmt.com/marketplace/google-sheets-api.
   - Tool instructions: Append the recording id, the doc link, the number of corrections applied, and any flagged unknown terms to the processed log so the recording is never handled twice and the glossary can be tuned over time.

## Tool Skill Links
- Google Sheets: `../google-sheets`; ClawHub https://clawhub.ai/agentpmt/google-sheets; skills.sh `npx skills add AgentPMT/agent-skills --skill google-sheets`; marketplace https://www.agentpmt.com/marketplace/google-sheets-api
- Plaud: `../plaud`; ClawHub https://clawhub.ai/agentpmt/plaud; skills.sh `npx skills add AgentPMT/agent-skills --skill plaud`; marketplace https://www.agentpmt.com/marketplace/plaud
- Google Docs Connector: `../google-docs-connector`; ClawHub https://clawhub.ai/agentpmt/google-docs-connector; skills.sh `npx skills add AgentPMT/agent-skills --skill google-docs-connector`; marketplace https://www.agentpmt.com/marketplace/google-docs-connector

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Workflow page: https://www.agentpmt.com/agent-workflow-skills/plaud-transcripts-corrected-with-your-own-terminology-glossary
- AgentPMT workflows: https://www.agentpmt.com/agent-workflow-skills
