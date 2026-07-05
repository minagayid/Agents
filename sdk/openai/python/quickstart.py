"""OpenAI Agents SDK — Python quickstart.

Setup:
    pip install -r requirements.txt
    export OPENAI_API_KEY="sk-..."

Run:
    python quickstart.py

Docs: https://github.com/openai/openai-agents-python
"""

import asyncio

from agents import Agent, Runner, function_tool


# 1) A function tool. Name comes from the function; description from the docstring.
@function_tool
def get_weather(city: str) -> str:
    """Return the current weather for a city.

    Args:
        city: The city to look up.
    """
    return f"The weather in {city} is sunny, 24°C."


# 2) An agent configured with instructions and the tool above.
agent = Agent(
    name="Assistant",
    instructions="You are a friendly assistant. Use tools when relevant and be concise.",
    tools=[get_weather],
)


async def main() -> None:
    # Async run (preferred). Runner.run_sync(...) exists for non-async callers.
    result = await Runner.run(agent, "What's the weather in Tokyo?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
