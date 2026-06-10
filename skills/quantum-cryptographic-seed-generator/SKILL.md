---
name: quantum-cryptographic-seed-generator
description: "Quantum Cryptographic Seed Generator: Generate cryptographic seeds, UUIDs, tokens, passwords, and prime numbers using quantum-derived randomness with verification certificates. Use when an agent needs quantum cryptographic seed generator, key derivation and encryption seed generation, session tokens and api key creation, secure password generation, unique identifier production for databases and distributed systems, password, source, length through AgentPMT-hosted remote tool calls."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/quantum-cryptographic-seed-generator
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/quantum-cryptographic-seed-generator"}}
---
# Quantum Cryptographic Seed Generator

## Freshness
Last updated: `2026-06-10`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Cryptographic primitives and secure random generation powered by quantum or pseudo-random sources. Generate cryptographically secure seeds, UUIDs, tokens, passwords, and prime numbers using quantum-derived randomness for enhanced unpredictability or standard cryptographic randomness as a fallback. Supports verification certificates for audit trails and configurable parameters for bit length, character sets, and output formats.

## Product Instructions
### Quantum Cryptographic Seed Generator

#### Overview
Generate cryptographically secure seeds, UUIDs, tokens, passwords, and prime numbers using quantum or standard random sources. All operations support both quantum-derived randomness and standard cryptographic randomness.

#### Actions

##### seed — Generate Cryptographic Seed
Generates a random seed with an optional timestamp certificate for verification.

**Required fields:**
- `operation`: `"seed"`

**Optional fields:**
- `source`: `"quantum"` (default) or `"standard"` — random source
- `bit_length`: Integer 128–2048 (default 256) — seed size in bits
- `include_certificate`: Boolean (default true) — include a SHA-256 hash certificate with timestamp

**Example:**
```json
{
  "operation": "seed",
  "bit_length": 512,
  "include_certificate": true
}
```

---

##### uuid — Generate UUIDs
Generates one or more version-4 UUIDs.

**Required fields:**
- `operation`: `"uuid"`

**Optional fields:**
- `source`: `"quantum"` or `"standard"` (default `"quantum"`)
- `count`: Integer 1–1000 (default 1) — number of UUIDs to generate

**Example:**
```json
{
  "operation": "uuid",
  "count": 5,
  "source": "quantum"
}
```

---

##### token — Generate Secure Token
Generates a random token string in a specified character set.

**Required fields:**
- `operation`: `"token"`

**Optional fields:**
- `source`: `"quantum"` or `"standard"` (default `"quantum"`)
- `length`: Integer 8–256 (default 32) — token length in characters
- `charset`: `"alphanumeric"` (default), `"hex"`, `"base64"`, or `"ascii"`

**Example — hex API key:**
```json
{
  "operation": "token",
  "length": 64,
  "charset": "hex"
}
```

**Example — base64 token:**
```json
{
  "operation": "token",
  "length": 44,
  "charset": "base64"
}
```

---

##### password — Generate Secure Password
Generates a random password with configurable character classes.

**Required fields:**
- `operation`: `"password"`

**Optional fields:**
- `source`: `"quantum"` or `"standard"` (default `"quantum"`)
- `length`: Integer 8–256 (default 32) — password length
- `uppercase`: Boolean (default true) — include uppercase letters
- `lowercase`: Boolean (default true) — include lowercase letters
- `digits`: Boolean (default true) — include digits
- `symbols`: Boolean (default true) — include punctuation symbols
- `exclude_ambiguous`: Boolean (default true) — exclude visually ambiguous characters (0, O, 1, l, I)

**Example:**
```json
{
  "operation": "password",
  "length": 20,
  "symbols": false,
  "exclude_ambiguous": true
}
```

---

##### prime — Generate Prime Numbers
Generates one or more prime numbers of a specified bit length using Miller-Rabin primality testing.

**Required fields:**
- `operation`: `"prime"`

**Optional fields:**
- `source`: `"quantum"` or `"standard"` (default `"quantum"`)
- `bit_length`: Integer 128–2048 (default 256) — bit length of each prime
- `count`: Integer 1–1000 (default 1) — number of primes to generate

**Quantum source limit:** When using `"quantum"` source, `bit_length * count` must not exceed 1900.

**Example:**
```json
{
  "operation": "prime",
  "bit_length": 256,
  "count": 3
}
```

---

##### prime_pair — Generate RSA Prime Pair
Generates two distinct prime numbers suitable for RSA key generation, along with their product (n = p * q).

**Required fields:**
- `operation`: `"prime_pair"`

**Optional fields:**
- `source`: `"quantum"` or `"standard"` (default `"quantum"`)
- `bit_length`: Integer 128–2048 (default 256) — bit length of each prime
- `min_difference`: Integer, minimum 0 (default 100) — minimum numeric difference between the two primes

