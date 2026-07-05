/**
 * OpenAI Agents SDK — TypeScript quickstart.
 *
 * Setup:
 *   npm install
 *   export OPENAI_API_KEY="sk-..."
 *
 * Run:
 *   npx tsx quickstart.ts
 *
 * Docs: https://github.com/openai/openai-agents-js
 */

import { Agent, run, tool } from "@openai/agents";
import { z } from "zod";

// A schema-validated function tool.
const getWeather = tool({
  name: "get_weather",
  description: "Return the current weather for a city.",
  parameters: z.object({ city: z.string() }),
  execute: async ({ city }) => `The weather in ${city} is sunny, 24°C.`,
});

const agent = new Agent({
  name: "Assistant",
  instructions: "You are a friendly assistant. Use tools when relevant and be concise.",
  tools: [getWeather],
});

async function main(): Promise<void> {
  const result = await run(agent, "What's the weather in Tokyo?");
  console.log(result.finalOutput);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
