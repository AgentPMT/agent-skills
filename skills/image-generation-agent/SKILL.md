---
name: image-generation-agent
description: "Image Generation Agent: Google Gemini-powered image generation tool (Nano Banana / Gemini 2.5 & 3 Flash Image). Use when an agent needs image generation agent, ai image generation, nano banana image creation, google gemini image api, text to image, generate budget image, prompt, aspect ratio through AgentPMT with either an account Bearer Token or the no-account AgentAddress/x402 flow. Discovery terms: image generation agent, ai image generation, nano banana image creation."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/image-generation-agent
compatibility: "Requires access to AgentPMT through either an AgentPMT account Bearer Token for MCP/REST calls, or the no-account AgentAddress/x402 flow. This product skill is tool-specific; use the linked AgentPMT setup skills for connection and payment setup."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/image-generation-agent"}}
---
# Image Generation Agent

## What This Tool Does
AI image generator powered by Google Gemini 3 Flash Image and  "Nano Banana". Create photorealistic product photography, marketing creative, social graphics, app icons, concept art, hero images, and brand assets from a single text prompt — or edit an existing image by passing up to four reference photos for style, subject, or scene guidance. Choose your output tier: a low-cost budget draft for ideation, or crisp 0.5K, 1K, 2K, and 4K final renders for print, ads, e-commerce, and presentation use. Supports 14 aspect ratios including 1:1, 16:9, 9:16, 21:9, 4:5, and ultra-wide 8:1 banner formats. Every generated image is auto-saved to AgentPMT File Manager with a 7-day signed download URL, file_id, width, height, MIME type, and size bytes — ready to drop into chat, hand off to another tool, or pull into a workflow. Built for designers, marketers, e-commerce sellers, content creators, and AI agents that need on-demand visuals without leaving the conversation.

## Product Instructions
### AI Image Creator

Create images from prompts, or edit an image by adding reference images. Generated images are saved to File Manager and returned with a signed URL that users can open or download directly, plus `file_id`, MIME type, size, width, and height.

#### Choosing an action

- `generate_budget_image`: Lower-cost drafts, previews, simple assets, or 1024px-class output.
- `generate_image_0_5k`: Small high-efficiency output.
- `generate_image_1k`: Standard final images.
- `generate_image_2k`: Higher-resolution social, presentation, or product assets.
- `generate_image_4k`: Highest-resolution final assets.

#### Inputs

- `prompt` is required for every generation action.
- `aspect_ratio` defaults to `1:1`.
- `reference_images` is optional and accepts up to 4 images.
- Reference image formats: PNG, JPEG, or WebP.
- Reference image sources:
  - `{"source_kind":"file_id","file_id":"<file-id>"}`
  - `{"source_kind":"url","url":"https://example.com/image.png"}`
  - `{"source_kind":"base64","base64_data":"<base64>","mime_type":"image/png"}`
- `filename` is optional. The final extension is inferred from the generated image.
- `expiration_days` defaults to 7 and must be from 1 to 7.
- Generated image bytes are not returned inline. Use the signed URL to open or download the file.

Only use reference images you have the right to use.

#### Aspect ratios

`generate_budget_image` supports:
`1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`.

High-resolution actions support:
`1:1`, `1:4`, `1:8`, `2:3`, `3:2`, `3:4`, `4:1`, `4:3`, `4:5`, `5:4`, `8:1`, `9:16`, `16:9`, `21:9`.

#### Examples

Budget text-to-image:

```json
{
  "action": "generate_budget_image",
  "prompt": "A clean blue circle icon on a white background, flat vector style",
  "aspect_ratio": "1:1"
}
```

High-resolution text-to-image:

```json
{
  "action": "generate_image_2k",
  "prompt": "A polished product mockup of a reusable water bottle on a white studio sweep",
  "aspect_ratio": "16:9",
  "filename": "water-bottle-product-mockup"
}
```

Reference-image edit from File Manager:

```json
{
  "action": "generate_image_1k",
  "prompt": "Keep the subject and pose. Replace the background with a bright minimalist studio scene.",
  "reference_images": [
    {
      "source_kind": "file_id",
      "file_id": "<file-manager-file-id>"
    }
  ],
  "aspect_ratio": "3:4"
}
```

#### Output

Successful calls return:

```json
{
  "success": true,
  "action": "generate_image_1k",
  "tier": "1k",
  "model_tier": "standard",
  "aspect_ratio": "1:1",
  "image_size": "1K",
  "reference_image_count": 0,
  "images": [
    {
      "file_id": "...",
      "filename": "...png",
      "signed_url": "https://...",
      "signed_url_expires_in": 604800,
      "content_type": "image/png",
      "size_bytes": 123456,
      "width": 1024,
      "height": 1024
    }
  ],
  "text_parts": [],
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "total_tokens": 0
  }
}
```

