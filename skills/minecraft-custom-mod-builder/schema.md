# Minecraft Custom Mod Builder Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `minecraft-custom-mod-builder`

x402 action routes are enabled for this product through `https://www.agentpmt.com/api/external`.

## `create_mod_project`

Action slug: `create-mod-project`

x402 action URL: `POST https://www.agentpmt.com/api/external/tools/minecraft-custom-mod-builder/actions/create-mod-project/invoke`

Price: `15` credits

Generate installable Minecraft artifacts and upload them to File Manager. Supports Bedrock .mcaddon, Bedrock skin packs, Fabric jars/source, and NeoForge jars/source from structured specs.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `advanced_resources` | `array` | no | Escape hatch for raw files: path plus content_base64, content_text, or source_file_id. |
| `allow_experimental_bedrock_features` | `boolean` | no | Allow Bedrock experimental features when selected components require experiments. |
| `assets` | `object` | no | Optional pre-bound textures, sounds, particles, models, and language entries. |
| `build_jar` | `boolean` | no | Fabric/NeoForge only. Build the jar offline when true; for long Java jar builds use start_build_job instead of synchronous create_mod_project. |
| `compatibility_mode` | `string` | no | strict or allow_platform_passthrough. |
| `description` | `string` | no | Short mod description. |
| `features` | `object` | no | FeatureSet object. Use arrays such as items, blocks, entities, events, commands, client_modules, machines, recipes, loot_tables, worldgen, scoreboards, particles, sounds, functions, storage, structures, biomes, dimensions, effects, and skins. See product instructions for exact nested fields and platform gates. |
| `include_file_preview` | `boolean` | no | Include capped text previews in generated_files. |
| `minecraft_version` | `string` | no | Pinned version. Omit unless the user explicitly asks for the supported pinned version. |
| `mod_id` | `string` | yes | Lowercase namespace matching ^[a-z][a-z0-9_]{1,63}$. |
| `mod_metadata` | `object` | no | Optional metadata such as version, license, authors, homepage_url, issue_tracker_url, credits, logo_texture, brand_color_hex, java_side, and bedrock_experiments. |
| `mod_name` | `string` | yes | Human-readable mod name. |
| `output_mode` | `string` | no | installable, source, or both. Use source with build_jar=false for fast Java source generation. |
| `skin_pack` | `object` | no | Skin pack definition for target_platform=bedrock_skinpack. Include skins with 64x64 texture sources. |
| `target_platform` | `string` | yes | bedrock, bedrock_skinpack, fabric, or neoforge. Legacy forge is rejected with a NeoForge migration message. |
| `validate_output` | `boolean` | no | Run output validation when supported. |

Sample parameters:

```json
{
  "advanced_resources": [
    {}
  ],
  "allow_experimental_bedrock_features": true,
  "assets": {},
  "build_jar": true,
  "compatibility_mode": "strict",
  "description": "example description",
  "features": {
    "animation_controllers": [
      {}
    ],
    "animations": [
      {}
    ],
    "biomes": [
      {}
    ],
    "blocks": [
      {}
    ],
    "client_modules": [
      {}
    ],
    "commands": [
      {}
    ],
    "damage_types": [
      {}
    ],
    "dimensions": [
      {}
    ]
  },
  "include_file_preview": true
}
```

Generated JSON parameter schema:

