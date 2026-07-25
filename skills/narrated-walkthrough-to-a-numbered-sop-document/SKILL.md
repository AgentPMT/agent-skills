---
name: narrated-walkthrough-to-a-numbered-sop-document
description: "Narrated Walkthrough to a Numbered SOP Document: Turns talking through a job out loud into a written, numbered standard operating procedure. Built for the people who actually know the equipment and have no time to write documentation: maintenance and facilities teams, field service, manufacturing, labs, franchise operations, and any owner trying to get a process out of their own head before handing it over. Walk the machine or the task and narrate it, saying the step number out loud as you go."
version: 1.0.0
homepage: https://www.agentpmt.com/agent-workflow-skills/narrated-walkthrough-to-a-numbered-sop-document
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/agent-workflow-skills/narrated-walkthrough-to-a-numbered-sop-document"}}
---
# Narrated Walkthrough to a Numbered SOP Document

## Freshness
Last updated: `2026-07-25`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Workflow Does
Turns talking through a job out loud into a written, numbered standard operating procedure. Built for the people who actually know the equipment and have no time to write documentation: maintenance and facilities teams, field service, manufacturing, labs, franchise operations, and any owner trying to get a process out of their own head before handing it over. Walk the machine or the task and narrate it, saying the step number out loud as you go, and the workflow pulls the transcript of each new Plaud recording and turns it into a clean procedure document: a title, the equipment or process it covers, tools and safety notes gathered into their own sections, then numbered steps in the order you said them, with your asides and warnings kept attached to the step they belong to. Filler, false starts and interruptions are dropped; the technical content is left in your words rather than rewritten into corporate documentation voice. It lands as a Google Doc so it stays editable and exports to PDF or Word, and anything the narration left ambiguous is flagged at the end for you to fill in rather than being invented. Say each step number aloud and the transcript carries its own index, which makes pairing photos to steps afterwards mechanical instead of guesswork.

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
{"action":"start_workflow","skill_id":"narrated-walkthrough-to-a-numbered-sop-document"}
```

```json
{"action":"end_workflow","skill_id":"narrated-walkthrough-to-a-numbered-sop-document","rating":5,"comment":"completed"}
```

## Workflow Process
1. List Plaud Recordings
   - Tool product: Plaud.
   - Tool skill: `../plaud`.
   - ClawHub page: https://clawhub.ai/agentpmt/plaud.
   - skills.sh install: `npx skills add AgentPMT/agent-skills --skill plaud`.
   - Marketplace: https://www.agentpmt.com/marketplace/plaud.
   - Tool instructions: List the user's recordings and carry forward only those not already in the processed log. A scheduled run then picks up each new walkthrough once.
2. Each New Walkthrough
   - Iterate over the configured collection, then continue through the connected workflow path.
3. Fetch Transcript
   - Tool product: Plaud.
   - Tool skill: `../plaud`.
   - ClawHub page: https://clawhub.ai/agentpmt/plaud.
   - skills.sh install: `npx skills add AgentPMT/agent-skills --skill plaud`.
   - Marketplace: https://www.agentpmt.com/marketplace/plaud.
   - Tool instructions: Fetch the full transcript for this recording, reusing Plaud's existing transcript when one exists.
4. Summarize the Run
   - Prompt: Tell the user which procedures were written and which ones still need a human.
5. Structure Into a Procedure
   - Prompt: Turn a spoken walkthrough into an ordered, numbered standard operating procedure.
6. Write the SOP Document
   - Tool product: Google Docs Connector.
   - Tool skill: `../google-docs-connector`.
   - ClawHub page: https://clawhub.ai/agentpmt/google-docs-connector.
   - skills.sh install: `npx skills add AgentPMT/agent-skills --skill google-docs-connector`.
   - Marketplace: https://www.agentpmt.com/marketplace/google-docs-connector.
   - Tool instructions: Create a Google Doc for the procedure: title and process at the top, then tools and materials, then safety notes, then the numbered steps as a numbered list, and finally the ambiguities section headed as needing review. Leave the document editable so the user can drop photos beside the steps and export to PDF or Word.
7. Log the Run
   - Tool product: Google Sheets.
   - Tool skill: `../google-sheets`.
   - ClawHub page: https://clawhub.ai/agentpmt/google-sheets.
   - skills.sh install: `npx skills add AgentPMT/agent-skills --skill google-sheets`.
   - Marketplace: https://www.agentpmt.com/marketplace/google-sheets-api.
   - Tool instructions: Append the recording id, the procedure title, the doc link, the step count and the number of open ambiguities to the processed log, so nothing is documented twice and unfinished procedures are easy to find.

## Tool Skill Links
- Plaud: `../plaud`; ClawHub https://clawhub.ai/agentpmt/plaud; skills.sh `npx skills add AgentPMT/agent-skills --skill plaud`; marketplace https://www.agentpmt.com/marketplace/plaud
- Google Docs Connector: `../google-docs-connector`; ClawHub https://clawhub.ai/agentpmt/google-docs-connector; skills.sh `npx skills add AgentPMT/agent-skills --skill google-docs-connector`; marketplace https://www.agentpmt.com/marketplace/google-docs-connector
- Google Sheets: `../google-sheets`; ClawHub https://clawhub.ai/agentpmt/google-sheets; skills.sh `npx skills add AgentPMT/agent-skills --skill google-sheets`; marketplace https://www.agentpmt.com/marketplace/google-sheets-api

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Workflow page: https://www.agentpmt.com/agent-workflow-skills/narrated-walkthrough-to-a-numbered-sop-document
- AgentPMT workflows: https://www.agentpmt.com/agent-workflow-skills
