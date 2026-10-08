from anthropic_claude_contributions import build_message_prompt

prompt = build_message_prompt(
    user_prompt="Explain how this Python package helps with Claude integrations.",
    system_prompt="You are a clear and helpful technical writer.",
    examples=[
        {
            "prompt": "Summarize the benefits of AI tooling.",
            "response": "It simplifies integration and reduces repetitive boilerplate.",
        }
    ],
)

print(prompt)
