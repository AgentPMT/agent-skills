# Minecraft Custom Mod Builder Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `minecraft-custom-mod-builder`

x402 action routes are enabled for this product through `https://www.agentpmt.com/api/external`.

## `create_mod_project`

Action slug: `create-mod-project`

x402 action URL: `POST https://www.agentpmt.com/api/external/tools/minecraft-custom-mod-builder/actions/create-mod-project/invoke`

Price: `15` credits

Generate installable Minecraft artifacts and upload them to File Manager. Supports Bedrock .mcaddon, Bedrock skin packs, Fabric jars/source, and NeoForge jars/source from structured specs. Supports deterministic world-side mechanics, scheduled/random events, cooldowns, radius conditions, custom commands with parameters, time/weather/title actions, scoreboards, particles/sounds, relative teleports, explosions, lightning, block changes, effects, tags, items, entities, machines, recipes, and Java client utility modules. Use render_preview_image when visual assets matter.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `advanced_resources` | `array` | no | Escape hatch for raw files: path plus content_base64, content_text, or source_file_id. |
| `allow_experimental_bedrock_features` | `boolean` | no | Allow Bedrock experimental features when a selected component requires experiments. |
| `assets` | `object` | no | Optional pre-bound textures, sounds, particles, models, and language entries. |
| `build_jar` | `boolean` | no | Fabric/NeoForge only; build the jar offline when true. |
| `compatibility_mode` | `string` | no | strict or allow_platform_passthrough. |
| `description` | `string` | no | Short mod description shown in pack/mod metadata. |
| `features` | `object` | no | FeatureSet object. Use arrays such as items, blocks, entities, events, commands, client_modules, machines, recipes, loot_tables, worldgen, scoreboards, particles, sounds, functions, storage, structures, biomes, dimensions, effects, and skins. Events support interval_ticks, cooldown_ticks, chance_percent, action_selection=random_one, wait actions, conditions such as entity_within_radius/time_of_day/weather_is/y_below/y_above/light_level_below, radius-targeted actions, typed command parameters with {param:name}, show_title display/timing, replace_held_item, time/weather actions, broadcast aliases, relative positions, particle count/spread, sound volume/pitch, scoreboard set/add/remove, and strict action-option validation. See product instructions for exact nested fields and platform gates. |
| `include_file_preview` | `boolean` | no | Include a compact file preview in response metadata. |
| `minecraft_version` | `string` | no | Pinned version. Omit to use the platform default; unsupported versions are rejected with supported-version guidance. |
| `mod_id` | `string` | yes | Lowercase namespace ^[a-z][a-z0-9_]{1,63}$; becomes generated identifier namespace. |
| `mod_metadata` | `object` | no | Optional metadata: version, license, authors, homepage_url, issue_tracker_url, credits, logo_texture, brand_color_hex, java_side, bedrock_experiments. |
| `mod_name` | `string` | yes | Human-readable mod name shown in generated pack/mod metadata. |
| `output_mode` | `string` | no | installable, source, or both. |
| `skin_pack` | `object` | no | Skin pack definition for target_platform=bedrock_skinpack. Include skins with 64x64 texture source. |
| `target_platform` | `string` | yes | One of bedrock, bedrock_skinpack, fabric, neoforge. Legacy forge is rejected with a NeoForge migration message. |
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
    "description": "Allow Bedrock experimental features when a selected component requires experiments.",
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
    "description": "Fabric/NeoForge only; build the jar offline when true.",
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
    "description": "Short mod description shown in pack/mod metadata.",
    "required": false,
    "type": "string"
  },
  "features": {
    "description": "FeatureSet object. Use arrays such as items, blocks, entities, events, commands, client_modules, machines, recipes, loot_tables, worldgen, scoreboards, particles, sounds, functions, storage, structures, biomes, dimensions, effects, and skins. Events support interval_ticks, cooldown_ticks, chance_percent, action_selection=random_one, wait actions, conditions such as entity_within_radius/time_of_day/weather_is/y_below/y_above/light_level_below, radius-targeted actions, typed command parameters with {param:name}, show_title display/timing, replace_held_item, time/weather actions, broadcast aliases, relative positions, particle count/spread, sound volume/pitch, scoreboard set/add/remove, and strict action-option validation. See product instructions for exact nested fields and platform gates.",
    "properties": {
      "animation_controllers": {
        "description": "animation_controllers feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "animations": {
        "description": "animations feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "biomes": {
        "description": "Custom biome definitions and worldgen references.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "blocks": {
        "description": "Custom blocks. Key fields: block_id, display_name, block_kind, texture, hardness, resistance, light_level, drops, crop/redstone/machine/container presets.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "client_modules": {
        "description": "Java-only client utility modules: utility_client_preset, performance_profile, fullbright, block_esp, entity_esp, tnt_cart_placement_esp, renderer_profile.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "commands": {
        "description": "Custom commands. Key fields: command_id, description, command_kind, permission_level, parameters, actions. Use {param:name} placeholders in action messages/commands.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "damage_types": {
        "description": "damage_types feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "dimensions": {
        "description": "Custom dimension definitions and linked biome/worldgen settings.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "effects": {
        "description": "Status/effect definitions. Key fields: effect_id, display_name, effect_kind, builtin_effect_id, duration_ticks, amplifier.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "enchantments": {
        "description": "enchantments feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "entities": {
        "description": "Custom mobs/entities. Key fields: entity_id, display_name, entity_kind, texture, health, attack_damage, movement_speed, families, ai_goals, scale, component_overrides.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "events": {
        "description": "Event behaviors. Key fields: event_id, event_kind, conditions, actions, interval_ticks, cooldown_ticks, chance_percent, action_selection.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "functions": {
        "description": "Bedrock/Java command function files. Use lines or commands aliases. Shell syntax is rejected.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "game_rules": {
        "description": "game_rules feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "items": {
        "description": "Custom items and tools. Key fields: item_id, display_name, item_kind, texture, tool_type/tool_tier, armor, food, durability, damage, max_stack_size.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "localizations": {
        "description": "localizations feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "loot_tables": {
        "description": "Loot tables for entity/block drops. Key fields: loot_id, target, drops, functions, conditions.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "machines": {
        "description": "Interact-driven machines. Key fields: machine_id/block_id, display_name, texture, processing_time_ticks, machine_recipes.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "particles": {
        "description": "Custom particles. Key fields: particle_id, texture, color_hex/source_file_id.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "recipes": {
        "description": "Crafting/smelting/smithing/brewing recipes. Key fields: recipe_id, recipe_kind, result_item, pattern/key, ingredients, input_item, count.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "render_controllers": {
        "description": "render_controllers feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "scoreboards": {
        "description": "Scoreboard objectives. Key fields: objective_id, display_name, criteria, display_slot.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "sounds": {
        "description": "Custom or vanilla sounds. Key fields: sound_id, source_file_id/source_base64, category, volume, pitch.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "storage": {
        "description": "Storage blocks/backpacks. Key fields: storage_id, display_name, storage_kind, texture, capacity.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "structures": {
        "description": "Structure assets and placements. Key fields: structure_id, source_file_id/source_base64, placement settings.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "tags": {
        "description": "Named tag presets for grouped behavior.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "trades": {
        "description": "trades feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "transportation": {
        "description": "transportation feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "ui": {
        "description": "ui feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "worldgen": {
        "description": "World generation features. Key fields: feature_id, feature_kind, block_id, target_block, vein_size, count_per_chunk, min_y, max_y, biomes.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
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
    "description": "Include a compact file preview in response metadata.",
    "required": false,
    "type": "boolean"
  },
  "minecraft_version": {
    "description": "Pinned version. Omit to use the platform default; unsupported versions are rejected with supported-version guidance.",
    "required": false,
    "type": "string"
  },
  "mod_id": {
    "description": "Lowercase namespace ^[a-z][a-z0-9_]{1,63}$; becomes generated identifier namespace.",
    "required": true,
    "type": "string"
  },
  "mod_metadata": {
    "description": "Optional metadata: version, license, authors, homepage_url, issue_tracker_url, credits, logo_texture, brand_color_hex, java_side, bedrock_experiments.",
    "required": false,
    "type": "object"
  },
  "mod_name": {
    "description": "Human-readable mod name shown in generated pack/mod metadata.",
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
    "description": "Skin pack definition for target_platform=bedrock_skinpack. Include skins with 64x64 texture source.",
    "required": false,
    "type": "object"
  },
  "target_platform": {
    "description": "One of bedrock, bedrock_skinpack, fabric, neoforge. Legacy forge is rejected with a NeoForge migration message.",
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

## `list_capabilities`

Action slug: `list-capabilities`

x402 action URL: `POST https://www.agentpmt.com/api/external/tools/minecraft-custom-mod-builder/actions/list-capabilities/invoke`

Price: `2` credits

Return supported platforms, pinned versions, feature kinds, event kinds, action kinds, client module kinds, event options, condition kinds, action options, unsupported families, and the capability matrix. Use this before planning complex Java/Bedrock behavior.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `target_platform` | `string` | no | One of bedrock, bedrock_skinpack, fabric, neoforge. Legacy forge is rejected with a NeoForge migration message. |

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
    "description": "One of bedrock, bedrock_skinpack, fabric, neoforge. Legacy forge is rejected with a NeoForge migration message.",
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

Render and upload an enlarged PNG preview for an item, block, entity, texture, or generated source archive. Uses the same current structured feature contract as create_mod_project when previewing from a spec.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `advanced_resources` | `array` | no | Escape hatch for raw files: path plus content_base64, content_text, or source_file_id. |
| `allow_experimental_bedrock_features` | `boolean` | no | Allow Bedrock experimental features when a selected component requires experiments. |
| `assets` | `object` | no | Optional pre-bound textures, sounds, particles, models, and language entries. |
| `compatibility_mode` | `string` | no | strict or allow_platform_passthrough. |
| `description` | `string` | no | Short mod description shown in pack/mod metadata. |
| `features` | `object` | no | FeatureSet object. Use arrays such as items, blocks, entities, events, commands, client_modules, machines, recipes, loot_tables, worldgen, scoreboards, particles, sounds, functions, storage, structures, biomes, dimensions, effects, and skins. Events support interval_ticks, cooldown_ticks, chance_percent, action_selection=random_one, wait actions, conditions such as entity_within_radius/time_of_day/weather_is/y_below/y_above/light_level_below, radius-targeted actions, typed command parameters with {param:name}, show_title display/timing, replace_held_item, time/weather actions, broadcast aliases, relative positions, particle count/spread, sound volume/pitch, scoreboard set/add/remove, and strict action-option validation. See product instructions for exact nested fields and platform gates. |
| `minecraft_version` | `string` | no | Pinned version. Omit to use the platform default; unsupported versions are rejected with supported-version guidance. |
| `mod_id` | `string` | no | Lowercase namespace ^[a-z][a-z0-9_]{1,63}$; becomes generated identifier namespace. |
| `mod_metadata` | `object` | no | Optional metadata: version, license, authors, homepage_url, issue_tracker_url, credits, logo_texture, brand_color_hex, java_side, bedrock_experiments. |
| `mod_name` | `string` | no | Human-readable mod name shown in generated pack/mod metadata. |
| `preview_background` | `string` | no | transparent, checkerboard, light, or dark. |
| `preview_size` | `integer` | no | Preview PNG size in pixels. |
| `preview_source_file_id` | `string` | no | File Manager file_id for a user-supplied image to preview directly. |
| `preview_target_id` | `string` | no | Identifier of the item/block/entity to preview. |
| `preview_target_kind` | `string` | no | item, block, or entity. Omit to auto-select. |
| `skin_pack` | `object` | no | Skin pack definition for target_platform=bedrock_skinpack. Include skins with 64x64 texture source. |
| `source_archive_file_id` | `string` | no | File Manager file_id for a previously generated source zip; preview an asset without resending the spec. |
| `target_platform` | `string` | no | One of bedrock, bedrock_skinpack, fabric, neoforge. Legacy forge is rejected with a NeoForge migration message. |

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
    "description": "Allow Bedrock experimental features when a selected component requires experiments.",
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
    "description": "Short mod description shown in pack/mod metadata.",
    "required": false,
    "type": "string"
  },
  "features": {
    "description": "FeatureSet object. Use arrays such as items, blocks, entities, events, commands, client_modules, machines, recipes, loot_tables, worldgen, scoreboards, particles, sounds, functions, storage, structures, biomes, dimensions, effects, and skins. Events support interval_ticks, cooldown_ticks, chance_percent, action_selection=random_one, wait actions, conditions such as entity_within_radius/time_of_day/weather_is/y_below/y_above/light_level_below, radius-targeted actions, typed command parameters with {param:name}, show_title display/timing, replace_held_item, time/weather actions, broadcast aliases, relative positions, particle count/spread, sound volume/pitch, scoreboard set/add/remove, and strict action-option validation. See product instructions for exact nested fields and platform gates.",
    "properties": {
      "animation_controllers": {
        "description": "animation_controllers feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "animations": {
        "description": "animations feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "biomes": {
        "description": "Custom biome definitions and worldgen references.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "blocks": {
        "description": "Custom blocks. Key fields: block_id, display_name, block_kind, texture, hardness, resistance, light_level, drops, crop/redstone/machine/container presets.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "client_modules": {
        "description": "Java-only client utility modules: utility_client_preset, performance_profile, fullbright, block_esp, entity_esp, tnt_cart_placement_esp, renderer_profile.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "commands": {
        "description": "Custom commands. Key fields: command_id, description, command_kind, permission_level, parameters, actions. Use {param:name} placeholders in action messages/commands.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "damage_types": {
        "description": "damage_types feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "dimensions": {
        "description": "Custom dimension definitions and linked biome/worldgen settings.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "effects": {
        "description": "Status/effect definitions. Key fields: effect_id, display_name, effect_kind, builtin_effect_id, duration_ticks, amplifier.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "enchantments": {
        "description": "enchantments feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "entities": {
        "description": "Custom mobs/entities. Key fields: entity_id, display_name, entity_kind, texture, health, attack_damage, movement_speed, families, ai_goals, scale, component_overrides.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "events": {
        "description": "Event behaviors. Key fields: event_id, event_kind, conditions, actions, interval_ticks, cooldown_ticks, chance_percent, action_selection.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "functions": {
        "description": "Bedrock/Java command function files. Use lines or commands aliases. Shell syntax is rejected.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "game_rules": {
        "description": "game_rules feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "items": {
        "description": "Custom items and tools. Key fields: item_id, display_name, item_kind, texture, tool_type/tool_tier, armor, food, durability, damage, max_stack_size.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "localizations": {
        "description": "localizations feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "loot_tables": {
        "description": "Loot tables for entity/block drops. Key fields: loot_id, target, drops, functions, conditions.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "machines": {
        "description": "Interact-driven machines. Key fields: machine_id/block_id, display_name, texture, processing_time_ticks, machine_recipes.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "particles": {
        "description": "Custom particles. Key fields: particle_id, texture, color_hex/source_file_id.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "recipes": {
        "description": "Crafting/smelting/smithing/brewing recipes. Key fields: recipe_id, recipe_kind, result_item, pattern/key, ingredients, input_item, count.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "render_controllers": {
        "description": "render_controllers feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "scoreboards": {
        "description": "Scoreboard objectives. Key fields: objective_id, display_name, criteria, display_slot.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "sounds": {
        "description": "Custom or vanilla sounds. Key fields: sound_id, source_file_id/source_base64, category, volume, pitch.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "storage": {
        "description": "Storage blocks/backpacks. Key fields: storage_id, display_name, storage_kind, texture, capacity.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "structures": {
        "description": "Structure assets and placements. Key fields: structure_id, source_file_id/source_base64, placement settings.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "tags": {
        "description": "Named tag presets for grouped behavior.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "trades": {
        "description": "trades feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "transportation": {
        "description": "transportation feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "ui": {
        "description": "ui feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "worldgen": {
        "description": "World generation features. Key fields: feature_id, feature_kind, block_id, target_block, vein_size, count_per_chunk, min_y, max_y, biomes.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      }
    },
    "required": false,
    "type": "object"
  },
  "minecraft_version": {
    "description": "Pinned version. Omit to use the platform default; unsupported versions are rejected with supported-version guidance.",
    "required": false,
    "type": "string"
  },
  "mod_id": {
    "description": "Lowercase namespace ^[a-z][a-z0-9_]{1,63}$; becomes generated identifier namespace.",
    "required": false,
    "type": "string"
  },
  "mod_metadata": {
    "description": "Optional metadata: version, license, authors, homepage_url, issue_tracker_url, credits, logo_texture, brand_color_hex, java_side, bedrock_experiments.",
    "required": false,
    "type": "object"
  },
  "mod_name": {
    "description": "Human-readable mod name shown in generated pack/mod metadata.",
    "required": false,
    "type": "string"
  },
  "preview_background": {
    "default": "checkerboard",
    "description": "transparent, checkerboard, light, or dark.",
    "enum": [
      "transparent",
      "checkerboard",
      "light",
      "dark"
    ],
    "required": false,
    "type": "string"
  },
  "preview_size": {
    "default": 256,
    "description": "Preview PNG size in pixels.",
    "maximum": 1024,
    "minimum": 64,
    "required": false,
    "type": "integer"
  },
  "preview_source_file_id": {
    "description": "File Manager file_id for a user-supplied image to preview directly.",
    "required": false,
    "type": "string"
  },
  "preview_target_id": {
    "description": "Identifier of the item/block/entity to preview.",
    "required": false,
    "type": "string"
  },
  "preview_target_kind": {
    "description": "item, block, or entity. Omit to auto-select.",
    "enum": [
      "item",
      "block",
      "entity"
    ],
    "required": false,
    "type": "string"
  },
  "skin_pack": {
    "description": "Skin pack definition for target_platform=bedrock_skinpack. Include skins with 64x64 texture source.",
    "required": false,
    "type": "object"
  },
  "source_archive_file_id": {
    "description": "File Manager file_id for a previously generated source zip; preview an asset without resending the spec.",
    "required": false,
    "type": "string"
  },
  "target_platform": {
    "description": "One of bedrock, bedrock_skinpack, fabric, neoforge. Legacy forge is rejected with a NeoForge migration message.",
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

## `validate_mod_project`

Action slug: `validate-mod-project`

x402 action URL: `POST https://www.agentpmt.com/api/external/tools/minecraft-custom-mod-builder/actions/validate-mod-project/invoke`

Price: `5` credits

Validate a structured mod specification or source archive without writing artifacts. Use this before create_mod_project for complex specs, especially specs with events, client_modules, command parameters, machine recipes, radius conditions, or platform-specific behavior.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `advanced_resources` | `array` | no | Escape hatch for raw files: path plus content_base64, content_text, or source_file_id. |
| `allow_experimental_bedrock_features` | `boolean` | no | Allow Bedrock experimental features when a selected component requires experiments. |
| `assets` | `object` | no | Optional pre-bound textures, sounds, particles, models, and language entries. |
| `compatibility_mode` | `string` | no | strict or allow_platform_passthrough. |
| `description` | `string` | no | Short mod description shown in pack/mod metadata. |
| `features` | `object` | no | FeatureSet object. Use arrays such as items, blocks, entities, events, commands, client_modules, machines, recipes, loot_tables, worldgen, scoreboards, particles, sounds, functions, storage, structures, biomes, dimensions, effects, and skins. Events support interval_ticks, cooldown_ticks, chance_percent, action_selection=random_one, wait actions, conditions such as entity_within_radius/time_of_day/weather_is/y_below/y_above/light_level_below, radius-targeted actions, typed command parameters with {param:name}, show_title display/timing, replace_held_item, time/weather actions, broadcast aliases, relative positions, particle count/spread, sound volume/pitch, scoreboard set/add/remove, and strict action-option validation. See product instructions for exact nested fields and platform gates. |
| `minecraft_version` | `string` | no | Pinned version. Omit to use the platform default; unsupported versions are rejected with supported-version guidance. |
| `mod_id` | `string` | no | Lowercase namespace ^[a-z][a-z0-9_]{1,63}$; becomes generated identifier namespace. |
| `mod_metadata` | `object` | no | Optional metadata: version, license, authors, homepage_url, issue_tracker_url, credits, logo_texture, brand_color_hex, java_side, bedrock_experiments. |
| `mod_name` | `string` | no | Human-readable mod name shown in generated pack/mod metadata. |
| `skin_pack` | `object` | no | Skin pack definition for target_platform=bedrock_skinpack. Include skins with 64x64 texture source. |
| `source_archive_file_id` | `string` | no | File Manager file_id for a previously generated source zip to validate instead of a spec. |
| `target_platform` | `string` | no | One of bedrock, bedrock_skinpack, fabric, neoforge. Legacy forge is rejected with a NeoForge migration message. |

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
    "description": "Allow Bedrock experimental features when a selected component requires experiments.",
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
    "description": "Short mod description shown in pack/mod metadata.",
    "required": false,
    "type": "string"
  },
  "features": {
    "description": "FeatureSet object. Use arrays such as items, blocks, entities, events, commands, client_modules, machines, recipes, loot_tables, worldgen, scoreboards, particles, sounds, functions, storage, structures, biomes, dimensions, effects, and skins. Events support interval_ticks, cooldown_ticks, chance_percent, action_selection=random_one, wait actions, conditions such as entity_within_radius/time_of_day/weather_is/y_below/y_above/light_level_below, radius-targeted actions, typed command parameters with {param:name}, show_title display/timing, replace_held_item, time/weather actions, broadcast aliases, relative positions, particle count/spread, sound volume/pitch, scoreboard set/add/remove, and strict action-option validation. See product instructions for exact nested fields and platform gates.",
    "properties": {
      "animation_controllers": {
        "description": "animation_controllers feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "animations": {
        "description": "animations feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "biomes": {
        "description": "Custom biome definitions and worldgen references.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "blocks": {
        "description": "Custom blocks. Key fields: block_id, display_name, block_kind, texture, hardness, resistance, light_level, drops, crop/redstone/machine/container presets.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "client_modules": {
        "description": "Java-only client utility modules: utility_client_preset, performance_profile, fullbright, block_esp, entity_esp, tnt_cart_placement_esp, renderer_profile.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "commands": {
        "description": "Custom commands. Key fields: command_id, description, command_kind, permission_level, parameters, actions. Use {param:name} placeholders in action messages/commands.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "damage_types": {
        "description": "damage_types feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "dimensions": {
        "description": "Custom dimension definitions and linked biome/worldgen settings.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "effects": {
        "description": "Status/effect definitions. Key fields: effect_id, display_name, effect_kind, builtin_effect_id, duration_ticks, amplifier.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "enchantments": {
        "description": "enchantments feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "entities": {
        "description": "Custom mobs/entities. Key fields: entity_id, display_name, entity_kind, texture, health, attack_damage, movement_speed, families, ai_goals, scale, component_overrides.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "events": {
        "description": "Event behaviors. Key fields: event_id, event_kind, conditions, actions, interval_ticks, cooldown_ticks, chance_percent, action_selection.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "functions": {
        "description": "Bedrock/Java command function files. Use lines or commands aliases. Shell syntax is rejected.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "game_rules": {
        "description": "game_rules feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "items": {
        "description": "Custom items and tools. Key fields: item_id, display_name, item_kind, texture, tool_type/tool_tier, armor, food, durability, damage, max_stack_size.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "localizations": {
        "description": "localizations feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "loot_tables": {
        "description": "Loot tables for entity/block drops. Key fields: loot_id, target, drops, functions, conditions.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "machines": {
        "description": "Interact-driven machines. Key fields: machine_id/block_id, display_name, texture, processing_time_ticks, machine_recipes.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "particles": {
        "description": "Custom particles. Key fields: particle_id, texture, color_hex/source_file_id.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "recipes": {
        "description": "Crafting/smelting/smithing/brewing recipes. Key fields: recipe_id, recipe_kind, result_item, pattern/key, ingredients, input_item, count.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "render_controllers": {
        "description": "render_controllers feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "scoreboards": {
        "description": "Scoreboard objectives. Key fields: objective_id, display_name, criteria, display_slot.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "sounds": {
        "description": "Custom or vanilla sounds. Key fields: sound_id, source_file_id/source_base64, category, volume, pitch.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "storage": {
        "description": "Storage blocks/backpacks. Key fields: storage_id, display_name, storage_kind, texture, capacity.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "structures": {
        "description": "Structure assets and placements. Key fields: structure_id, source_file_id/source_base64, placement settings.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "tags": {
        "description": "Named tag presets for grouped behavior.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "trades": {
        "description": "trades feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "transportation": {
        "description": "transportation feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "ui": {
        "description": "ui feature array. See product instructions for exact fields.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      },
      "worldgen": {
        "description": "World generation features. Key fields: feature_id, feature_kind, block_id, target_block, vein_size, count_per_chunk, min_y, max_y, biomes.",
        "items": {
          "description": "Nested object; see product instructions for exact fields.",
          "type": "object"
        },
        "required": false,
        "type": "array"
      }
    },
    "required": false,
    "type": "object"
  },
  "minecraft_version": {
    "description": "Pinned version. Omit to use the platform default; unsupported versions are rejected with supported-version guidance.",
    "required": false,
    "type": "string"
  },
  "mod_id": {
    "description": "Lowercase namespace ^[a-z][a-z0-9_]{1,63}$; becomes generated identifier namespace.",
    "required": false,
    "type": "string"
  },
  "mod_metadata": {
    "description": "Optional metadata: version, license, authors, homepage_url, issue_tracker_url, credits, logo_texture, brand_color_hex, java_side, bedrock_experiments.",
    "required": false,
    "type": "object"
  },
  "mod_name": {
    "description": "Human-readable mod name shown in generated pack/mod metadata.",
    "required": false,
    "type": "string"
  },
  "skin_pack": {
    "description": "Skin pack definition for target_platform=bedrock_skinpack. Include skins with 64x64 texture source.",
    "required": false,
    "type": "object"
  },
  "source_archive_file_id": {
    "description": "File Manager file_id for a previously generated source zip to validate instead of a spec.",
    "required": false,
    "type": "string"
  },
  "target_platform": {
    "description": "One of bedrock, bedrock_skinpack, fabric, neoforge. Legacy forge is rejected with a NeoForge migration message.",
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
