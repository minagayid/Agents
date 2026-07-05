# Google ADK — Go starter

Adapted from the official [`examples/quickstart`](https://github.com/google/adk-go/tree/main/examples/quickstart).

```bash
go mod tidy
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
export GOOGLE_API_KEY="your-gemini-api-key"
go run . -launcher console
```

The module path is `google.golang.org/adk/v2`. Run `go mod tidy` to resolve exact versions.

> The launcher/agent constructor options evolve between ADK releases — if a symbol doesn't
> resolve, check the current [examples/quickstart/main.go](https://github.com/google/adk-go/blob/main/examples/quickstart/main.go)
> and adjust. Other launchers: `-launcher restapi`, `-launcher webui`, `-launcher a2a`.
