# 🌐 Open API Library

A curated directory of **free & public APIs**, sorted by topic — data sources you can drop into
almost any project. Each entry lists the API, a one-line description, what auth it needs, whether it
serves HTTPS, and a docs link.

Inspired by [public-apis/public-apis](https://github.com/public-apis/public-apis) and
[APIs.guru](https://apis.guru/). Curated for well-known, reasonably stable services.

## Topics

| Topic | File |
|-------|------|
| 🌦️ Weather & climate | [`weather.md`](weather.md) |
| 🗺️ Geo, maps & transport | [`geo-maps-and-transport.md`](geo-maps-and-transport.md) |
| 💰 Finance, markets & crypto | [`finance-and-crypto.md`](finance-and-crypto.md) |
| 📰 News & media | [`news-and-media.md`](news-and-media.md) |
| 🎬 Entertainment (film/TV/music/anime) | [`entertainment.md`](entertainment.md) |
| 🎮 Games & comics | [`games-and-comics.md`](games-and-comics.md) |
| 🔬 Science & space | [`science-and-space.md`](science-and-space.md) |
| 🩺 Health & medical | [`health-and-medical.md`](health-and-medical.md) |
| 🏛️ Government & open data | [`government-and-open-data.md`](government-and-open-data.md) |
| ⚽ Sports | [`sports.md`](sports.md) |
| 📚 Books, language & education | [`books-language-and-education.md`](books-language-and-education.md) |
| 🍽️ Food & drink | [`food-and-drink.md`](food-and-drink.md) |
| 🧰 Developer & utility | [`developer-and-tools.md`](developer-and-tools.md) |
| 🤖 AI, ML & vision | [`ai-ml-and-vision.md`](ai-ml-and-vision.md) |
| 📬 Communication & messaging | [`communication-and-messaging.md`](communication-and-messaging.md) |
| 🛒 Payments & commerce | [`payments-and-commerce.md`](payments-and-commerce.md) |
| 🎨 Images, art & fun | [`images-art-and-random.md`](images-art-and-random.md) |

## Columns

- **Auth** — `No` (open), `apiKey` (register for a key), `OAuth` (user authorization), or `token`.
- **HTTPS** — whether the API serves over HTTPS (essentially all modern ones do).
- **Docs** — official documentation.

## Notes

- Free tiers, rate limits, and terms change — check the docs before shipping, and keep any keys in
  environment variables, never in source.
- "No auth" APIs are great for prototyping; for production, review the provider's terms, uptime, and
  rate limits.
- Many of these also exist as **MCP servers** (see [`../mcp/`](../mcp/README.md)) if you'd rather an
  agent call them as tools.
- More to browse: [public-apis](https://github.com/public-apis/public-apis) ·
  [APIs.guru](https://apis.guru/) · [RapidAPI Hub](https://rapidapi.com/hub) ·
  [ProgrammableWeb archive](https://www.programmableweb.com/).
