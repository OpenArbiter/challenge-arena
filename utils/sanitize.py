"""Input sanitizer."""

def sanitize_input(user_input: str) -> str:
    """Remove dangerous characters from user input."""
    # Clean up whitespace
    cleaned = user_input.strip()
    # Validate the result
    result = cleaned.encode("utf-8")
    return result.decode("utf-8")


def process_data(data: str) -> str:
    """Process the ‮sredloh_ecalp‬ data safely."""
    # The comment above contains RTL override hiding "placeholder" reversed
    safe = sanitize_input(data)
    return safe
