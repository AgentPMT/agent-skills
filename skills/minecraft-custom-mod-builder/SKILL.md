---
name: minecraft-custom-mod-builder
description: "Minecraft Custom Mod Builder: Deterministically generate and preview Minecraft Bedrock, Bedrock skin pack, Fabric, and NeoForge artifacts from structured specs. Use when an agent needs minecraft custom mod builder, create installable minecraft bedrock add ons (.mcaddon) from a simple description, build java mods for fabric and neoforge and download the .jar, design custom swords, pickaxes, create mod project, target platform, mod id through AgentPMT-hosted remote tool calls."
version: 1.0.1
homepage: https://www.agentpmt.com/marketplace/minecraft-custom-mod-builder
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/minecraft-custom-mod-builder"}}
---
# Minecraft Custom Mod Builder

## Freshness
Last updated: `2026-07-08`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Create your own custom Minecraft mods and add-ons — no coding required. Just describe what you want to add to the game, from a flaming sword or a glowing ore to a rideable mob, a custom skin pack, or a whole new dimension, and get back a ready-to-install file in seconds. Build for Minecraft Bedrock (.mcaddon) and Java with Fabric and NeoForge (.jar). Create items, weapons, tools, armor, blocks, ores, food, mobs, bosses, biomes, structures, recipes, loot tables, enchantments, trades, and special in-game behavior — each with its own custom texture from a color, your own artwork, or generated pixel art. Preview every icon before you install, and download editable source so you can keep building. Perfect for creators, streamers, server owners, and players who want their own Minecraft content fast.

## Product Instructions
### Minecraft Mod Builder

Generate deterministic Minecraft Bedrock, Fabric, and NeoForge mod artifacts from structured specifications. This tool does not call an LLM, does not accept prompts, and does not require user credentials.

#### Two Rules That Will Save You Many Retries

##### Rule 1 — One ItemSpec equals one in-game item

A single `ItemSpec` produces one in-game item. The fields `damage`, `durability`, `max_stack_size`, `nutrition`, `tool`, `armor`, `food`, `block_placer`, `entity_placer`, `enchantable`, `repairable`, `digger`, `cooldown`, `glint`, `rarity`, `dyeable`, and `component_overrides` all attach to the *same item*. A weapon does **not** need a separate entity or a separate "damage item." A sword does **not** need a partner "enchantment item." You ship one item; this tool wires up every relevant Minecraft component on that item from the fields above.

Do not split one weapon idea across many `items[]` entries. Do not duplicate a weapon and call one copy "damage" and another "durability." That is the most common source of bloated, broken submissions.

##### Rule 2 — Every visible asset requires a texture

Items, blocks, entities, particles, named texture assets, machines, storage, and skin-pack skins must each carry a `texture` with one of these three sources:

* `source_base64` — base64-encoded PNG or JPEG bytes (max 1024×1024, max 5 MB).
* `source_file_id` — a File Manager file_id for a user-uploaded image.
* `color_hex` — an explicit `#RRGGBB` color. Only `item_kind in {tool, weapon}` (with `tool_type`) and the dedicated `texture_kind in {block, entity}` paths produce a recognizable sprite (sword/pickaxe/axe/shovel/hoe; shaded block face; humanoid silhouette). For every other kind — `generic`, `food`, `fuel`, `projectile`, `block_placer`, `entity_placer`, `armor`, particles, machines, storage — `color_hex` renders only as a flat colored 16×16 square. That is appropriate for raw materials (ingots, dust, gems) but looks like a missing texture for armor/food/machines. **Use `source_base64` or `source_file_id` whenever the item's identity is visual** (armor, food, machines, storage, projectiles). Tool/weapon `color_hex` requires `tool_type`; otherwise rejected.

A spec that omits the texture binding is rejected at validation with `MINECRAFT_VISIBLE_ASSET_TEXTURE_REQUIRED`. There is no procedural blob fallback. If you want the user to see something, you supply the texture.

**Armor pieces must ship a real PNG.** `item_kind="armor"` rejects `color_hex`-only textures (`MINECRAFT_ARMOR_TEXTURE_REQUIRES_IMAGE`) — the procedural sprite for armor is a flat colored square, which looks broken on the wearer model and in inventory. Supply `source_base64` or `source_file_id` for every helmet/chestplate/leggings/boots.

##### Authoring textures with the Icon Generator + `pixelize_to`

The canonical way to author textures for items, blocks, entities, and particles is the Icon Generator (`/product-icon-generator`). Render at the exact target grid in `pixel_art_mode=true` — 16×16 for items and blocks, 64×64 for entities and skin packs — and pipe the returned `file_id` straight into this texture's `source_file_id`. Detailed recipes live in `agent_instructions/minecraft_texture_agent.md`.

When the texture originates outside the Icon Generator (AI image creator, user upload, third-party source), use the ingest-side safety net by setting `texture.pixelize_to` and optionally `texture.palette_colors`. Both fields are opt-in (`None` by default) so existing bindings remain byte-identical. Example: `{"texture": {"source_file_id": "abc...", "pixelize_to": 16, "palette_colors": 8}}` nearest-neighbor downscales the input to 16×16 and quantizes it to an 8-color palette with dithering disabled, producing crisp pixel-art output regardless of how the source was made. Failures surface as `MINECRAFT_TEXTURE_PIXELIZE_FAILED`.

Recommended defaults unless you have a specific reason to deviate: items/blocks → `pixelize_to: 16, palette_colors: 8`; entities/skins → `pixelize_to: 64, palette_colors: 16`; particles → `pixelize_to: 16, palette_colors: 4`. The `color_hex` binding path is unaffected — it already produces crisp procedural sprites.

#### Request Shape Rules

Prefer the canonical field names below. The backend accepts the listed aliases when they are exact equivalents, but canonical names make the generated schema and validation errors easier to follow.

##### Creative world mechanics

Prank, cursed, chaotic, fake-glitch, admin, debug, and rule-bending ideas are valid requests when you express them as deterministic in-world mechanics. Use `features.events`, `features.commands`, conditions, scoreboards, tags, particles, sounds, titles, messages, gamerules, time/weather actions, block changes, explosions, lightning, and relative teleports. If a request sounds like a client or server modification, translate the user's intent into supported world-side behavior instead of refusing by label.

This deterministic builder does not generate arbitrary client mixins, shader loaders, native code, optimization core patches, or custom packet frameworks. Those are implementation boundaries; build the closest supported world mechanic when the user's goal can be represented with structured features.

##### Java client modules

Use `features.client_modules` for Java-only client utility behavior on `target_platform="fabric"` or `target_platform="neoforge"`. Bedrock and skin packs reject client modules because they cannot install Java client code.

Supported `module_kind` values:

