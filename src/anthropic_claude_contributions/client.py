from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any


def build_message_prompt(
    user_prompt: str,
    system_prompt: str | None = None,
    examples: list[dict[str, str]] | None = None,
) -> str:
    """Build a readable prompt payload for Claude-based workflows."""
    if not user_prompt or not user_prompt.strip():
        raise ValueError("user_prompt must not be empty.")

    blocks: list[str] = []

    if system_prompt and system_prompt.strip():
        blocks.append(f"System:\n{system_prompt.strip()}")

    if examples:
        example_lines = []
        for index, example in enumerate(examples, start=1):
            prompt = example.get("prompt", "").strip()
            response = example.get("response", "").strip()
            if prompt and response:
                example_lines.append(f"Example {index}:\nPrompt: {prompt}\nResponse: {response}")
        if example_lines:
            blocks.append("Examples:\n" + "\n\n".join(example_lines))

    blocks.append(f"User:\n{user_prompt.strip()}")
    return "\n\n".join(blocks)


@dataclass
class ClaudeClientConfig:
    """Configuration for Claude API use and client setup."""

    model: str = "claude-3-5-sonnet-20241022"
    api_key: str | None = None
    max_tokens: int = 1024
    base_url: str | None = None

    @classmethod
    def from_env(cls) -> "ClaudeClientConfig":
        return cls(
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            model=os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022"),
            max_tokens=int(os.getenv("ANTHROPIC_MAX_TOKENS", "1024")),
            base_url=os.getenv("ANTHROPIC_BASE_URL"),
        )


class ClaudeClient:
    """Thin wrapper around the Anthropic Python SDK for common Claude tasks."""

    def __init__(self, config: ClaudeClientConfig | None = None):
        self.config = config or ClaudeClientConfig.from_env()
        self._client: Any | None = None

    def get_client(self) -> Any:
        """Return an authenticated Anthropic client instance."""
        if self._client is not None:
            return self._client

        try:
            from anthropic import Anthropic
        except ImportError as exc:  # pragma: no cover - dependency path
            raise RuntimeError(
                "Anthropic SDK is required. Install it with `pip install anthropic`."
            ) from exc

        api_key = self.config.api_key or os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "An Anthropic API key is required. Set ANTHROPIC_API_KEY or pass api_key in ClaudeClientConfig."
            )

        self._client = Anthropic(api_key=api_key, base_url=self.config.base_url)
        return self._client

    def create_message(
        self,
        prompt: str,
        system_prompt: str | None = None,
        **kwargs: Any,
    ) -> Any:
        """Create a simple Claude message request."""
        client = self.get_client()

        response = client.messages.create(
            model=kwargs.pop("model", self.config.model),
            max_tokens=kwargs.pop("max_tokens", self.config.max_tokens),
            system=system_prompt,
            messages=[{"role": "user", "content": prompt}],
            **kwargs,
        )
        return response

    def extract_text(self, response: Any) -> str:
        """Extract the text content from a Claude response object."""
        if hasattr(response, "content"):
            content = response.content
            if isinstance(content, list) and content:
                first_item = content[0]
                if hasattr(first_item, "text"):
                    return first_item.text
                if isinstance(first_item, dict):
                    return str(first_item.get("text", ""))
        return str(response)