```json
{
  "advanced_resources": {
    "description": "Escape hatch for raw files: path plus content_base64, content_text, or source_file_id.",
    "items": {
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "allow_experimental_bedrock_features": {
    "description": "Allow Bedrock experimental features when selected components require experiments.",
    "required": false,
    "type": "boolean"
  },
  "assets": {
    "description": "Optional pre-bound textures, sounds, particles, models, and language entries.",
    "required": false,
    "type": "object"
  },
  "build_jar": {
    "default": true,
    "description": "Fabric/NeoForge only. Build the jar offline when true; for long Java jar builds use start_build_job instead of synchronous create_mod_project.",
    "required": false,
    "type": "boolean"
  },
  "compatibility_mode": {
    "default": "strict",
    "description": "strict or allow_platform_passthrough.",
    "enum": [
      "strict",
      "allow_platform_passthrough"
    ],
    "required": false,
    "type": "string"
  },
  "description": {
    "description": "Short mod description.",
    "required": false,
    "type": "string"
  },
  "features": {
    "description": "FeatureSet object. Use arrays such as items, blocks, entities, events, commands, client_modules, machines, recipes, loot_tables, worldgen, scoreboards, particles, sounds, functions, storage, structures, biomes, dimensions, effects, and skins. See product instructions for exact nested fields and platform gates.",
    "properties": {
      "animation_controllers": {
        "description": "Animation controller definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "animations": {
        "description": "Animation definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "biomes": {
        "description": "Custom biome definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "blocks": {
        "description": "Custom blocks.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "client_modules": {
        "description": "Java-only client utility modules.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "commands": {
        "description": "Custom commands.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "damage_types": {
        "description": "Damage type definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "dimensions": {
        "description": "Custom dimension definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "effects": {
        "description": "Status/effect definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "enchantments": {
        "description": "Enchantment definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "entities": {
        "description": "Custom mobs/entities.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "events": {
        "description": "Event behaviors.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "functions": {
        "description": "Bedrock/Java command function files.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "game_rules": {
        "description": "Game rule definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "items": {
        "description": "Custom items and tools.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "localizations": {
        "description": "Localization entries.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "loot_tables": {
        "description": "Loot tables.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "machines": {
        "description": "Interact-driven machines.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "particles": {
        "description": "Custom particles.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "recipes": {
        "description": "Crafting/smelting/smithing/brewing recipes.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "render_controllers": {
        "description": "Render controller definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "scoreboards": {
        "description": "Scoreboard objectives.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "sounds": {
        "description": "Custom or vanilla sounds.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "storage": {
        "description": "Storage blocks and backpacks.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "structures": {
        "description": "Structure assets and placements.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "tags": {
        "description": "Named tag presets.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "trades": {
        "description": "Trade definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "transportation": {
        "description": "Transportation definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "ui": {
        "description": "UI definitions.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "worldgen": {
        "description": "World generation features.",
        "items": {
          "type": "object"
        },
        "required": false,
        "type": "array"
      }
    },
    "required": false,
    "type": "object"
  },
  "include_file_preview": {
    "description": "Include capped text previews in generated_files.",
    "required": false,
    "type": "boolean"
  },
  "minecraft_version": {
    "description": "Pinned version. Omit unless the user explicitly asks for the supported pinned version.",
    "required": false,
    "type": "string"
  },
  "mod_id": {
    "description": "Lowercase namespace matching ^[a-z][a-z0-9_]{1,63}$.",
    "required": true,
    "type": "string"
  },
  "mod_metadata": {
    "description": "Optional metadata such as version, license, authors, homepage_url, issue_tracker_url, credits, logo_texture, brand_color_hex, java_side, and bedrock_experiments.",
    "required": false,
    "type": "object"
  },
  "mod_name": {
    "description": "Human-readable mod name.",
    "required": true,
    "type": "string"
  },
  "output_mode": {
    "default": "both",
    "description": "installable, source, or both. Use source with build_jar=false for fast Java source generation.",
    "enum": [
      "installable",
      "source",
      "both"
    ],
    "required": false,
    "type": "string"
  },
  "skin_pack": {
    "description": "Skin pack definition for target_platform=bedrock_skinpack. Include skins with 64x64 texture sources.",
    "required": false,
    "type": "object"
  },
  "target_platform": {
    "description": "bedrock, bedrock_skinpack, fabric, or neoforge. Legacy forge is rejected with a NeoForge migration message.",
    "enum": [
      "bedrock",
      "bedrock_skinpack",
      "fabric",
      "neoforge"
    ],
    "required": true,
    "type": "string"
  },
  "validate_output": {
    "default": true,
    "description": "Run output validation when supported.",
    "required": false,
    "type": "boolean"
  }
}
```

## `get_build_job`

Action slug: `get-build-job`

x402 action URL: `POST https://www.agentpmt.com/api/external/tools/minecraft-custom-mod-builder/actions/get-build-job/invoke`

Price: `2` credits

Fetch one queued Minecraft build job by task_id. Poll after start_build_job until status is completed or failed.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `task_id` | `string` | yes | Build job id returned by start_build_job. |
| `timeout_seconds` | `integer` | no | HTTP timeout for the status lookup; defaults to 600 seconds and may be 10-1200. |

