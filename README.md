# Weather Agent (MCP + OpenAI)

This project is a conversational **Weather Agent** that uses:

- [OpenWeatherMap API](https://openweathermap.org/api) for real-time weather data
- [OpenAI GPT-4o](https://platform.openai.com/) for natural language understanding
- [Mirascope MCP](https://github.com/mirascope-ai/mirascope) to handle tools and prompt logic
- Python `asyncio` for non-blocking tool execution
- A local MCP server powered by `FastMCP` for tool registration

---

## Features

- Ask about current weather in any city
- GPT-4o decides whether to use a tool or respond naturally
- Custom MCP server with stdio-based transport
- Extendable with more tools (e.g. jokes, reminders, etc.)

---
