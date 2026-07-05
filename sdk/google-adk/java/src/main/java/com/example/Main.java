package com.example;

import com.google.adk.agents.LlmAgent;
import com.google.adk.tools.GoogleSearchTool;

/**
 * Google Agent Development Kit (ADK) — Java quickstart.
 *
 * <p>Setup:
 * <pre>
 *   export GOOGLE_GENAI_USE_VERTEXAI=FALSE
 *   export GOOGLE_API_KEY="your-gemini-api-key"
 *   mvn -q compile
 * </pre>
 *
 * <p>Prefer the ADK dev UI to interact with the agent:
 * <pre>
 *   mvn exec:java -Dexec.mainClass="com.google.adk.web.AdkWebServer"
 * </pre>
 *
 * Docs: https://github.com/google/adk-java · https://google.github.io/adk-docs/
 */
public class Main {

  // The ADK Web/CLI discovers a public static agent named `ROOT_AGENT`.
  public static final LlmAgent ROOT_AGENT =
      LlmAgent.builder()
          .name("search_assistant")
          .description("An assistant that can search the web.")
          .model("gemini-2.5-flash")
          .instruction(
              "You are a helpful assistant. Answer user questions using Google Search when needed.")
          .tools(new GoogleSearchTool())
          .build();

  public static void main(String[] args) {
    System.out.println("Defined ADK agent: " + ROOT_AGENT.name());
    System.out.println(
        "Run the ADK web UI to chat with it: "
            + "mvn exec:java -Dexec.mainClass=\"com.google.adk.web.AdkWebServer\"");
  }
}