## When To Use
- Use this skill for `Image Generation Agent` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: image generation agent, ai image generation, nano banana image creation, google gemini image api, text to image, generate budget image, prompt, aspect ratio.
- Supported action names: `generate_budget_image`, `generate_image_0_5k`, `generate_image_1k`, `generate_image_2k`, `generate_image_4k`.

## Use Cases
- AI image generation
- Nano Banana image creation
- Google Gemini image API
- text-to-image
- image editing with reference photos
- product photography mockups
- hero banner generation
- social media graphics for Instagram and TikTok and LinkedIn
- e-commerce product visuals
- concept art
- app and product icon design
- marketing campaign creative
- ad creative generation
- brand asset production
- style transfer with reference images
- photoshoot replacement

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
### `generate_budget_image`

Action slug: `generate-budget-image`

No-account action URL: `POST https://www.agentpmt.com/api/external/tools/image-generation-agent/actions/generate-budget-image/invoke`

Price: `8` credits

Create or edit a lower-cost image from a prompt and optional reference images. Use for drafts, previews, and standard 1024px-class outputs.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `aspect_ratio` | `string` | no | Desired output aspect ratio. Default is 1:1. |
| `expiration_days` | `integer` | no | File Manager expiration in days, from 1 to 7. Default is 7. |
| `filename` | `string` | no | Optional output filename base. Extension is inferred from generated image MIME type. |
| `prompt` | `string` | yes | Image generation or edit instruction, 3 to 4000 characters. |
| `reference_images` | `array` | no | Optional reference images for edits or style/subject guidance. Maximum 4. |

Sample parameters:

```json
{
  "aspect_ratio": "1:1",
  "expiration_days": 1,
  "filename": "example filename",
  "prompt": "example prompt",
  "reference_images": [
    {
      "base64_data": "example base64 data",
      "file_id": "example file id",
      "mime_type": "image/png",
      "source_kind": "file_id",
      "url": "https://example.com"
    }
  ]
}
```

### `generate_image_0_5k`

Action slug: `generate-image-0-5k`

No-account action URL: `POST https://www.agentpmt.com/api/external/tools/image-generation-agent/actions/generate-image-0-5k/invoke`

Price: `10` credits

Create or edit a high-efficiency 0.5K image from a prompt and optional reference images.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `aspect_ratio` | `string` | no | Desired output aspect ratio. Default is 1:1. |
| `expiration_days` | `integer` | no | File Manager expiration in days, from 1 to 7. Default is 7. |
| `filename` | `string` | no | Optional output filename base. Extension is inferred from generated image MIME type. |
| `prompt` | `string` | yes | Image generation or edit instruction, 3 to 4000 characters. |
| `reference_images` | `array` | no | Optional reference images for edits or style/subject guidance. Maximum 4. |

Sample parameters:

```json
{
  "aspect_ratio": "1:1",
  "expiration_days": 1,
  "filename": "example filename",
  "prompt": "example prompt",
  "reference_images": [
    {
      "base64_data": "example base64 data",
      "file_id": "example file id",
      "mime_type": "image/png",
      "source_kind": "file_id",
      "url": "https://example.com"
    }
  ]
}
```

### `generate_image_1k`

Action slug: `generate-image-1k`

No-account action URL: `POST https://www.agentpmt.com/api/external/tools/image-generation-agent/actions/generate-image-1k/invoke`

Price: `15` credits

Create or edit a 1K image from a prompt and optional reference images.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `aspect_ratio` | `string` | no | Desired output aspect ratio. Default is 1:1. |
| `expiration_days` | `integer` | no | File Manager expiration in days, from 1 to 7. Default is 7. |
| `filename` | `string` | no | Optional output filename base. Extension is inferred from generated image MIME type. |
| `prompt` | `string` | yes | Image generation or edit instruction, 3 to 4000 characters. |
| `reference_images` | `array` | no | Optional reference images for edits or style/subject guidance. Maximum 4. |

Sample parameters:

```json
{
  "aspect_ratio": "1:1",
  "expiration_days": 1,
  "filename": "example filename",
  "prompt": "example prompt",
  "reference_images": [
    {
      "base64_data": "example base64 data",
      "file_id": "example file id",
      "mime_type": "image/png",
      "source_kind": "file_id",
      "url": "https://example.com"
    }
  ]
}
```

### `generate_image_2k`