Sample parameters:

```json
{
  "task_id": "example task id",
  "timeout_seconds": 600
}
```

Generated JSON parameter schema:

```json
{
  "task_id": {
    "description": "Build job id returned by start_build_job.",
    "required": true,
    "type": "string"
  },
  "timeout_seconds": {
    "default": 600,
    "description": "HTTP timeout for the status lookup; defaults to 600 seconds and may be 10-1200.",
    "maximum": 1200,
    "minimum": 10,
    "required": false,
    "type": "integer"
  }
}
```

## `list_build_jobs`

Action slug: `list-build-jobs`

x402 action URL: `POST https://www.agentpmt.com/api/external/tools/minecraft-custom-mod-builder/actions/list-build-jobs/invoke`

Price: `2` credits

List recent Minecraft build jobs for the active budget. Use this to recover a task_id or inspect recent queued/completed builds.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `limit` | `integer` | no | Maximum number of build jobs to return, from 1 to 100. |
| `timeout_seconds` | `integer` | no | HTTP timeout for the list lookup; defaults to 600 seconds and may be 10-1200. |

Sample parameters:

```json
{
  "limit": 20,
  "timeout_seconds": 600
}
```

Generated JSON parameter schema:

```json
{
  "limit": {
    "default": 20,
    "description": "Maximum number of build jobs to return, from 1 to 100.",
    "maximum": 100,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "timeout_seconds": {
    "default": 600,
    "description": "HTTP timeout for the list lookup; defaults to 600 seconds and may be 10-1200.",
    "maximum": 1200,
    "minimum": 10,
    "required": false,
    "type": "integer"
  }
}
```

## `list_capabilities`

Action slug: `list-capabilities`

x402 action URL: `POST https://www.agentpmt.com/api/external/tools/minecraft-custom-mod-builder/actions/list-capabilities/invoke`

Price: `2` credits

Return supported platforms, pinned versions, feature kinds, event/action/condition matrices, client module kinds, and unsupported families. Use before planning complex Bedrock/Fabric/NeoForge behavior.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `target_platform` | `string` | no | Optional platform filter. |

Sample parameters:

```json
{
  "target_platform": "bedrock"
}
```

Generated JSON parameter schema:

```json
{
  "target_platform": {
    "description": "Optional platform filter.",
    "enum": [
      "bedrock",
      "bedrock_skinpack",
      "fabric",
      "neoforge"
    ],
    "required": false,
    "type": "string"
  }
}
```

## `render_preview_image`

Action slug: `render-preview-image`

x402 action URL: `POST https://www.agentpmt.com/api/external/tools/minecraft-custom-mod-builder/actions/render-preview-image/invoke`

Price: `5` credits

Render and upload an enlarged PNG preview for an item, block, entity, texture, or generated source archive. Use after create_mod_project when visual assets matter.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `advanced_resources` | `array` | no | Escape hatch for raw files. |
| `allow_experimental_bedrock_features` | `boolean` | no | Allow Bedrock experimental features when selected components require experiments. |
| `assets` | `object` | no | Optional pre-bound textures, sounds, particles, models, and language entries. |
| `compatibility_mode` | `string` | no | strict or allow_platform_passthrough. |
| `description` | `string` | no | Short mod description. |
| `features` | `object` | no | FeatureSet object for spec preview. |
| `minecraft_version` | `string` | no | Pinned version. Omit unless explicitly needed. |
| `mod_id` | `string` | no | Lowercase namespace for spec/source preview. |
| `mod_metadata` | `object` | no | Optional metadata. |
| `mod_name` | `string` | no | Human-readable mod name for spec preview. |
| `preview_background` | `string` | no | checkerboard, transparent, white, or black. |
| `preview_size` | `integer` | no | Square preview PNG size from 32 to 1024 pixels. |
| `preview_source_file_id` | `string` | no | File Manager image file_id for direct image preview. |
| `preview_target_id` | `string` | no | Feature id or namespaced id, such as flame_sword or flame_tools:flame_sword. |
| `preview_target_kind` | `string` | no | item, block, entity, or texture. |
| `skin_pack` | `object` | no | Skin pack definition for target_platform=bedrock_skinpack. |
| `source_archive_file_id` | `string` | no | File Manager file_id for a previously generated source zip to preview from. |
| `target_platform` | `string` | no | Optional platform context. |