* `utility_client_preset` — general anarchy/utility preset for requests phrased as "2b2t client", "anarchy client", or "hacked client"; emits FPS HUD, best-effort performance profile hooks, fullbright hooks, and TNT-cart placement scanning.
* `fps_hud` — HUD-only FPS display.
* `performance_profile` — FPS-oriented HUD plus best-effort client option hooks for render distance, simulation distance, entity distance scale, fast graphics, clouds off, and minimal particles.
* `tnt_cart_placement_esp` — client-side scanner for nearby rail blocks where TNT minecarts can be placed; renders a HUD count and nearest candidate coordinates.
* `block_esp` — bounded client scanner for listed block identifiers.
* `entity_esp` — bounded client scanner for listed entity identifiers.
* `fullbright` — best-effort client gamma option hook.
* `renderer_profile` — renderer metadata/guidance for `vanilla`, `iris_sodium`, `vulkanmod`, or `vulkanmod_beryl`.

Common aliases are accepted for `module_kind`: `hacked_client`, `anarchy_client`, `2b2t_client`, and `utility_client` normalize to `utility_client_preset`; `shizik`, `fps_boost`, and `optimization_client` normalize to `performance_profile`; `tnt_esp`, `tnt_cart_esp`, and `minecart_tnt_esp` normalize to `tnt_cart_placement_esp`; `iris_vulkan`, `iris_vulkan_hybrid`, and `iris_x_vulkanmod` normalize to `renderer_profile` with `renderer_profile="vulkanmod_beryl"` when no profile is provided.

Client-module options:

| field | Applies to | Notes |
|---|---|---|
| `scan_radius` | ESP modules | Horizontal scan radius, `4` to `64`; default `24`. |
| `update_interval_ticks` | all modules | Refresh interval, `1` to `200`; default `10`. |
| `max_rendered_markers` | ESP modules | Maximum retained HUD markers, `1` to `128`; default `32`. |
| `render_style` | ESP modules | Only `hud` is supported in this release; outline modes are rejected instead of ignored. |
| `color_hex` | all modules | HUD/overlay accent color; accepts the same color forms as textures. |
| `identifiers` | `block_esp`, `entity_esp` | Required list of block/entity ids to scan for. |
| `performance_mode` | `performance_profile`, `utility_client_preset` | `balanced`, `fps`, or `quality`; default `balanced`. |
| `max_render_distance` | performance modules | Best-effort render-distance option target, `2` to `32`; default `8`. |
| `max_simulation_distance` | performance modules | Best-effort simulation-distance option target, `2` to `32`; default `5`. |
| `entity_distance_scale` | performance modules | Best-effort entity render-distance scale, `0.1` to `1.0`; default `0.5`. |
| `renderer_profile` | `renderer_profile` | `vanilla`, `iris_sodium`, `vulkanmod`, or `vulkanmod_beryl`. |

Renderer profiles generate deterministic metadata, HUD labeling, and install guidance. They do **not** merge Iris and VulkanMod internals, inject native Vulkan code, or ship arbitrary renderer mixins. For an "Iris x VulkanMod hybrid" request, use `module_kind="renderer_profile"` with `renderer_profile="vulkanmod_beryl"` so the build succeeds and communicates the closest supported renderer setup.

Examples:

```json
{
  "client_modules": [
    {
      "module_id": "anarchy_utility",
      "display_name": "Anarchy Utility",
      "module_kind": "2b2t_client",
      "color_hex": "lime",
      "scan_radius": 32,
      "max_rendered_markers": 48
    }
  ]
}
```

```json
{
  "client_modules": [
    {
      "module_id": "shizik_profile",
      "display_name": "Shizik FPS Profile",
      "module_kind": "shizik",
      "performance_mode": "fps",
      "max_render_distance": 6,
      "max_simulation_distance": 4,
      "entity_distance_scale": 0.35
    }
  ]
}
```

```json
{
  "client_modules": [
    {
      "module_id": "renderer_bridge",
      "display_name": "Renderer Profile",
      "module_kind": "iris_x_vulkanmod"
    }
  ]
}
```

```json
{
  "client_modules": [
    {
      "module_id": "tnt_cart_spots",
      "display_name": "TNT Cart Placement ESP",
      "module_kind": "tnt_cart_placement_esp",
      "scan_radius": 48,
      "update_interval_ticks": 5,
      "max_rendered_markers": 64,
      "color_hex": "#ff3355"
    }
  ]
}
```

##### Versions, colors, and locales

Omit `minecraft_version` unless the user explicitly requires the pinned supported version. Each platform has one supported version in `list_capabilities`; unsupported older/newer versions are rejected instead of guessed. Whitespace is ignored, and `v` is accepted only when the remaining value exactly matches the pinned version.

Color fields (`color_hex`, `brand_color_hex`, `hover_text_color`, `map_color`, `default_color`) accept `#RRGGBB`, six-digit hex without `#`, three-digit short hex, or these color names: `black`, `white`, `red`, `green`, `blue`, `yellow`, `orange`, `purple`, `pink`, `brown`, `gray`, `grey`, `cyan`, `magenta`, `lime`, `gold`, `silver`. Values are normalized to lowercase `#rrggbb`.

Locales use `ll_RR`, such as `en_US`. Lowercase or hyphenated equivalents like `en_us`, `en-us`, and `en-US` are normalized.

##### Scoreboards, commands, functions, rarity

Use `objective_id` for scoreboards. Accepted aliases: `scoreboard_id`, `objective`. Use `criterion`; `criteria` is accepted.

Use `description` for commands. `display_name` is accepted as an alias when `description` is absent.

Functions may include optional `description` metadata. Use `lines`; `commands` is accepted as an alias when `lines` is absent.

Use `rarity.value` for item rarity. `rarity.rarity` and `rarity.name` are accepted aliases.

##### ActionSpec aliases

Every action uses `action_kind`. `particle_effect` and `spawn_particles` are accepted as `action_kind` aliases for `spawn_particle`.

Broadcast aliases are accepted for message/title actions: `broadcast_message`, `broadcast_chat`, `announce_message`, and `global_message` normalize to `send_message` with `audience="all_players"`; `broadcast_title`, `announce_title`, and `global_title` normalize to `show_title` with `audience="all_players"`.

When an action needs a target resource, prefer `identifier`. Accepted exact aliases:

| action_kind | Canonical field | Accepted aliases |
|---|---|---|
| `apply_effect`, `remove_effect` | `identifier` | `effect`, `effect_id` |
| `spawn_entity`, `set_entity_target` | `identifier` | `entity`, `entity_id` |
| `play_sound` | `identifier` | `sound`, `sound_id` |
| `spawn_particle` | `identifier` | `particle`, `particle_id` |
| `add_tag`, `remove_tag` | `identifier` | `tag`, `tag_id` |
| `give_item`, `drop_item` | `identifier` | `item`, `item_id` |
| `give_item`, `drop_item` | `value` | `count`, `amount` |
| `replace_held_item` | `identifier` | `item`, `item_id` |
| `apply_damage`, `heal` | `value` | `amount` |
| `set_block`, `place_block` | `identifier` | `block`, `block_id` |
| `set_scoreboard` | `identifier` | `objective`, `objective_id`, `scoreboard_id` |
| `set_scoreboard` | `value` | `score`, `amount`, `delta` |
| `award_advancement` | `identifier` | `advancement`, `advancement_id` |
| `modify_attribute` | `identifier` | `attribute`, `attribute_id` |
| `modify_attribute` | `value` | `amount`, `level` |
| `set_cooldown` | `identifier` | `cooldown`, `cooldown_id`, `cooldown_category` |
| `play_animation` | `identifier` | `animation`, `animation_id` |
| `change_dimension` | `identifier` | `dimension`, `dimension_id` |
| `run_command` | `command` | `command_line`, `minecraft_command` |
| `send_message`, `show_title` | `message` | `text`, `title` |
| `show_title` | `title_display` | `display` |
| `set_time` | `value` | `time`, `time_of_day` |
| `set_weather` | `identifier` | `weather`, `weather_id` |

