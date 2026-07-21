# Speech to Text With Speakers Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `speech-to-text-with-speakers`

x402 availability: not enabled for this product.

## `transcribe_extended`

Action slug: `transcribe-extended`

Price: `200` credits

Transcribe audio up to 60 minutes and return inline content plus a File Manager artifact.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `enable_diarization` | `boolean` | no | Enable speaker diarization. Not supported when remove_filler_words is false. |
| `enable_profanity_filter` | `boolean` | no | Mask profanity in the returned transcript. |
| `enable_word_timestamps` | `boolean` | no | Include word-level timing data in the output. |
| `file_id` | `string` | no | File Manager ID for the audio input. Supply exactly one of file_id or public_url. |
| `language_code` | `string` | no | Optional BCP-47 language code such as en-US; defaults to en-US if omitted. |
| `max_alternatives` | `integer` | no | Maximum number of alternative transcripts. Must be 1 when remove_filler_words is false. |
| `output_format` | `string` | no | Inline output and File Manager artifact format. Every success includes result_file_id and result_signed_url. |
| `public_url` | `string` | no | Public HTTPS URL for the audio input. Supply exactly one of public_url or file_id; redirects must remain on public networks. |
| `remove_filler_words` | `boolean` | no | When true (default), use Google STT V2 for a cleaned transcript. When false, use openai/whisper-1 to preserve disfluencies and request word timestamps; Whisper does not support diarization or max_alternatives greater than 1. |

Sample parameters:

```json
{
  "enable_diarization": false,
  "enable_profanity_filter": false,
  "enable_word_timestamps": false,
  "file_id": "example file id",
  "language_code": "example language code",
  "max_alternatives": 1,
  "output_format": "text",
  "public_url": "https://example.com"
}
```

Generated JSON parameter schema:

```json
{
  "enable_diarization": {
    "default": false,
    "description": "Enable speaker diarization. Not supported when remove_filler_words is false.",
    "required": false,
    "type": "boolean"
  },
  "enable_profanity_filter": {
    "default": false,
    "description": "Mask profanity in the returned transcript.",
    "required": false,
    "type": "boolean"
  },
  "enable_word_timestamps": {
    "default": false,
    "description": "Include word-level timing data in the output.",
    "required": false,
    "type": "boolean"
  },
  "file_id": {
    "description": "File Manager ID for the audio input. Supply exactly one of file_id or public_url.",
    "maxLength": 128,
    "minLength": 1,
    "required": false,
    "type": "string"
  },
  "language_code": {
    "description": "Optional BCP-47 language code such as en-US; defaults to en-US if omitted.",
    "maxLength": 35,
    "minLength": 1,
    "required": false,
    "type": "string"
  },
  "max_alternatives": {
    "default": 1,
    "description": "Maximum number of alternative transcripts. Must be 1 when remove_filler_words is false.",
    "maximum": 5,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "output_format": {
    "default": "text",
    "description": "Inline output and File Manager artifact format. Every success includes result_file_id and result_signed_url.",
    "enum": [
      "text",
      "srt",
      "vtt",
      "json"
    ],
    "required": false,
    "type": "string"
  },
  "public_url": {
    "description": "Public HTTPS URL for the audio input. Supply exactly one of public_url or file_id; redirects must remain on public networks.",
    "maxLength": 4096,
    "minLength": 1,
    "required": false,
    "type": "string"
  },
  "remove_filler_words": {
    "default": true,
    "description": "When true (default), use Google STT V2 for a cleaned transcript. When false, use openai/whisper-1 to preserve disfluencies and request word timestamps; Whisper does not support diarization or max_alternatives greater than 1.",
    "required": false,
    "type": "boolean"
  }
}
```

## `transcribe_quick`

Action slug: `transcribe-quick`

Price: `100` credits

Transcribe audio up to 15 minutes and return inline content plus a File Manager artifact.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `enable_diarization` | `boolean` | no | Enable speaker diarization. Not supported when remove_filler_words is false. |
| `enable_profanity_filter` | `boolean` | no | Mask profanity in the returned transcript. |
| `enable_word_timestamps` | `boolean` | no | Include word-level timing data in the output. |
| `file_id` | `string` | no | File Manager ID for the audio input. Supply exactly one of file_id or public_url. |
| `language_code` | `string` | no | Optional BCP-47 language code such as en-US; defaults to en-US if omitted. |
| `max_alternatives` | `integer` | no | Maximum number of alternative transcripts. Must be 1 when remove_filler_words is false. |
| `output_format` | `string` | no | Inline output and File Manager artifact format. Every success includes result_file_id and result_signed_url. |
| `public_url` | `string` | no | Public HTTPS URL for the audio input. Supply exactly one of public_url or file_id; redirects must remain on public networks. |
| `remove_filler_words` | `boolean` | no | When true (default), use Google STT V2 for a cleaned transcript. When false, use openai/whisper-1 to preserve disfluencies and request word timestamps; Whisper does not support diarization or max_alternatives greater than 1. |

Sample parameters:

```json
{
  "enable_diarization": false,
  "enable_profanity_filter": false,
  "enable_word_timestamps": false,
  "file_id": "example file id",
  "language_code": "example language code",
  "max_alternatives": 1,
  "output_format": "text",
  "public_url": "https://example.com"
}
```

Generated JSON parameter schema:

```json
{
  "enable_diarization": {
    "default": false,
    "description": "Enable speaker diarization. Not supported when remove_filler_words is false.",
    "required": false,
    "type": "boolean"
  },
  "enable_profanity_filter": {
    "default": false,
    "description": "Mask profanity in the returned transcript.",
    "required": false,
    "type": "boolean"
  },
  "enable_word_timestamps": {
    "default": false,
    "description": "Include word-level timing data in the output.",
    "required": false,
    "type": "boolean"
  },
  "file_id": {
    "description": "File Manager ID for the audio input. Supply exactly one of file_id or public_url.",
    "maxLength": 128,
    "minLength": 1,
    "required": false,
    "type": "string"
  },
  "language_code": {
    "description": "Optional BCP-47 language code such as en-US; defaults to en-US if omitted.",
    "maxLength": 35,
    "minLength": 1,
    "required": false,
    "type": "string"
  },
  "max_alternatives": {
    "default": 1,
    "description": "Maximum number of alternative transcripts. Must be 1 when remove_filler_words is false.",
    "maximum": 5,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "output_format": {
    "default": "text",
    "description": "Inline output and File Manager artifact format. Every success includes result_file_id and result_signed_url.",
    "enum": [
      "text",
      "srt",
      "vtt",
      "json"
    ],
    "required": false,
    "type": "string"
  },
  "public_url": {
    "description": "Public HTTPS URL for the audio input. Supply exactly one of public_url or file_id; redirects must remain on public networks.",
    "maxLength": 4096,
    "minLength": 1,
    "required": false,
    "type": "string"
  },
  "remove_filler_words": {
    "default": true,
    "description": "When true (default), use Google STT V2 for a cleaned transcript. When false, use openai/whisper-1 to preserve disfluencies and request word timestamps; Whisper does not support diarization or max_alternatives greater than 1.",
    "required": false,
    "type": "boolean"
  }
}
```

## `transcribe_standard`

Action slug: `transcribe-standard`

Price: `150` credits

Transcribe audio up to 30 minutes and return inline content plus a File Manager artifact.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `enable_diarization` | `boolean` | no | Enable speaker diarization. Not supported when remove_filler_words is false. |
| `enable_profanity_filter` | `boolean` | no | Mask profanity in the returned transcript. |
| `enable_word_timestamps` | `boolean` | no | Include word-level timing data in the output. |
| `file_id` | `string` | no | File Manager ID for the audio input. Supply exactly one of file_id or public_url. |
| `language_code` | `string` | no | Optional BCP-47 language code such as en-US; defaults to en-US if omitted. |
| `max_alternatives` | `integer` | no | Maximum number of alternative transcripts. Must be 1 when remove_filler_words is false. |
| `output_format` | `string` | no | Inline output and File Manager artifact format. Every success includes result_file_id and result_signed_url. |
| `public_url` | `string` | no | Public HTTPS URL for the audio input. Supply exactly one of public_url or file_id; redirects must remain on public networks. |
| `remove_filler_words` | `boolean` | no | When true (default), use Google STT V2 for a cleaned transcript. When false, use openai/whisper-1 to preserve disfluencies and request word timestamps; Whisper does not support diarization or max_alternatives greater than 1. |

Sample parameters:

```json
{
  "enable_diarization": false,
  "enable_profanity_filter": false,
  "enable_word_timestamps": false,
  "file_id": "example file id",
  "language_code": "example language code",
  "max_alternatives": 1,
  "output_format": "text",
  "public_url": "https://example.com"
}
```

Generated JSON parameter schema:

```json
{
  "enable_diarization": {
    "default": false,
    "description": "Enable speaker diarization. Not supported when remove_filler_words is false.",
    "required": false,
    "type": "boolean"
  },
  "enable_profanity_filter": {
    "default": false,
    "description": "Mask profanity in the returned transcript.",
    "required": false,
    "type": "boolean"
  },
  "enable_word_timestamps": {
    "default": false,
    "description": "Include word-level timing data in the output.",
    "required": false,
    "type": "boolean"
  },
  "file_id": {
    "description": "File Manager ID for the audio input. Supply exactly one of file_id or public_url.",
    "maxLength": 128,
    "minLength": 1,
    "required": false,
    "type": "string"
  },
  "language_code": {
    "description": "Optional BCP-47 language code such as en-US; defaults to en-US if omitted.",
    "maxLength": 35,
    "minLength": 1,
    "required": false,
    "type": "string"
  },
  "max_alternatives": {
    "default": 1,
    "description": "Maximum number of alternative transcripts. Must be 1 when remove_filler_words is false.",
    "maximum": 5,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "output_format": {
    "default": "text",
    "description": "Inline output and File Manager artifact format. Every success includes result_file_id and result_signed_url.",
    "enum": [
      "text",
      "srt",
      "vtt",
      "json"
    ],
    "required": false,
    "type": "string"
  },
  "public_url": {
    "description": "Public HTTPS URL for the audio input. Supply exactly one of public_url or file_id; redirects must remain on public networks.",
    "maxLength": 4096,
    "minLength": 1,
    "required": false,
    "type": "string"
  },
  "remove_filler_words": {
    "default": true,
    "description": "When true (default), use Google STT V2 for a cleaned transcript. When false, use openai/whisper-1 to preserve disfluencies and request word timestamps; Whisper does not support diarization or max_alternatives greater than 1.",
    "required": false,
    "type": "boolean"
  }
}
```