Sample parameters:

```json
{
  "advanced_resources": [
    {}
  ],
  "allow_experimental_bedrock_features": true,
  "assets": {},
  "compatibility_mode": "strict",
  "description": "example description",
  "features": {},
  "minecraft_version": "example minecraft version",
  "mod_id": "example mod id"
}
```

Generated JSON parameter schema:

```json
{
  "advanced_resources": {
    "description": "Escape hatch for raw files.",
    "items": {
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "allow_experimental_bedrock_features": {
    "description": "Allow Bedrock experimental features when selected components require experiments.",
    "required": false,
    "type": "boolean"
  },
  "assets": {
    "description": "Optional pre-bound textures, sounds, particles, models, and language entries.",
    "required": false,
    "type": "object"
  },
  "compatibility_mode": {
    "default": "strict",
    "description": "strict or allow_platform_passthrough.",
    "enum": [
      "strict",
      "allow_platform_passthrough"
    ],
    "required": false,
    "type": "string"
  },
  "description": {
    "description": "Short mod description.",
    "required": false,
    "type": "string"
  },
  "features": {
    "description": "FeatureSet object for spec preview.",
    "required": false,
    "type": "object"
  },
  "minecraft_version": {
    "description": "Pinned version. Omit unless explicitly needed.",
    "required": false,
    "type": "string"
  },
  "mod_id": {
    "description": "Lowercase namespace for spec/source preview.",
    "required": false,
    "type": "string"
  },
  "mod_metadata": {
    "description": "Optional metadata.",
    "required": false,
    "type": "object"
  },
  "mod_name": {
    "description": "Human-readable mod name for spec preview.",
    "required": false,
    "type": "string"
  },
  "preview_background": {
    "default": "checkerboard",
    "description": "checkerboard, transparent, white, or black.",
    "enum": [
      "checkerboard",
      "transparent",
      "white",
      "black"
    ],
    "required": false,
    "type": "string"
  },
  "preview_size": {
    "default": 256,
    "description": "Square preview PNG size from 32 to 1024 pixels.",
    "maximum": 1024,
    "minimum": 32,
    "required": false,
    "type": "integer"
  },
  "preview_source_file_id": {
    "description": "File Manager image file_id for direct image preview.",
    "required": false,
    "type": "string"
  },
  "preview_target_id": {
    "description": "Feature id or namespaced id, such as flame_sword or flame_tools:flame_sword.",
    "required": false,
    "type": "string"
  },
  "preview_target_kind": {
    "description": "item, block, entity, or texture.",
    "enum": [
      "item",
      "block",
      "entity",
      "texture"
    ],
    "required": false,
    "type": "string"
  },
  "skin_pack": {
    "description": "Skin pack definition for target_platform=bedrock_skinpack.",
    "required": false,
    "type": "object"
  },
  "source_archive_file_id": {
    "description": "File Manager file_id for a previously generated source zip to preview from.",
    "required": false,
    "type": "string"
  },
  "target_platform": {
    "description": "Optional platform context.",
    "enum": [
      "bedrock",
      "bedrock_skinpack",
      "fabric",
      "neoforge"
    ],
    "required": false,
    "type": "string"
  }
}
```

## `start_build_job`

Action slug: `start-build-job`

x402 action URL: `POST https://www.agentpmt.com/api/external/tools/minecraft-custom-mod-builder/actions/start-build-job/invoke`

Price: `15` credits