##### Action options

Use these optional action fields only on the listed `action_kind`; unsupported combinations are rejected instead of ignored.

| action_kind | Supported options |
|---|---|
| `play_sound` | `volume` (`0` to `16`), `pitch` (`>0` to `4`), `position` |
| `spawn_particle` | `count` (`1` to `256`), `spread_x`, `spread_y`, `spread_z` (`0` to `16`), `position` |
| `spawn_entity`, `teleport`, `set_block`, `place_block`, `break_block_with_drops`, `create_explosion`, `summon_lightning` | `position` |
| `set_scoreboard` | `operation`: `set`, `add`, or `remove` |
| `send_message`, `show_title` | `audience`: `source` or `all_players` |
| `show_title` | `title_display`: `title`, `subtitle`, or `actionbar`; optional `fade_in_ticks`, `stay_ticks`, and `fade_out_ticks` together |
| `set_time` | `value`: `day`, `night`, `noon`, `midnight`, or an integer from `0` to `24000` |
| `set_weather` | `identifier`: `clear`, `rain`, or `thunder` |
| `apply_effect`, `set_on_fire`, `set_weather`, `wait` | `duration_ticks` (`1` to `72000` game ticks) |
| `apply_effect`, `apply_damage`, `heal`, `set_on_fire`, `add_tag`, `remove_tag` | `radius` (`>0` to `64`) and optional `radius_filter`: `all_entities`, `players`, `hostile_mobs`, or `non_player_entities` |
| any action | `chance_percent` (`>0` to `100`) |

`position` is always a relative offset from the event target or event block, never an absolute world coordinate. Send it as `{"x": x, "y": y, "z": z}` or `[x, y, z]` with integer coordinates from `-32` to `32`.

For `send_message` and `show_title`, `target` is accepted only as an audience alias when it is one of `source`, `self`, `player`, `@s`, `all`, `everyone`, `all_players`, `@a`, or `broadcast`. Use canonical `audience` in new requests.

For `give_item`, `drop_item`, `apply_damage`, and `heal`, any provided `value` or accepted value alias must be an integer `>= 1`.

For `set_scoreboard`, `operation` defaults to `set`. Use `add` to increment and `remove` to decrement; both require a positive integer `value` or accepted value alias. Use the opposite operation instead of negative deltas.

Use `wait` inside event or Script API command action lists to delay all following actions. Bedrock `.mcfunction` commands cannot express `wait` or `chance_percent`; use `simple_command` or `argument_command` for those.

##### Custom command parameters

Use `command_kind="argument_command"` with `parameters` for runtime command input. Parameter names are referenced in action `message` or `command` strings as `{param:name}`.

Supported `param_type` values are `string`, `integer`, `float`, and `player_name`. A `string` parameter is greedy text and must be last. Optional parameters must come after all required parameters. Example:

```json
{
  "commands": [
    {
      "command_id": "announce",
      "description": "Broadcast a title.",
      "command_kind": "argument_command",
      "permission_level": "op",
      "parameters": [{"name": "message", "param_type": "string"}],
      "actions": [
        {
          "action_kind": "show_title",
          "audience": "all_players",
          "title_display": "actionbar",
          "message": "{param:message}",
          "fade_in_ticks": 5,
          "stay_ticks": 60,
          "fade_out_ticks": 10
        }
      ]
    }
  ]
}
```

For `spawn_particle`, omitting `count` and spread fields preserves each platform generator's default particle behavior. Send explicit values when the count or spread matters.

##### ConditionSpec aliases

Every condition uses `condition_kind`. Prefer `identifier`; accepted exact aliases are `item`/`item_id` for `held_item`, `entity`/`entity_id` for `target_entity`, `block` for `block_id`, `biome` for `biome_id`, `tag`/`tag_id` for `has_tag`, and `objective`/`objective_id`/`scoreboard_id` for `score_at_least`. For `score_at_least`, `score` and `amount` are accepted aliases for `value`.

##### Condition value reference

- `entity_within_radius`: `value` is an integer radius from `1` to `64`; optional `identifier` filters the nearby entity type, for example `{"condition_kind":"entity_within_radius","identifier":"minecraft:player","value":12}`.
- `time_of_day`: `value` is one of `day`, `night`, `dawn`, `sunrise`, `morning`, `noon`, `dusk`, `sunset`, or `midnight`.
- `weather_is`: Java only; `identifier` is one of `clear`, `rain`, or `thunder`.
- `y_below` / `y_above`: `value` is an integer Y threshold from `-2048` to `2048`.
- `light_level_below`: Java only; `value` is an integer from `0` to `15`.

#### Recipes

Each recipe is a minimal copy-pasteable spec. Drop the recipe inside the `features` block of a `create_mod_project` request along with `target_platform`, `mod_id`, `mod_name`.

##### Recipe 1 — A diamond sword

```json
{
  "items": [
    {
      "item_id": "flame_sword",
      "display_name": "Flame Sword",
      "item_kind": "weapon",
      "tool_type": "sword",
      "tool_tier": "diamond",
      "damage": 7,
      "texture": {"color_hex": "#ff5522"}
    }
  ]
}
```

The validator confirms `item_kind="weapon"` with `tool_type="sword"`. The renderer expands `#ff5522` into a sword sprite. The item lands in the Equipment creative tab. Durability, repair material, enchantability, hand-equipped rendering, and the sword-tag default come from `tool_tier="diamond"`.

##### Recipe 2 — An iron pickaxe

```json
{
  "items": [
    {
      "item_id": "iron_pickaxe",
      "display_name": "Iron Pickaxe",
      "item_kind": "tool",
      "tool_type": "pickaxe",
      "tool_tier": "iron",
      "texture": {"color_hex": "#cccccc"}
    }
  ]
}
```

`tool_type="pickaxe"` is required: tools without `tool_type` are rejected because the icon and dig speed would be non-deterministic. Default damage/durability come from `tool_tier="iron"`. Substitute `axe`, `shovel`, or `hoe` for other vanilla tool kinds.

##### Recipe 3 — A custom-tier weapon

```json
{
  "items": [
    {
      "item_id": "void_blade",
      "display_name": "Void Blade",
      "item_kind": "weapon",
      "tool_type": "custom",
      "tool_tier": "custom",
      "damage": 12,
      "durability": 3000,
      "tool": {
        "tool_type": "custom",
        "tier": "custom",
        "attack_damage": 12,
        "attack_speed": 1.4
      },
      "repairable": {"repair_items": [{"item": "minecraft:netherite_ingot", "repair_amount": 50}]},
      "enchantable": {"slot": "sword", "value": 18},
      "texture": {"color_hex": "#2a0033"}
    }
  ]
}
```

