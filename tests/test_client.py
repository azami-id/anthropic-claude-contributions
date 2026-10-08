from anthropic_claude_contributions import ClaudeClient, ClaudeClientConfig, build_message_prompt


def test_build_message_prompt_includes_system_and_user():
    result = build_message_prompt(
        user_prompt="Summarize this document.",
        system_prompt="You are a concise technical assistant.",
        examples=[{"prompt": "Explain AI.", "response": "AI is the simulation of intelligence."}],
    )

    assert "System:" in result
    assert "You are a concise technical assistant." in result
    assert "User:" in result
    assert "Summarize this document." in result
    assert "Example 1:" in result


def test_config_reads_from_environment(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    monkeypatch.setenv("ANTHROPIC_MODEL", "claude-3-5-sonnet")
    monkeypatch.setenv("ANTHROPIC_MAX_TOKENS", "2048")

    config = ClaudeClientConfig.from_env()

    assert config.api_key == "test-key"
    assert config.model == "claude-3-5-sonnet"
    assert config.max_tokens == 2048


def test_client_requires_api_key(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)

    client = ClaudeClient(ClaudeClientConfig(api_key=None))

    try:
        client.get_client()
    except ValueError:
        return

    raise AssertionError("Expected ValueError when API key is missing.")