Queue long-running Minecraft mod generation and return immediately with a task_id. Use this instead of create_mod_project for Fabric/NeoForge jar builds or requests likely to exceed chat/tool timeouts. The input spec is the same as create_mod_project; poll get_build_job until completed or failed.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `advanced_resources` | `array` | no | Escape hatch for raw files. |
| `allow_experimental_bedrock_features` | `boolean` | no | Allow Bedrock experimental features when selected components require experiments. |
| `assets` | `object` | no | Optional pre-bound textures, sounds, particles, models, and language entries. |
| `build_jar` | `boolean` | no | Fabric/NeoForge only. Defaults true; this queued action is intended for build_jar=true jar builds. |
| `compatibility_mode` | `string` | no | strict or allow_platform_passthrough. |
| `description` | `string` | no | Short mod description. |
| `features` | `object` | no | FeatureSet object. Same shape as create_mod_project. |
| `include_file_preview` | `boolean` | no | Include capped text previews in generated_files. |
| `minecraft_version` | `string` | no | Pinned version. Omit unless explicitly needed. |
| `mod_id` | `string` | yes | Lowercase namespace matching ^[a-z][a-z0-9_]{1,63}$. |
| `mod_metadata` | `object` | no | Optional metadata. |
| `mod_name` | `string` | yes | Human-readable mod name. |
| `output_mode` | `string` | no | installable, source, or both. |
| `skin_pack` | `object` | no | Skin pack definition for target_platform=bedrock_skinpack. |
| `target_platform` | `string` | yes | bedrock, bedrock_skinpack, fabric, or neoforge. Use this mainly for Fabric/NeoForge jar builds. |
| `validate_output` | `boolean` | no | Run output validation when supported. |

Sample parameters:

```json
{
  "advanced_resources": [
    {}
  ],
  "allow_experimental_bedrock_features": true,
  "assets": {},
  "build_jar": true,
  "compatibility_mode": "strict",
  "description": "example description",
  "features": {},
  "include_file_preview": true
}
```

Generated JSON parameter schema:

```json
{
  "advanced_resources": {
    "description": "Escape hatch for raw files.",
    "items": {
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "allow_experimental_bedrock_features": {
    "description": "Allow Bedrock experimental features when selected components require experiments.",
    "required": false,
    "type": "boolean"
  },
  "assets": {
    "description": "Optional pre-bound textures, sounds, particles, models, and language entries.",
    "required": false,
    "type": "object"
  },
  "build_jar": {
    "default": true,
    "description": "Fabric/NeoForge only. Defaults true; this queued action is intended for build_jar=true jar builds.",
    "required": false,
    "type": "boolean"
  },
  "compatibility_mode": {
    "default": "strict",
    "description": "strict or allow_platform_passthrough.",
    "enum": [
      "strict",
      "allow_platform_passthrough"
    ],
    "required": false,
    "type": "string"
  },
  "description": {
    "description": "Short mod description.",
    "required": false,
    "type": "string"
  },
  "features": {
    "description": "FeatureSet object. Same shape as create_mod_project.",
    "required": false,
    "type": "object"
  },
  "include_file_preview": {
    "description": "Include capped text previews in generated_files.",
    "required": false,
    "type": "boolean"
  },
  "minecraft_version": {
    "description": "Pinned version. Omit unless explicitly needed.",
    "required": false,
    "type": "string"
  },
  "mod_id": {
    "description": "Lowercase namespace matching ^[a-z][a-z0-9_]{1,63}$.",
    "required": true,
    "type": "string"
  },
  "mod_metadata": {
    "description": "Optional metadata.",
    "required": false,
    "type": "object"
  },
  "mod_name": {
    "description": "Human-readable mod name.",
    "required": true,
    "type": "string"
  },
  "output_mode": {
    "default": "both",
    "description": "installable, source, or both.",
    "enum": [
      "installable",
      "source",
      "both"
    ],
    "required": false,
    "type": "string"
  },
  "skin_pack": {
    "description": "Skin pack definition for target_platform=bedrock_skinpack.",
    "required": false,
    "type": "object"
  },
  "target_platform": {
    "description": "bedrock, bedrock_skinpack, fabric, or neoforge. Use this mainly for Fabric/NeoForge jar builds.",
    "enum": [
      "bedrock",
      "bedrock_skinpack",
      "fabric",
      "neoforge"
    ],
    "required": true,
    "type": "string"
  },
  "validate_output": {
    "default": true,
    "description": "Run output validation when supported.",
    "required": false,
    "type": "boolean"
  }
}
```

## `validate_mod_project`

Action slug: `validate-mod-project`

x402 action URL: `POST https://www.agentpmt.com/api/external/tools/minecraft-custom-mod-builder/actions/validate-mod-project/invoke`

Price: `5` credits

