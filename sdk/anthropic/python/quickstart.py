"""Claude Agent SDK — Python quickstart.

Setup:
    pip install -r requirements.txt
    export ANTHROPIC_API_KEY="sk-ant-..."

Run:
    python quickstart.py

Requires Python 3.10+. The SDK bundles Claude Code automatically.
Docs: https://github.com/anthropics/claude-agent-sdk-python
"""

import anyio

from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    query,
    tool,
    create_sdk_mcp_server,
)


# 1) Simplest possible call: stream messages from a one-shot query.
async def basic_query() -> None:
    async for message in query(prompt="What is 2 + 2? Answer in one word."):
        print(message)


# 2) A custom in-process tool exposed to the agent via an SDK MCP server.
@tool("add", "Add two numbers", {"a": float, "b": float})
async def add(args: dict) -> dict:
    result = args["a"] + args["b"]
    return {"content": [{"type": "text", "text": f"{result}"}]}


calculator = create_sdk_mcp_server(name="calculator", version="1.0.0", tools=[add])


# 3) Configure options: system prompt, allowed built-in tools, and our custom tool.
async def with_tools() -> None:
    options = ClaudeAgentOptions(
        system_prompt="You are a concise assistant. Use tools when they help.",
        allowed_tools=["Read", "Write", "Bash", "mcp__calculator__add"],
        mcp_servers={"calculator": calculator},
    )
    async with ClaudeSDKClient(options=options) as client:
        await client.query("Use the add tool to compute 17 + 25, then explain briefly.")
        async for msg in client.receive_response():
            print(msg)


async def main() -> None:
    print("=== basic_query ===")
    await basic_query()
    print("\n=== with_tools ===")
    await with_tools()


if __name__ == "__main__":
    anyio.run(main)