**Quantum source limit:** When using `"quantum"` source, `bit_length` must not exceed 950 (since two primes are generated).

**Example:**
```json
{
  "operation": "prime_pair",
  "bit_length": 512,
  "min_difference": 1000
}
```

---

#### Common Workflows

##### Generate a secure API key
```json
{
  "operation": "token",
  "length": 64,
  "charset": "hex",
  "source": "quantum"
}
```

##### Generate a user-friendly password
```json
{
  "operation": "password",
  "length": 16,
  "symbols": false,
  "exclude_ambiguous": true
}
```

##### Generate a certified seed for auditable randomness
```json
{
  "operation": "seed",
  "bit_length": 256,
  "include_certificate": true,
  "source": "quantum"
}
```

##### Generate an RSA key pair foundation
```json
{
  "operation": "prime_pair",
  "bit_length": 512,
  "source": "quantum"
}
```

##### Generate batch UUIDs for record identifiers
```json
{
  "operation": "uuid",
  "count": 100
}
```

#### Important Notes
- **Quantum vs Standard:** The `"quantum"` source uses hardware-derived quantum randomness. The `"standard"` source uses Python's `secrets` module (cryptographically secure but not quantum-derived). Default is `"quantum"` for all operations.
- **Quantum limits for primes:** When using quantum source, total bits requested for prime generation are capped (bit_length * count ≤ 1900 for `prime`; bit_length ≤ 950 for `prime_pair`).
- **At least one character class required:** For password generation, at least one of uppercase, lowercase, digits, or symbols must be enabled.
- **Seed certificates** include a UTC timestamp, the random source used, and a SHA-256 hash of the seed for independent verification.

## When To Use
- Use this skill for `Quantum Cryptographic Seed Generator` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: quantum cryptographic seed generator, key derivation and encryption seed generation, session tokens and api key creation, secure password generation, unique identifier production for databases and distributed systems, password, source, length.
- Supported action names: `password`, `prime`, `prime_pair`, `seed`, `token`, `uuid`.

## Use Cases
- Key derivation and encryption seed generation
- session tokens and API key creation
- secure password generation
- unique identifier production for databases and distributed systems
- RSA prime pair generation for public/private key creation
- cryptographic research and entropy analysis
- auditable randomness with timestamped certificates.

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `6`.
x402 availability: not enabled for this product.

- `password` (action slug: `password`): Generate a secure random password with configurable character classes and ambiguity settings. Price: `5` credits. Parameters: `digits`, `exclude_ambiguous`, `length`, `lowercase`, `source`, `symbols`, `uppercase`.
- `prime` (action slug: `prime`): Generate one or more prime numbers of a specified bit length using Miller-Rabin primality testing. Price: `5` credits. Parameters: `bit_length`, `count`, `source`.
- `prime_pair` (action slug: `prime-pair`): Generate two distinct prime numbers suitable for RSA key generation, along with their product (n = p * q). Price: `5` credits. Parameters: `bit_length`, `min_difference`, `source`.
- `seed` (action slug: `seed`): Generate a cryptographic seed with an optional timestamp certificate for verification. Supports quantum or standard random sources. Price: `5` credits. Parameters: `bit_length`, `include_certificate`, `source`.
- `token` (action slug: `token`): Generate a random token string in a specified character set. Suitable for API keys, session tokens, and nonces. Price: `5` credits. Parameters: `charset`, `length`, `source`.
- `uuid` (action slug: `uuid`): Generate one or more version-4 UUIDs using quantum or standard randomness. Price: `5` credits. Parameters: `count`, `source`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "quantum-cryptographic-seed-generator"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "quantum-cryptographic-seed-generator"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "quantum-cryptographic-seed-generator"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "quantum-cryptographic-seed-generator"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "quantum-cryptographic-seed-generator"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "quantum-cryptographic-seed-generator"
  }
}
```

## Call This Tool
Product slug: `quantum-cryptographic-seed-generator`

Marketplace page: https://www.agentpmt.com/marketplace/quantum-cryptographic-seed-generator

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
    "name": "Quantum-Cryptographic-Seed-Generator",
    "arguments": {
      "action": "password",
      "digits": true,
      "exclude_ambiguous": true,
      "length": 32,
      "lowercase": true,
      "source": "quantum",
      "symbols": true,
      "uppercase": true
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "quantum-cryptographic-seed-generator",
  "parameters": {
    "action": "password",
    "digits": true,
    "exclude_ambiguous": true,
    "length": 32,
    "lowercase": true,
    "source": "quantum",
    "symbols": true,
    "uppercase": true
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `password` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/quantum-cryptographic-seed-generator
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