Validate a structured Minecraft mod spec or previously generated source archive without writing artifacts.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `advanced_resources` | `array` | no | Escape hatch for raw files: path plus content_base64, content_text, or source_file_id. |
| `allow_experimental_bedrock_features` | `boolean` | no | Allow Bedrock experimental features when selected components require experiments. |
| `assets` | `object` | no | Optional pre-bound textures, sounds, particles, models, and language entries. |
| `compatibility_mode` | `string` | no | strict or allow_platform_passthrough. |
| `description` | `string` | no | Short mod description. |
| `features` | `object` | no | FeatureSet object. Use arrays such as items, blocks, entities, events, commands, client_modules, machines, recipes, loot_tables, worldgen, scoreboards, particles, sounds, functions, storage, structures, biomes, dimensions, effects, and skins. See product instructions for exact nested fields and platform gates. |
| `minecraft_version` | `string` | no | Pinned version. Omit unless the user explicitly asks for the supported pinned version. |
| `mod_id` | `string` | no | Lowercase namespace matching ^[a-z][a-z0-9_]{1,63}$. |
| `mod_metadata` | `object` | no | Optional metadata such as version, license, authors, homepage_url, issue_tracker_url, credits, logo_texture, brand_color_hex, java_side, and bedrock_experiments. |
| `mod_name` | `string` | no | Human-readable mod name. |
| `skin_pack` | `object` | no | Skin pack definition for target_platform=bedrock_skinpack. Include skins with 64x64 texture sources. |
| `source_archive_file_id` | `string` | no | File Manager file_id for a previously generated source zip to validate instead of a spec. |
| `target_platform` | `string` | no | bedrock, bedrock_skinpack, fabric, or neoforge. Legacy forge is rejected with a NeoForge migration message. |

Sample parameters:

```json
{
  "advanced_resources": [
    {}
  ],
  "allow_experimental_bedrock_features": true,
  "assets": {},
  "compatibility_mode": "strict",
  "description": "example description",
  "features": {},
  "minecraft_version": "example minecraft version",
  "mod_id": "example mod id"
}
```

Generated JSON parameter schema:

```json
{
  "advanced_resources": {
    "description": "Escape hatch for raw files: path plus content_base64, content_text, or source_file_id.",
    "items": {
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "allow_experimental_bedrock_features": {
    "description": "Allow Bedrock experimental features when selected components require experiments.",
    "required": false,
    "type": "boolean"
  },
  "assets": {
    "description": "Optional pre-bound textures, sounds, particles, models, and language entries.",
    "required": false,
    "type": "object"
  },
  "compatibility_mode": {
    "default": "strict",
    "description": "strict or allow_platform_passthrough.",
    "enum": [
      "strict",
      "allow_platform_passthrough"
    ],
    "required": false,
    "type": "string"
  },
  "description": {
    "description": "Short mod description.",
    "required": false,
    "type": "string"
  },
  "features": {
    "description": "FeatureSet object. Use arrays such as items, blocks, entities, events, commands, client_modules, machines, recipes, loot_tables, worldgen, scoreboards, particles, sounds, functions, storage, structures, biomes, dimensions, effects, and skins. See product instructions for exact nested fields and platform gates.",
    "required": false,
    "type": "object"
  },
  "minecraft_version": {
    "description": "Pinned version. Omit unless the user explicitly asks for the supported pinned version.",
    "required": false,
    "type": "string"
  },
  "mod_id": {
    "description": "Lowercase namespace matching ^[a-z][a-z0-9_]{1,63}$.",
    "required": false,
    "type": "string"
  },
  "mod_metadata": {
    "description": "Optional metadata such as version, license, authors, homepage_url, issue_tracker_url, credits, logo_texture, brand_color_hex, java_side, and bedrock_experiments.",
    "required": false,
    "type": "object"
  },
  "mod_name": {
    "description": "Human-readable mod name.",
    "required": false,
    "type": "string"
  },
  "skin_pack": {
    "description": "Skin pack definition for target_platform=bedrock_skinpack. Include skins with 64x64 texture sources.",
    "required": false,
    "type": "object"
  },
  "source_archive_file_id": {
    "description": "File Manager file_id for a previously generated source zip to validate instead of a spec.",
    "required": false,
    "type": "string"
  },
  "target_platform": {
    "description": "bedrock, bedrock_skinpack, fabric, or neoforge. Legacy forge is rejected with a NeoForge migration message.",
    "enum": [
      "bedrock",
      "bedrock_skinpack",
      "fabric",
      "neoforge"
    ],
    "required": false,
    "type": "string"
  }
}
```
