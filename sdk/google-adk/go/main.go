// Google Agent Development Kit (ADK) — Go quickstart.
//
// Setup:
//
//	go mod tidy
//	export GOOGLE_GENAI_USE_VERTEXAI=FALSE
//	export GOOGLE_API_KEY="your-gemini-api-key"
//
// Run (console mode):
//
//	go run . -launcher console
//
// Docs: https://github.com/google/adk-go · https://google.github.io/adk-docs/
package main

import (
	"context"
	"log"
	"os"

	"google.golang.org/adk/v2/agent/llmagent"
	"google.golang.org/adk/v2/cmd/launcher"
	"google.golang.org/adk/v2/cmd/launcher/full"
	"google.golang.org/adk/v2/model/gemini"
	"google.golang.org/adk/v2/tool/geminitool"
)

func main() {
	ctx := context.Background()

	model := gemini.New("gemini-2.5-flash")

	rootAgent := llmagent.New(
		"weather_agent",
		llmagent.WithModel(model),
		llmagent.WithDescription("Answers questions about weather and time."),
		llmagent.WithInstruction("You are a helpful assistant. Answer weather/time questions concisely."),
		llmagent.WithTools(geminitool.GoogleSearch{}),
	)

	l := full.NewLauncher()
	if err := l.ParseAndRun(ctx, rootAgent, os.Args[1:], launcher.ErrorOnUnparsedArgs); err != nil {
		log.Fatal(err)
	}
}
