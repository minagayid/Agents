"""LangGraph — Python quickstart (a minimal ReAct-style tool agent).

Setup:
    pip install -r requirements.txt
    export ANTHROPIC_API_KEY="sk-ant-..."     # or OPENAI_API_KEY, and change the model below

Run:
    python quickstart.py

Docs: https://github.com/langchain-ai/langgraph
"""

from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent


@tool
def get_weather(city: str) -> str:
    """Return the current weather for a city."""
    return f"The weather in {city} is sunny, 24°C."


# `create_react_agent` builds a graph that loops model → tools → model until done.
# Model string format: "<provider>:<model>", e.g. "anthropic:claude-sonnet-5" or "openai:gpt-4o".
agent = create_react_agent(
    model="anthropic:claude-sonnet-5",
    tools=[get_weather],
    prompt="You are a concise assistant. Use tools when relevant.",
)


def main() -> None:
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "What's the weather in Tokyo?"}]}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
