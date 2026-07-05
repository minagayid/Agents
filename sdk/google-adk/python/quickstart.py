"""Google Agent Development Kit (ADK) — Python quickstart.

Setup:
    pip install -r requirements.txt

    # Option A: Google AI Studio (Gemini API key)
    export GOOGLE_GENAI_USE_VERTEXAI=FALSE
    export GOOGLE_API_KEY="your-gemini-api-key"

    # Option B: Vertex AI
    #   export GOOGLE_GENAI_USE_VERTEXAI=TRUE
    #   export GOOGLE_CLOUD_PROJECT="your-project"
    #   export GOOGLE_CLOUD_LOCATION="us-central1"

Run this file directly:
    python quickstart.py

Or use the ADK dev tooling (expects an `agent.py` exposing `root_agent`):
    adk run .
    adk web

Docs: https://google.github.io/adk-docs/ · https://github.com/google/adk-python
"""

import asyncio

from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.genai import types


def get_weather(city: str) -> dict:
    """Return the current weather for a city.

    Args:
        city: The city to look up.
    """
    return {"status": "ok", "report": f"The weather in {city} is sunny, 24°C."}


# `root_agent` is the conventional name the ADK CLI (`adk run` / `adk web`) looks for.
root_agent = Agent(
    name="weather_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant. Use the get_weather tool when asked about weather.",
    description="Answers weather questions.",
    tools=[get_weather],
)


async def main() -> None:
    runner = InMemoryRunner(agent=root_agent, app_name="quickstart")
    session = await runner.session_service.create_session(
        app_name="quickstart", user_id="user"
    )
    content = types.Content(role="user", parts=[types.Part(text="Weather in Paris?")])
    async for event in runner.run_async(
        user_id="user", session_id=session.id, new_message=content
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(part.text)


if __name__ == "__main__":
    asyncio.run(main())
