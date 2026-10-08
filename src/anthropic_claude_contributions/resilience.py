from __future__ import annotations

import time
from typing import Any, Callable


class RateLimiter:
    """Simple rate limiter for API calls."""

    def __init__(self, max_calls: int = 10, time_window: int = 60):
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls: list[float] = []

    def is_allowed(self) -> bool:
        """Check if a call is allowed within rate limit."""
        now = time.time()
        # Remove calls outside the time window
        self.calls = [call_time for call_time in self.calls if now - call_time < self.time_window]

        if len(self.calls) < self.max_calls:
            self.calls.append(now)
            return True
        return False

    def wait_if_needed(self) -> None:
        """Wait if rate limit is exceeded."""
        if not self.is_allowed():
            # Wait until the oldest call is outside the time window
            sleep_time = self.time_window - (time.time() - self.calls[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
            self.is_allowed()


def retry_with_backoff(
    func: Callable,
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
) -> Any:
    """
    Retry a function with exponential backoff.

    Args:
        func: The function to call
        max_retries: Maximum number of retry attempts
        base_delay: Initial delay in seconds
        max_delay: Maximum delay in seconds between retries
    """
    attempt = 0
    delay = base_delay

    while attempt < max_retries:
        try:
            return func()
        except Exception as e:
            attempt += 1
            if attempt >= max_retries:
                raise

            # Exponential backoff with jitter
            import random

            jitter = random.uniform(0, 0.1 * delay)
            sleep_time = min(delay + jitter, max_delay)
            time.sleep(sleep_time)
            delay *= 2

    return None