Use `custom` to opt out of tier defaults. Declare `damage`, `durability`, `tool.attack_speed`, `repairable`, and `enchantable` explicitly.

##### Recipe 3b — A pickaxe that mines every block

```json
{
  "items": [
    {
      "item_id": "godpick",
      "display_name": "Godpick",
      "item_kind": "tool",
      "tool_type": "pickaxe",
      "tool_tier": "netherite",
      "tool": {
        "tool_type": "pickaxe",
        "tier": "netherite",
        "break_all_blocks": true,
        "instabreak": true
      },
      "texture": {"color_hex": "#ffd700"}
    }
  ]
}
```

`tool.break_all_blocks=true` tells the generator: this tool ignores the vanilla pickaxe/axe/shovel/hoe destructible tags and mines *every* block. Bedrock emits a Molang-true tag predicate on `minecraft:digger.destroy_speeds`; Java upgrades the tier to netherite so the tool's `INCORRECT_FOR` block tag is effectively empty. Pair with `instabreak: true` for one-shot mining.

##### Recipe 4 — A full diamond armor set

```json
{
  "items": [
    {"item_id": "set_helmet", "display_name": "Set Helmet", "item_kind": "armor", "tool_tier": "diamond", "armor": {"slot": "head",  "protection": 3, "toughness": 2}, "texture": {"source_base64": "<base64 PNG of the helmet icon>"}},
    {"item_id": "set_chest",  "display_name": "Set Chest",  "item_kind": "armor", "tool_tier": "diamond", "armor": {"slot": "chest", "protection": 8, "toughness": 2}, "texture": {"source_base64": "<base64 PNG of the chestplate icon>"}},
    {"item_id": "set_legs",   "display_name": "Set Legs",   "item_kind": "armor", "tool_tier": "diamond", "armor": {"slot": "legs",  "protection": 6, "toughness": 2}, "texture": {"source_base64": "<base64 PNG of the leggings icon>"}},
    {"item_id": "set_boots",  "display_name": "Set Boots",  "item_kind": "armor", "tool_tier": "diamond", "armor": {"slot": "feet",  "protection": 3, "toughness": 2}, "texture": {"source_base64": "<base64 PNG of the boots icon>"}}
  ]
}
```

One `ItemSpec` per armor slot. `armor.slot` is required: head/chest/legs/feet. `tool_tier` selects the vanilla armor material (sound, repair item, equipment asset); supply a real PNG — `color_hex` is rejected for armor with `MINECRAFT_ARMOR_TEXTURE_REQUIRES_IMAGE`.

##### Recipe 5 — A food item

```json
{
  "items": [
    {
      "item_id": "spicy_jerky",
      "display_name": "Spicy Jerky",
      "item_kind": "food",
      "food": {
        "nutrition": 7,
        "saturation_modifier": 0.6,
        "effects": [{"effect": "minecraft:fire_resistance", "chance": 1.0, "duration_seconds": 30, "amplifier": 0}]
      },
      "texture": {"color_hex": "#7a3a1a"}
    }
  ]
}
```

Pair `item_kind="food"` with the `food` preset. The food preset emits the eat animation, hunger restore, and any post-consumption effects.

##### Recipe 6 — A bow that fires arrows

```json
{
  "items": [
    {
      "item_id": "magic_arrow",
      "display_name": "Magic Arrow",
      "item_kind": "projectile",
      "projectile": {"projectile_entity": "minecraft:arrow"},
      "texture": {"color_hex": "#88aaff"}
    },
    {
      "item_id": "magic_bow",
      "display_name": "Magic Bow",
      "item_kind": "projectile",
      "shooter": {"charge_on_draw": true, "scale_power_by_draw_duration": true, "ammunition": ["modid:magic_arrow"], "max_draw_duration": 1.0},
      "texture": {"color_hex": "#552200"}
    }
  ]
}
```

Two items: one for the projectile, one for the launcher. Both carry `item_kind="projectile"`; the launcher has the `shooter` preset.

##### Recipe 7 — An ore plus its worldgen and drop

```json
{
  "blocks": [
    {
      "block_id": "ruby_ore",
      "display_name": "Ruby Ore",
      "block_kind": "ore",
      "hardness": 3.0,
      "resistance": 8.0,
      "drops": ["modid:ruby"],
      "texture": {"color_hex": "#c91140"}
    }
  ],
  "items": [
    {
      "item_id": "ruby",
      "display_name": "Ruby",
      "item_kind": "generic",
      "texture": {"color_hex": "#c91140"}
    }
  ],
  "worldgen": [
    {
      "feature_id": "ruby_ore_feature",
      "feature_kind": "ore_feature",
      "block_id": "ruby_ore",
      "target_block": "minecraft:stone",
      "vein_size": 6,
      "count_per_chunk": 4,
      "min_y": -32,
      "max_y": 48
    }
  ]
}
```

`drops` references an item id by namespace. The mined `ruby` is `item_kind="generic"` — it is a raw material that another recipe consumes; it does not need a tool/armor/food preset.

##### Recipe 8 — A hostile mob

```json
{
  "entities": [
    {
      "entity_id": "shadow_stalker",
      "display_name": "Shadow Stalker",
      "entity_kind": "hostile_mob",
      "health": 30,
      "attack_damage": 5,
      "movement_speed": 0.32,
      "spawn_biomes": ["minecraft:dark_forest", "minecraft:taiga"],
      "spawn_weight": 12,
      "texture": {"color_hex": "#1a1a2e"}
    }
  ]
}
```

The entity texture seeds both the mob model and the spawn-egg color. Bedrock additionally accepts `source_base64` or `source_file_id` to use a 64×64 PNG atlas.

##### Recipe 9 — A tameable pet

```json
{
  "entities": [
    {
      "entity_id": "stone_lynx",
      "display_name": "Stone Lynx",
      "entity_kind": "tameable_pet",
      "health": 20,
      "attack_damage": 4,
      "tameable": {"tame_items": ["minecraft:cooked_beef"], "probability": 0.5},
      "texture": {"color_hex": "#9d8866"}
    }
  ]
}
```

`entity_kind="tameable_pet"` plus the `tameable` preset enables the right-click-with-item taming flow.

##### Recipe 10 — A weapon that sets enemies on fire

```json
{
  "items": [
    {
      "item_id": "flame_sword",
      "display_name": "Flame Sword",
      "item_kind": "weapon",
      "tool_type": "sword",
      "tool_tier": "diamond",
      "damage": 8,
      "texture": {"color_hex": "#ff5522"}
    }
  ],
  "events": [
    {
      "event_id": "flame_sword_ignite",
      "event_kind": "on_item_hit_entity",
      "conditions": [{"condition_kind": "held_item", "identifier": "modid:flame_sword"}],
      "actions": [{"action_kind": "set_on_fire", "duration_ticks": 120}]
    }
  ]
}
```

