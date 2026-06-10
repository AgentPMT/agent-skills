# Recent News Article Aggregator Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `recent-news-article-aggregator`

x402 availability: not enabled for this product.

## `search`

Action slug: `search`

Price: `10` credits

Search for news articles by topic, category, country, and language. Returns articles from multiple news sources with title, description, URL, image, source, and publication date.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `categories` | `array` | no | Include only articles in these categories. |
| `country` | `string` | no | Two-letter country code to filter news by region. Default: us. |
| `exclude_categories` | `array` | no | Exclude articles in these categories. |
| `language` | `string` | no | Language code for article language. Default: en. |
| `max_age_in_days` | `integer` | no | Limit results to articles published within the past N days. |
| `news_type` | `string` | no | Result scope: 'all_news' for broad results or 'top_stories' for major headlines only. Default: all_news. |
| `topic` | `string` | no | Search query for news articles. Supports operators: + (AND), \| (OR), - (NOT), quotes for exact phrases, * for prefix matching. |

Sample parameters:

```json
{
  "categories": [
    "general"
  ],
  "country": "us",
  "exclude_categories": [
    "general"
  ],
  "language": "en",
  "max_age_in_days": 1,
  "news_type": "all_news",
  "topic": "example topic"
}
```

Generated JSON parameter schema:

```json
{
  "categories": {
    "description": "Include only articles in these categories.",
    "items": {
      "enum": [
        "general",
        "science",
        "sports",
        "business",
        "health",
        "entertainment",
        "tech",
        "politics",
        "food",
        "travel"
      ],
      "type": "string"
    },
    "required": false,
    "type": "array"
  },
  "country": {
    "default": "us",
    "description": "Two-letter country code to filter news by region. Default: us.",
    "required": false,
    "type": "string"
  },
  "exclude_categories": {
    "description": "Exclude articles in these categories.",
    "items": {
      "enum": [
        "general",
        "science",
        "sports",
        "business",
        "health",
        "entertainment",
        "tech",
        "politics",
        "food",
        "travel"
      ],
      "type": "string"
    },
    "required": false,
    "type": "array"
  },
  "language": {
    "default": "en",
    "description": "Language code for article language. Default: en.",
    "required": false,
    "type": "string"
  },
  "max_age_in_days": {
    "description": "Limit results to articles published within the past N days.",
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "news_type": {
    "default": "all_news",
    "description": "Result scope: 'all_news' for broad results or 'top_stories' for major headlines only. Default: all_news.",
    "enum": [
      "top_stories",
      "all_news"
    ],
    "required": false,
    "type": "string"
  },
  "topic": {
    "description": "Search query for news articles. Supports operators: + (AND), | (OR), - (NOT), quotes for exact phrases, * for prefix matching.",
    "required": false,
    "type": "string"
  }
}
```
