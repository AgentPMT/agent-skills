# Agent Skills

**Production-ready workflow skills for Claude, Codex, and local AI models.**

Build, publish, and run complex business automations from a single prompt. This repository is the official collection of agent skills for [AgentPMT](https://www.agentpmt.com) -- the platform that gives AI agents real tools, real budgets, and real payments.

---

## What is AgentPMT?

AgentPMT is an agentic commerce platform where AI agents discover, purchase, and use tools autonomously. It connects three things that agents need to operate in the real world:

1. **A marketplace of tools** -- APIs, data sources, AI models, connectors, and services that agents can call on demand.
2. **A budget system** -- Spending controls, approved vendors, and credit-based payments so agents operate within defined limits.
3. **A dynamic MCP server** -- One endpoint that assembles exactly the right tools for each agent session based on its budget and permissions.

Instead of hardcoding tool integrations, you give your agent a budget, point it at AgentPMT's MCP server, and it figures out what tools are available, what they cost, and how to use them.

---

## The Workflow Builder

The workflow builder is a visual, no-code interface for creating agent automation sequences called **skills**. Skills chain together multiple tools, decision logic, and processing steps into executable workflows that any AI agent can run.

### What you can build

Skills are composed of six node types that you drag, drop, and connect:

| Node | Purpose |
|------|---------|
| **Tool** | Call any product from the marketplace -- web search, image generation, code execution, APIs, anything listed |
| **Prompt** | Give the agent inline instructions in freeform text or structured format (goal, inputs, outputs, constraints) |
| **Branch** | Split the workflow into conditional paths -- up to 8 parallel options based on agent reasoning |
| **Merge** | Rejoin parallel paths back into a single flow after branching |
| **For Each** | Loop over a collection of items, executing child nodes once per item |
| **Notify Human** | Pause the workflow and request human intervention before continuing |

### From prompt to production

You don't need to understand graph theory to build a workflow. Describe what you want in plain language, and the builder generates the node structure for you. From there, you can refine the flow visually -- reorder steps, add branches, swap tools, adjust prompts -- and publish it to the marketplace when it's ready.

Every published skill gets:
- A unique URL and slug for sharing
- Version tracking with frozen snapshots at each publish
- Export to **MCP server definition** or **REST API specification**
- Remix support so others can fork and improve your work
- Usage tracking and creator payments when others run your skill

### Real workflow patterns

**Research and report generation**
```
Web Search --> Extract Key Findings --> Generate Report --> Format as PDF
```

**Conditional processing with human oversight**
```
Analyze Input --> Branch (high risk / low risk)
  High risk --> Notify Human for Approval --> Process
  Low risk --> Auto-Process
Merge --> Deliver Result
```

**Batch operations with iteration**
```
Fetch Customer List --> For Each Customer:
  Look Up Account --> Check Status --> Branch (active / churned)
    Active --> Send Renewal Offer
    Churned --> Send Win-Back Email
  Merge
```

**Multi-tool orchestration**
```
Scrape Competitor Pricing --> Analyze with AI Model --> Generate Pricing Recommendations --> Post to Slack --> Log to Database
```

---

## The Dynamic MCP System

AgentPMT runs a dynamic [Model Context Protocol](https://modelcontextprotocol.io/) server that assembles tool availability in real time based on budget permissions.

### How it works

```
Your Agent                          AgentPMT MCP Server
   |                                       |
   |-- initialize (credentials) ---------->|
   |                                       |-- Validate budget
   |                                       |-- Load approved products
   |                                       |-- Fetch external MCP tools
   |                                       |-- Build unified tool list
   |<-- tool catalog with pricing ---------|
   |                                       |
   |-- tools/call ("web-search", args) --->|
   |                                       |-- Verify authorization
   |                                       |-- Deduct credits
   |                                       |-- Execute tool
   |<-- result ----------------------------|
```

One MCP endpoint serves every tool your agent is authorized to use. The tool list is not static -- it changes based on:

- **Budget approvals** -- Only tools and vendors you've approved appear in the catalog
- **Product availability** -- Tools can go up or down; the server reflects real-time status
- **External MCP servers** -- Third-party MCP servers are transparently integrated as normal tools
- **Workflow builder access** -- Budgets can enable or disable the ability to create new workflows
- **Dynamic configuration** -- Change approvals and the tool list updates on the next `tools/list` call

### What agents see

Every tool in the catalog includes metadata that helps agents make informed decisions:

```json
{
  "name": "ai-image-generator",
  "description": "Generate images from text prompts",
  "inputSchema": { ... },
  "x-pricing": {
    "price_per_unit": 50,
    "unit_type": "per_call",
    "currency": "credits"
  },
  "x-availability": {
    "status": "available"
  }
}
```

Agents know the cost before they call. Budget limits are enforced server-side. No surprise charges, no runaway spending.

### Connect any agent

The MCP server works with any agent that speaks the Model Context Protocol:

```
MCP Endpoint: https://api.agentpmt.com/mcp
Auth: Bearer base64(api_key:budget_key)
```

Claude Desktop, Claude Code, OpenAI agents, LangChain, AutoGPT, custom agents -- if it can make MCP calls, it works with AgentPMT.

---

## Create Complex Business Flows from Prompts

The power of AgentPMT is that you don't need to be a developer to build agent automations. The platform turns natural language descriptions into executable workflows.

### The process

1. **Describe your workflow** -- Tell the builder what you want to accomplish in plain language
2. **Review the generated flow** -- The builder creates a node graph you can inspect and modify
3. **Customize and refine** -- Swap tools, adjust prompts, add branches, set conditions
4. **Test with real tools** -- Every tool call uses actual APIs with real results
5. **Publish and share** -- Make it public for others to use, or keep it private for your team

### What makes this different

**Real tools, not mocks.** Every tool node calls an actual product from the marketplace. No simulations, no placeholder responses.

**Budget-controlled execution.** Workflows run within defined spending limits. Set a cap, and the agent stops when it's reached.

**Remix and improve.** Published workflows can be forked by anyone. The original creator earns credits when remixes are used. This creates a flywheel where the best workflows get refined by the community.

**Live execution tracking.** Watch your agent work through a workflow in real time with step-by-step progress, cost tracking, and session management.

**Exportable.** Every published workflow can be exported as an MCP server definition or REST API spec. Take your automation anywhere.

---

## What's in This Repository

This repo contains ready-to-use agent skills organized by use case. Each skill includes:

- A description of what it does and when to use it
- The workflow structure (nodes, edges, and configuration)
- Required tools and estimated credit cost
- Setup instructions for running it with your agent

### Skill categories

| Category | Examples |
|----------|----------|
| **Research & Analysis** | Competitive analysis, market research, literature reviews |
| **Content & Marketing** | Blog generation, social media scheduling, SEO audits |
| **Data Processing** | ETL pipelines, data enrichment, report generation |
| **Customer Operations** | Support ticket routing, onboarding sequences, churn analysis |
| **Development & DevOps** | Code review workflows, deployment pipelines, monitoring alerts |
| **Finance & Accounting** | Invoice processing, expense categorization, reconciliation |
| **Sales & Outreach** | Lead qualification, proposal generation, follow-up sequences |

---

## Getting Started

### 1. Create an AgentPMT account

Sign up at [agentpmt.com](https://www.agentpmt.com) and create your first budget.

### 2. Set up your agent

Add the AgentPMT MCP server to your agent's configuration:

**Claude Desktop / Claude Code**
```json
{
  "mcpServers": {
    "agentpmt": {
      "url": "https://api.agentpmt.com/mcp",
      "headers": {
        "Authorization": "Bearer <your-base64-credentials>"
      }
    }
  }
}
```

Your credentials are `base64(api_key:budget_key)` -- both available from the budget settings page in your dashboard.

### 3. Browse and import skills

Explore the skills in this repository or on the [AgentPMT marketplace](https://www.agentpmt.com/agent-workflow-skills). Import a skill into your account, approve the required tools in your budget, and let your agent run it.

### 4. Build your own

Open the [workflow builder](https://www.agentpmt.com/agent-workflow-skills-builder), describe what you want, and start building. Publish it to the marketplace when it's ready, or keep it private for your own use.

---

## Contributing

We welcome skill contributions from the community. If you've built a workflow that solves a real problem, submit a pull request.

**Guidelines:**
- Include a clear description of what the skill does and who it's for
- List all required tools and their approximate credit cost
- Test the workflow end-to-end before submitting
- Keep skills focused -- one skill, one job

---

## Links

- [AgentPMT Platform](https://www.agentpmt.com)
- [Marketplace](https://www.agentpmt.com/agent-workflow-skills)
- [Workflow Builder](https://www.agentpmt.com/agent-workflow-skills-builder)
- [Documentation](https://www.agentpmt.com/dynamic-mcp)

---

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, including commercial, as long as you provide appropriate credit.