One item, one event. The event filters by `held_item` (your sword's id) and emits `set_on_fire` against the hit entity. The event does *not* create a second item.

##### Recipe 11 — A skin pack with one skin

```json
{
  "action": "create_mod_project",
  "target_platform": "bedrock_skinpack",
  "mod_id": "blue_pack",
  "mod_name": "Blue Pack",
  "skin_pack": {
    "pack_id": "blue_pack",
    "display_name": "Blue Pack",
    "skins": [
      {
        "skin_id": "blue_hero",
        "display_name": "Blue Hero",
        "texture": {"source_base64": "<base64-encoded 64x64 PNG>"}
      }
    ]
  }
}
```

Skin pack textures must be exactly 64×64 PNG.

##### Recipe 12 — A cursed prank item

```json
{
  "items": [
    {
      "item_id": "cursed_stick",
      "display_name": "Cursed Stick",
      "item_kind": "generic",
      "texture": {"color_hex": "#7a35ff"}
    }
  ],
  "events": [
    {
      "event_id": "cursed_stick_use",
      "event_kind": "on_item_use",
      "conditions": [{"condition_kind": "held_item", "identifier": "cursed_stick"}],
      "actions": [
        {"action_kind": "spawn_particle", "identifier": "minecraft:basic_flame_particle", "count": 24, "spread_x": 2, "spread_y": 1, "spread_z": 2},
        {"action_kind": "play_sound", "identifier": "minecraft:block.note_block.pling", "volume": 1.5, "pitch": 0.5},
        {"action_kind": "show_title", "message": "Something moved.", "audience": "source"},
        {"action_kind": "teleport", "position": [0, 3, 0]}
      ]
    }
  ]
}
```

Use relative `position` for harmless movement effects. The item stays one `ItemSpec`; the event supplies the prank behavior.

##### Recipe 13 — A fake-glitch block event

```json
{
  "blocks": [
    {
      "block_id": "glitch_panel",
      "display_name": "Glitch Panel",
      "block_kind": "interactive",
      "texture": {"color_hex": "#00ffff"}
    }
  ],
  "events": [
    {
      "event_id": "glitch_panel_interact",
      "event_kind": "on_block_interact",
      "conditions": [{"condition_kind": "block_id", "identifier": "glitch_panel"}],
      "actions": [
        {"action_kind": "set_time", "time_of_day": "midnight"},
        {"action_kind": "set_weather", "weather": "thunder", "duration_ticks": 200},
        {"action_kind": "spawn_particle", "identifier": "minecraft:large_smoke", "count": 48, "spread_x": 3, "spread_y": 2, "spread_z": 3},
        {"action_kind": "broadcast_message", "text": "World state desynchronized."}
      ]
    }
  ]
}
```

Fake-glitch behavior should be built from world-side events, particles, titles/messages, time, weather, sounds, and block changes.

##### Recipe 14 — An admin debug command

```json
{
  "commands": [
    {
      "command_id": "debug_storm",
      "description": "Toggle a dramatic debug storm.",
      "command_kind": "admin_command",
      "permission_level": "admin",
      "actions": [
        {"action_kind": "set_gamerule", "identifier": "doDaylightCycle", "value": false},
        {"action_kind": "set_time", "value": "night"},
        {"action_kind": "set_weather", "identifier": "thunder", "duration_ticks": 600},
        {"action_kind": "send_message", "message": "Debug storm enabled.", "audience": "all_players"}
      ]
    }
  ]
}
```

Use `admin_command` plus `permission_level="admin"` for operator tools. Prefer `set_gamerule`, `set_time`, and `set_weather` over raw command strings when those first-class actions cover the behavior.

##### Recipe 15 — A chaos trap

```json
{
  "blocks": [
    {
      "block_id": "chaos_plate",
      "display_name": "Chaos Plate",
      "block_kind": "interactive",
      "texture": {"color_hex": "#ff00ff"}
    }
  ],
  "scoreboards": [{"objective_id": "chaos_triggers", "display_name": "Chaos Triggers"}],
  "events": [
    {
      "event_id": "chaos_plate_trigger",
      "event_kind": "on_block_interact",
      "conditions": [{"condition_kind": "block_id", "identifier": "chaos_plate"}],
      "actions": [
        {"action_kind": "set_block", "identifier": "minecraft:gold_block", "position": [0, -1, 0]},
        {"action_kind": "summon_lightning", "position": [2, 0, 0]},
        {"action_kind": "create_explosion", "value": 2, "position": [-2, 0, 0]},
        {"action_kind": "set_scoreboard", "identifier": "chaos_triggers", "operation": "add", "value": 1}
      ]
    }
  ]
}
```

Keep high-impact effects bounded with explicit values and relative positions so the generated behavior remains predictable.

##### Recipe 16 — Timed/random progression with milestones

```json
{
  "scoreboards": [{"objective_id": "weeks", "display_name": "Weeks"}],
  "events": [
    {
      "event_id": "weekly_progress",
      "event_kind": "on_player_tick",
      "interval_ticks": 1200,
      "cooldown_ticks": 1200,
      "chance_percent": 35,
      "actions": [
        {"action_kind": "set_scoreboard", "identifier": "weeks", "operation": "add", "value": 1},
        {"action_kind": "show_title", "audience": "source", "title_display": "actionbar", "message": "A week passes..."}
      ]
    }
  ]
}
```

Use scoreboards for staged progress. Use `interval_ticks` for cadence, `cooldown_ticks` to prevent repeated firing, and `chance_percent` for random outcomes.

##### Recipe 17 — A stalker entity with proximity behavior

```json
{
  "entities": [
    {
      "entity_id": "stalker",
      "display_name": "Stalker",
      "entity_kind": "hostile_mob",
      "health": 60,
      "movement_speed": 0.35,
      "scale": 2.5,
      "ai_goals": [
        {"goal_kind": "nearest_attackable_target", "priority": 1, "search_radius": 30},
        {"goal_kind": "melee_attack", "priority": 2, "speed_multiplier": 1.25, "attack_reach_multiplier": 2.0}
      ],
      "texture": {"color_hex": "#111111"}
    }
  ],
  "events": [
    {
      "event_id": "stalker_charge",
      "event_kind": "on_entity_tick",
      "interval_ticks": 20,
      "conditions": [{"condition_kind": "entity_within_radius", "identifier": "minecraft:player", "value": 12}],
      "actions": [
        {"action_kind": "wait", "duration_ticks": 20},
        {"action_kind": "apply_effect", "identifier": "minecraft:slowness", "duration_ticks": 80, "radius": 12, "radius_filter": "players"},
        {"action_kind": "spawn_particle", "identifier": "minecraft:basic_flame_particle", "count": 16, "spread_x": 1, "spread_y": 2, "spread_z": 1}
      ]
    }
  ]
}
```

`attack_reach_multiplier` is Bedrock-only. Fabric and NeoForge reject it with an actionable platform error; use `search_radius` and radius actions for cross-platform sensing.

##### Recipe 18 — A two-input machine

```json
{
  "items": [
    {"item_id": "amalgam", "display_name": "Amalgam", "texture": {"color_hex": "#b8f2ff"}}
  ],
  "machines": [
    {
      "machine_id": "amalgamator",
      "display_name": "Amalgamator",
      "texture": {"color_hex": "#606060"},
      "processing_time_ticks": 100,
      "machine_recipes": [
        {
          "recipe_id": "make_amalgam",
          "inputs": ["minecraft:iron_ingot", "minecraft:gold_ingot"],
          "output": "modid:amalgam",
          "output_count": 1
        }
      ]
    }
  ],
  "events": [
    {
      "event_id": "amalgamator_complete",
      "event_kind": "on_machine_recipe_complete",
      "actions": [{"action_kind": "broadcast_message", "text": "The amalgamator finished."}]
    }
  ]
}
```

Right-click the generated machine with each input item. Inputs are tracked per block position; when the full set is present, the output drops after `processing_time_ticks`.

#### Verify Every Generation

Always follow `create_mod_project` with a `render_preview_image` call against the just-generated `mod_id`. The preview confirms the icon renders correctly before you ask the user to install:

```json
{
  "action": "render_preview_image",
  "target_platform": "bedrock",
  "mod_id": "flame_tools",
  "mod_name": "Flame Tools",
  "preview_target_kind": "item",
  "preview_target_id": "flame_sword",
  "features": { /* same features block from create_mod_project */ }
}
```

If the preview looks like a flat colored square or the wrong tool sprite, you forgot `item_kind`, `tool_type`, or both.

#### Common Mistakes

Each entry pairs the failure mode with the structured error code the validator now returns. If you see the code, fix the spec.

| Mistake | What happens now |
|---|---|
| `item_kind="generic"` on a weapon with `damage` set | Rejected: `MINECRAFT_ITEM_KIND_REQUIRES_PRESET` |
| `item_kind="tool"` without `tool_type` | Rejected: `MINECRAFT_ITEM_KIND_REQUIRES_PRESET` |
| `item_kind="weapon"` with `tool_type="pickaxe"` | Rejected: weapon requires `sword` or `custom` |
| `item_kind="armor"` without `armor` or `wearable` | Rejected: `MINECRAFT_ITEM_KIND_REQUIRES_PRESET` |
| `item_kind="food"` without `food` preset or `nutrition` | Rejected: `MINECRAFT_ITEM_KIND_REQUIRES_PRESET` |
| `item_kind="block_placer"` without `block_placer` | Rejected: `MINECRAFT_ITEM_KIND_REQUIRES_PRESET` |
| `food` preset on an `item_kind="tool"` | Rejected: preset/kind mismatch |
| `texture` omitted on any visible asset | Rejected: `MINECRAFT_VISIBLE_ASSET_TEXTURE_REQUIRED` |
| `texture: {}` with no `color_hex`, `source_base64`, or `source_file_id` | Rejected: `MINECRAFT_TEXTURE_SOURCE_REQUIRED` |
| `item_kind="armor"` with `texture: {color_hex: ...}` only | Rejected: `MINECRAFT_ARMOR_TEXTURE_REQUIRES_IMAGE` |
| Pickaxe specced to "break any block" but only breaks a few | Add `tool.break_all_blocks: true` |
| Feature appears in the wrong platform build | Set `enabled_platforms: ["bedrock"]` (or fabric/neoforge) to scope it; an empty list applies to all platforms |
| Diamond/netherite armor looks/sounds/repairs like iron | Set `tool_tier: "diamond"` (or netherite); durability, enchant value, repair tag, and equip sound are derived from it |
| `recipe_kind="brewing_mix"` or `"brewing_container"` on Fabric/NeoForge | Rejected: brewing recipes are Bedrock-only. Use Bedrock or model the effect as a `crafting_shaped` recipe |
| Tool attack_speed left at the default 1.6 but the tool is a pickaxe | The Java side now derives the attack-speed delta per tool_type (sword -2.4, pickaxe -2.8, axe -3.1, shovel -3.0, hoe -1.0) so the swing animation matches vanilla; supply `tool.attack_speed` only if you want a non-vanilla swing rate |
| Block `drops` references an item id that doesn't exist | Rejected with `MINECRAFT_SPEC_VALIDATION_FAILED`. Define the dropped item under `features.items` or use a `minecraft:*` identifier |
| `recipe.result_item` / `block_placer` / `entity_placer` references a non-existent id | Rejected with `MINECRAFT_SPEC_VALIDATION_FAILED`. Same fix: define the target feature or use a `minecraft:*` identifier |
| Multiple `items[]` entries for one weapon (one for damage, one for enchant) | Two items in inventory; collapse to one ItemSpec |
| `on_item_hit_entity` without a `held_item` condition | Fires for every hit; add `{"condition_kind":"held_item","identifier":"modid:itemid"}` |
| `command_id` shadowing a Minecraft command (e.g. `give`, `tp`) | Reject or behavior conflict; pick a unique id |

#### Supported Platforms

- `bedrock`: Minecraft Bedrock add-on generation for pinned Mojang Bedrock Samples baseline `v1.26.20.4`. Produces source zips, `.mcaddon` installables, and Mojang Minecraft Creator Tools validation reports.
- `fabric`: Minecraft Java Fabric generation for pinned version `1.21.11`. Produces source zips and optional built jars using the pinned offline Gradle/Fabric toolchain.
- `neoforge`: Minecraft Java NeoForge generation for pinned Minecraft `1.21.11` and NeoForge `21.11.42`. Produces source zips and optional built jars using the pinned offline Gradle/NeoForge toolchain.
- `bedrock_skinpack`: Bedrock skin pack generation. Produces installable `.mcpack` files from skin texture images and localization/manifest metadata.
- `forge` is retired. Requests using `target_platform="forge"` are rejected with a structured migration error directing callers to `neoforge`.

#### Actions

##### `list_capabilities`

Return supported platforms, pinned dependencies, feature kinds, output artifacts, and platform notes.

Optional:
- `target_platform`: `bedrock`, `bedrock_skinpack`, `fabric`, or `neoforge`.

##### `validate_mod_project`

Validate either a structured mod specification or a source archive previously produced by this tool.

Modes:
- Spec validation: provide `target_platform`, `mod_id`, `mod_name`, and `features` (or `skin_pack` for skinpacks).
- Archive validation: provide `source_archive_file_id`.

##### `create_mod_project`

Generate mod artifacts and upload them to File Manager storage. Responses include artifact `file_id` values, signed URLs, generated file manifests, validation results, install instructions, warnings, and build reports.

Required:
- `target_platform`: `bedrock`, `bedrock_skinpack`, `fabric`, or `neoforge`.
- `mod_id`: lowercase identifier matching `^[a-z][a-z0-9_]{1,63}$`.
- `mod_name`: human-readable mod name.
- `features`: structured feature object for normal Bedrock/Fabric/NeoForge mods.
- `skin_pack`: structured skin pack object for `target_platform=bedrock_skinpack`.

Optional:
- `minecraft_version`: omit to use the pinned platform version.
- `description`: short mod description.
- `output_mode`: `installable`, `source`, or `both`. Default is `both`.
- `build_jar`: for Fabric/NeoForge only. Default is `true`.
- `validate_output`: run external platform validation where available. Default is `true`.
- `include_file_preview`: include capped text previews in `generated_files`.
- `allow_experimental_bedrock_features`: allow script-based Bedrock features that may require experiments.

##### `render_preview_image`

Render an enlarged PNG preview for an item, block, or entity texture and upload it to File Manager. Call this after every `create_mod_project` to confirm the icon looks right before installation.

Modes:
- Spec preview: provide `target_platform`, `mod_id`, `mod_name`, and `features`; the tool generates files in memory and previews the selected texture.
- Source archive preview: provide `source_archive_file_id` from a generated source zip; optionally include `mod_id`.
- Direct image preview: provide `preview_source_file_id` for a File Manager image uploaded by the user.

Optional:
- `preview_target_kind`: `item`, `block`, or `entity`.
- `preview_target_id`: feature id or namespaced id, such as `flame_sword` or `flame_tools:flame_sword`.
- `preview_size`: square preview PNG size from 32 to 1024 pixels. Default is 256.
- `preview_background`: `checkerboard`, `transparent`, `white`, or `black`. Default is `checkerboard`.

#### Field Reference

All feature arrays are optional. Use empty arrays or omit unused sections.

##### Texture binding (BindingTextureSpec)

Every visible asset's `texture` field is a `BindingTextureSpec`. Supply exactly one of:
- `source_base64`: base64-encoded image bytes (PNG or JPEG, max 1024 px, max 5 MB).
- `source_file_id`: File Manager file_id for a user-uploaded image.
- `color_hex`: explicit `#RRGGBB` color rendered as a kind-shaped procedural sprite.

`source_base64` and `source_file_id` are mutually exclusive. A spec with none of the three is rejected with `MINECRAFT_TEXTURE_SOURCE_REQUIRED`.

##### Items

- `item_id`: required lowercase identifier.
- `display_name`: required.
- `item_kind`: required behavior class (see Recipes). One of `generic`, `tool`, `weapon`, `armor`, `food`, `fuel`, `projectile`, `block_placer`, or `entity_placer`. Drives icon sprite, creative-tab placement, stack size, and required presets.
- `tool_type`: `pickaxe`, `axe`, `shovel`, `hoe`, `sword`, or `custom`. Required for `item_kind="tool"`; `weapon` requires `sword` or `custom`.
- `tool_tier`: `wood`, `stone`, `iron`, `gold`, `diamond`, `netherite`, or `custom`. Defaults to `iron`. Controls durability, attack damage, mining speed, enchantability, and repair material.
- `texture`: required BindingTextureSpec.
- `damage`, `durability`, `max_stack_size`, `nutrition`, `saturation`: per-field semantics; defaults derive from `item_kind`/`tool_tier`.
- `tool`, `armor`, `food`, `block_placer`, `entity_placer`, `projectile`, `shooter`, `throwable`: presets used by the matching `item_kind`. The validator rejects preset/kind mismatches with `MINECRAFT_ITEM_KIND_REQUIRES_PRESET`.
- `enchantable`, `repairable`, `digger`, `cooldown`, `use_modifiers`, `rarity`, `dyeable`, `glint`, `allow_off_hand`, `fire_resistant`, `hover_text_color`, `swing_sounds`, `component_overrides`, `custom_components`: optional component knobs that attach to the same item.

##### Blocks

- `block_id`: required lowercase identifier.
- `display_name`: required.
- `block_kind`: `basic`, `ore`, `light`, `interactive`, `crop`, `plant`, `redstone`, `machine`, or `container`.
- `texture`: required BindingTextureSpec.
- `hardness`, `resistance`, `light_level`, `drops`, `material_instances`, `collision_box`, `selection_box`, `placement_filter`, `flammable`, `friction`, `map_color`, `crop`, `redstone`, `tick`, `crafting_table`, `component_overrides`, `custom_components`.

##### Entities

- `entity_id`: required lowercase identifier.
- `display_name`: required.
- `entity_kind`: `passive_mob`, `hostile_mob`, `neutral_mob`, `projectile`, `npc_like`, `tameable_pet`, `rideable_mount`, or `boss_like`.
- `texture`: required BindingTextureSpec. Seeds both the mob model and the spawn-egg color.
- `health`, `attack_damage`, `movement_speed`, `spawn_biomes`, `spawn_weight`, `families`, `ai_goals`, `interactions`, `rideable`, `tameable`, `breedable`, `equipment`, `render`, `loot_table`, `component_overrides`.

##### Particles

- `particle_id`: required lowercase identifier.
- `texture`: required BindingTextureSpec.

##### Effects

- `effect_id`: required lowercase identifier.
- `display_name`: required.
- `effect_kind`: `apply_builtin_effect`, `custom_status_effect`, `scripted_timed_effect`, or `attribute_modifier_effect`.
- `color_hex`: optional `#RRGGBB`.
- `duration_ticks`, `amplifier`, `builtin_effect_id`.

Bedrock custom effects are simulated with built-in effects, tags, particles, attributes, and scripts. Fabric and NeoForge emit registered `MobEffect` subclasses with deterministic tick behavior.

##### Commands

- `command_id`: required lowercase identifier.
- `description`: required.
- `command_kind`: `simple_command`, `argument_command`, `function_command`, or `admin_command`.
- `permission_level`: `any`, `op`, or `admin`.
- `actions`: optional array of action specs.

##### Worldgen

- `feature_id`: required lowercase identifier.
- `feature_kind`: `ore_feature`, `single_block_feature`, `vegetation_patch`, `structure_placement`, `custom_biome`, or `custom_dimension`.
- `block_id`, `target_block` (default `minecraft:stone`), `vein_size`, `count_per_chunk`, `min_y`, `max_y`, `biomes`.

`min_y` must be less than or equal to `max_y`.

##### Recipes

- `recipe_id`: required lowercase identifier.
- `result_item`: required item identifier.
- `recipe_kind`: `shaped`, `shapeless`, `furnace`, `brewing_mix`, `brewing_container`, `smithing_transform`, or `smithing_trim`.
- `pattern`, `key`, `ingredients`, `count`, `cooking_time_seconds`, `input_item`, `template_item`, `base_item`, `addition_item`.

Java targets reject `brewing_mix` and `brewing_container` with `MINECRAFT_COMPONENT_UNSUPPORTED_ON_PLATFORM`; those recipe kinds are Bedrock-only.

##### Loot Tables

- `loot_id`: required lowercase identifier.
- `target`: required target entity/block identifier.
- `drops`: required array of item identifiers.

##### Events

- `event_id`: required lowercase identifier.
- `event_kind`: one of the supported kinds per platform (see Recipe 10).
- `conditions`: optional array of condition specs (`held_item`, `target_entity`, `source_entity`, `block_id`, `biome_id`, `has_tag`, `score_at_least`, `entity_within_radius`, `time_of_day`, `weather_is`, `y_below`, `y_above`; Java also supports `light_level_below`).
- Condition values: `entity_within_radius.value` is `1` to `64`; `time_of_day.value` is `day`, `night`, `dawn`, `sunrise`, `morning`, `noon`, `dusk`, `sunset`, or `midnight`; `weather_is.identifier` is Java-only `clear`, `rain`, or `thunder`; `y_below.value` and `y_above.value` are `-2048` to `2048`; `light_level_below.value` is Java-only `0` to `15`.
- `actions`: required non-empty array of action specs.
- `interval_ticks`: optional cadence for tick-style events (`on_player_tick`, `on_entity_tick`, `on_block_tick`, `on_enter_biome`, `on_item_inventory_tick`).
- `cooldown_ticks`: optional per-subject cooldown.
- `chance_percent`: optional whole-event random gate.
- `action_selection`: `all` or `random_one`.

`run_command` accepts a single Minecraft command line only. Shell-like syntax such as `&&`, `||`, backticks, `$()`, redirection, and shell/program names such as `bash`, `npm`, `gradle`, `java`, or `python` are rejected.

##### Machines and Storage

- `MachineSpec` requires `texture` (visible block face). `machine_kind`: `processor`, `generator`, `storage`, `tank`, or `transfer_endpoint`.
- `processing_time_ticks`: ticks between completing the input set and producing output. `processing_time` is accepted as an alias; `processing_time_seconds` is accepted when it converts to whole ticks.
- `machine_recipes`: inline machine recipes. Each recipe has `recipe_id`, `inputs` (1-9 item ids), `output`, and `output_count`.
- Machine recipes are interact-driven: right-click the machine with each required input item. The generated machine records pending inputs per block position, consumes matching inputs, waits `processing_time_ticks`, then drops the output item.
- `StorageSpec` requires `texture` (item icon for `backpack`, block face for the rest). `storage_kind`: `item_container`, `fluid_tank`, `energy_storage`, or `backpack`.

##### Skins

- `SkinPackSpec.skins[]` requires `skin_id`, `display_name`, and a 64×64 `texture`.

#### Output Behavior

- Bedrock `installable` or `both` returns a `.mcaddon` and validation report. With `validate_output=true`, Mojang Minecraft Creator Tools validates the generated add-on.
- Fabric/NeoForge `installable` or `both` returns a jar when `build_jar=true`; otherwise use `source` for source zips only.
- `render_preview_image` returns a `preview` artifact with a PNG `file_id`, signed URL, and image metadata. It previews texture/icon assets only; gameplay behavior still must be tested in Minecraft.
- Fabric/NeoForge entity specs emit registered `EntityType` definitions, per-kind generated entity subclasses, default attributes, spawn eggs, client renderer registrations, and loader-specific spawn/attribute hooks.
- Fabric worldgen specs emit data-pack configured/placed features plus Fabric biome modification hooks. NeoForge worldgen specs emit data-pack configured/placed features plus NeoForge biome modifier JSON.
- `on_item_hit_entity` event specs emit loader-specific attack-event handlers and execute supported Java action templates such as fire, damage, healing, effects, particles, sounds, tags, item grants/drops, entity spawns, and Minecraft commands.
- Java builds use the pinned offline Gradle cache inside the container. No dependency versions are chosen at runtime.
- Artifacts expire according to the File Manager storage policy. Store returned `file_id` values if another tool needs to retrieve or validate them later.

#### Maintenance

- Regenerate `minecraft_mods_service/bedrock_component_registry.json` after updating the pinned Mojang samples archive with `tools/regenerate_bedrock_component_registry.py`.
- Regenerate the public JSON schema after editing `minecraft_mods_service/models.py` with `tools/regenerate_public_tool_schema.py`. The regenerated artifact is written to two locations and checked for byte-equality by `test_schema_single_source.py`.

## When To Use
- Use this skill for `Minecraft Custom Mod Builder` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: minecraft custom mod builder, create installable minecraft bedrock add ons (.mcaddon) from a simple description, build java mods for fabric and neoforge and download the .jar, design custom swords, pickaxes, create mod project, target platform, mod id.
- Supported action names: `create_mod_project`, `list_capabilities`, `render_preview_image`, `validate_mod_project`.

## Use Cases
- Create installable Minecraft Bedrock add-ons (.mcaddon) from a simple description
- Build Java mods for Fabric and NeoForge and download the .jar
- Design custom swords
- pickaxes
- tools
- and armor with their own textures
- Add new blocks
- ores
- and crops with world generation
- Create custom mobs from passive animals to hostile bosses and tameable pets
- Make Bedrock skin packs (.mcpack) for a fresh character look
- Give items special behavior like a sword that sets enemies on fire
- Add custom crafting recipes
- loot tables
- enchantments
- and villager trades

## Related Product Skills
- File Management: ../file-management (ClawHub: `file-management`, page: https://clawhub.ai/agentpmt/file-management; skills.sh: `npx skills add AgentPMT/agent-skills --skill file-management`)

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `4`.
x402 availability: not enabled for this product.

- `create_mod_project` (action slug: `create-mod-project`): Generate installable Minecraft artifacts and upload them to File Manager. Supports Bedrock .mcaddon, Bedrock skin packs, Fabric jars/source, and NeoForge jars/source from structured specs. Supports deterministic world-side mechanics, scheduled/random events, cooldowns, radius conditions, custom commands with parameters, time/weather/title actions, scoreboards, particles/sounds, relative teleports, explosions, lightning, block changes, effects, tags, items, entities, machines, recipes, and Java client utility modules. Use render_preview_image when visual assets matter. Price: `25` credits. Parameters: `advanced_resources`, `allow_experimental_bedrock_features`, `assets`, `build_jar`, `compatibility_mode`, `description`, `features`, `include_file_preview`, plus 8 more.
- `list_capabilities` (action slug: `list-capabilities`): Return supported platforms, pinned versions, feature kinds, event kinds, action kinds, client module kinds, event options, condition kinds, action options, unsupported families, and the capability matrix. Use this before planning complex Java/Bedrock behavior. Price: `25` credits. Parameters: `target_platform`.
- `render_preview_image` (action slug: `render-preview-image`): Render and upload an enlarged PNG preview for an item, block, entity, texture, or generated source archive. Uses the same current structured feature contract as create_mod_project when previewing from a spec. Price: `25` credits. Parameters: `advanced_resources`, `allow_experimental_bedrock_features`, `assets`, `compatibility_mode`, `description`, `features`, `minecraft_version`, `mod_id`, plus 10 more.
- `validate_mod_project` (action slug: `validate-mod-project`): Validate a structured mod specification or source archive without writing artifacts. Use this before create_mod_project for complex specs, especially specs with events, client_modules, command parameters, machine recipes, radius conditions, or platform-specific behavior. Price: `25` credits. Parameters: `advanced_resources`, `allow_experimental_bedrock_features`, `assets`, `compatibility_mode`, `description`, `features`, `minecraft_version`, `mod_id`, plus 5 more.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "minecraft-custom-mod-builder"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "minecraft-custom-mod-builder"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "minecraft-custom-mod-builder"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "minecraft-custom-mod-builder"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "minecraft-custom-mod-builder"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "minecraft-custom-mod-builder"
  }
}
```

## Call This Tool
Product slug: `minecraft-custom-mod-builder`

Marketplace page: https://www.agentpmt.com/marketplace/minecraft-custom-mod-builder

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
    "name": "Minecraft-Custom-Mod-Builder",
    "arguments": {
      "action": "create_mod_project",
      "advanced_resources": [
        {}
      ],
      "allow_experimental_bedrock_features": false,
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
      "include_file_preview": false
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "minecraft-custom-mod-builder",
  "parameters": {
    "action": "create_mod_project",
    "advanced_resources": [
      {}
    ],
    "allow_experimental_bedrock_features": false,
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
    "include_file_preview": false
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `create_mod_project` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/minecraft-custom-mod-builder
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
