# Anthropic Claude Contributions

![CI](https://github.com/azami-id/anthropic-claude-contributions/actions/workflows/ci.yml/badge.svg)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-green)

A lightweight Python toolkit for building Claude-powered applications with a clean, minimal, and production-minded API.

This repository is designed as a practical foundation for:

- Claude API clients
- prompt composition helpers
- environment-based configuration
- reusable AI workflow utilities
- contributor-friendly open-source experimentation

## Why this project exists

Many Python integrations with Claude start from scratch. This project gives you a simple and readable starting point to:

- initialize a Claude client quickly
- keep prompt-building logic clean and reusable
- manage model and token settings with environment variables
- structure a small Python package in a maintainable way

## Installation

For local development:

```bash
git clone https://github.com/azami-id/anthropic-claude-contributions.git
cd anthropic-claude-contributions
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## Quick start

```python
from anthropic_claude_contributions import ClaudeClient, ClaudeClientConfig

config = ClaudeClientConfig(
    model="claude-3-5-sonnet-20241022",
    api_key="your_api_key_here",
    max_tokens=500,
)

client = ClaudeClient(config)
response = client.create_message(
    prompt="Summarize this issue in three bullet points.",
    system_prompt="You are a concise technical assistant.",
)

print(client.extract_text(response))
```

## Environment variables

Create a `.env` file or copy `.env.example`:

```bash
cp .env.example .env
```

Example values:

```bash
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
ANTHROPIC_MAX_TOKENS=1024
```

## Project structure

```text
.
├── .github/
│   └── workflows/
├── examples/
├── src/
│   └── anthropic_claude_contributions/
├── tests/
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── pyproject.toml
└── pytest.ini
```

## Features

- minimal Anthropic client wrapper
- prompt builder for reusable interactions
- environment-based configuration
- Python packaging via `pyproject.toml`
- CI validation across Python 3.10, 3.11, and 3.12
- contribution-friendly structure

## Roadmap

- add more workflow helpers
- provide structured output parsing utilities
- add example integrations for docs, summarization, and Q&A
- improve typing, validation, and error handling
- add release automation and semantic versioning

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Security

Please review [SECURITY.md](SECURITY.md) before reporting vulnerabilities or handling secrets.

## License

This project is licensed under the Apache License 2.0.
