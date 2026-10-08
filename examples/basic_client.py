from anthropic_claude_contributions import ClaudeClient, ClaudeClientConfig


config = ClaudeClientConfig(
    model="claude-3-5-sonnet-20241022",
    api_key="your_api_key_here",
    max_tokens=400,
)

client = ClaudeClient(config)
response = client.create_message(
    prompt="Write a short overview of this repository in 3 bullet points.",
    system_prompt="You are a useful technical assistant.",
)

print(client.extract_text(response))
