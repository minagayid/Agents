/**
 * Claude Agent SDK — TypeScript quickstart.
 *
 * Setup:
 *   npm install
 *   export ANTHROPIC_API_KEY="sk-ant-..."
 *
 * Run:
 *   npx tsx quickstart.ts
 *
 * Docs: https://github.com/anthropics/claude-agent-sdk-typescript
 */

import { query } from "@anthropic-ai/claude-agent-sdk";

// 1) Simplest possible call: async-iterate the streamed messages.
async function basicQuery(): Promise<void> {
  for await (const message of query({
    prompt: "What is 2 + 2? Answer in one word.",
  })) {
    console.log(message);
  }
}

// 2) With options: a system prompt and an allow-list of built-in tools.
async function withOptions(): Promise<void> {
  for await (const message of query({
    prompt: "Create a file called hello.txt containing 'hi', then read it back.",
    options: {
      systemPrompt: "You are a concise coding assistant.",
      allowedTools: ["Read", "Write", "Bash"],
    },
  })) {
    console.log(message);
  }
}

async function main(): Promise<void> {
  console.log("=== basicQuery ===");
  await basicQuery();
  console.log("\n=== withOptions ===");
  await withOptions();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