Action slug: `generate-image-2k`

No-account action URL: `POST https://www.agentpmt.com/api/external/tools/image-generation-agent/actions/generate-image-2k/invoke`

Price: `25` credits

Create or edit a 2K image from a prompt and optional reference images.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `aspect_ratio` | `string` | no | Desired output aspect ratio. Default is 1:1. |
| `expiration_days` | `integer` | no | File Manager expiration in days, from 1 to 7. Default is 7. |
| `filename` | `string` | no | Optional output filename base. Extension is inferred from generated image MIME type. |
| `prompt` | `string` | yes | Image generation or edit instruction, 3 to 4000 characters. |
| `reference_images` | `array` | no | Optional reference images for edits or style/subject guidance. Maximum 4. |

Sample parameters:

```json
{
  "aspect_ratio": "1:1",
  "expiration_days": 1,
  "filename": "example filename",
  "prompt": "example prompt",
  "reference_images": [
    {
      "base64_data": "example base64 data",
      "file_id": "example file id",
      "mime_type": "image/png",
      "source_kind": "file_id",
      "url": "https://example.com"
    }
  ]
}
```

### `generate_image_4k`

Action slug: `generate-image-4k`

No-account action URL: `POST https://www.agentpmt.com/api/external/tools/image-generation-agent/actions/generate-image-4k/invoke`

Price: `40` credits

Create or edit a 4K image from a prompt and optional reference images.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `aspect_ratio` | `string` | no | Desired output aspect ratio. Default is 1:1. |
| `expiration_days` | `integer` | no | File Manager expiration in days, from 1 to 7. Default is 7. |
| `filename` | `string` | no | Optional output filename base. Extension is inferred from generated image MIME type. |
| `prompt` | `string` | yes | Image generation or edit instruction, 3 to 4000 characters. |
| `reference_images` | `array` | no | Optional reference images for edits or style/subject guidance. Maximum 4. |

Sample parameters:

```json
{
  "aspect_ratio": "1:1",
  "expiration_days": 1,
  "filename": "example filename",
  "prompt": "example prompt",
  "reference_images": [
    {
      "base64_data": "example base64 data",
      "file_id": "example file id",
      "mime_type": "image/png",
      "source_kind": "file_id",
      "url": "https://example.com"
    }
  ]
}
```

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "image-generation-agent"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "image-generation-agent"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "image-generation-agent"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "image-generation-agent"
}
```

REST lookup body with an AgentPMT Bearer Token:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "image-generation-agent"
  }
}
```

REST live examples body with an AgentPMT Bearer Token:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "image-generation-agent"
  }
}
```

## Call This Tool
Product slug: `image-generation-agent`

Marketplace page: https://www.agentpmt.com/marketplace/image-generation-agent

- AgentPMT account path: first use `../agentpmt-account-mcp-rest-api-setup` to connect the main MCP server or REST API with a Bearer Token from an Agent Group where this tool is enabled and required credentials are configured.
- No-account path: first use `../agentpmt-no-account-agentaddress-x402` to create an AgentAddress and handle x402 or signed-credit calls.
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
    "name": "Image-Generation-Agent",
    "arguments": {
      "action": "generate_budget_image",
      "aspect_ratio": "1:1",
      "expiration_days": 1,
      "filename": "example filename",
      "prompt": "example prompt",
      "reference_images": [
        {
          "base64_data": "example base64 data",
          "file_id": "example file id",
          "mime_type": "image/png",
          "source_kind": "file_id",
          "url": "https://example.com"
        }
      ]
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

REST call body with an AgentPMT Bearer Token:

```json
{
  "name": "image-generation-agent",
  "parameters": {
    "action": "generate_budget_image",
    "aspect_ratio": "1:1",
    "expiration_days": 1,
    "filename": "example filename",
    "prompt": "example prompt",
    "reference_images": [
      {
        "base64_data": "example base64 data",
        "file_id": "example file id",
        "mime_type": "image/png",
        "source_kind": "file_id",
        "url": "https://example.com"
      }
    ]
  }
}
```

No-account action path: `POST https://www.agentpmt.com/api/external/tools/image-generation-agent/actions/generate-budget-image/invoke`.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `generate_budget_image` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place Bearer Tokens, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- No-account AgentAddress/x402 setup: ../agentpmt-no-account-agentaddress-x402 (ClawHub: `agentpmt-no-account-agentaddress-x402`, page: https://clawhub.ai/agentpmt/agentpmt-no-account-agentaddress-x402; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-no-account-agentaddress-x402`)
- Marketplace product: https://www.agentpmt.com/marketplace/image-generation-agent
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
