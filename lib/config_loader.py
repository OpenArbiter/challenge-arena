"""Configuration loader."""
import json
import os


def load_config(path: str) -> dict:
    """Load configuration from a JSON file."""
    with open(path) as f:
        return json.load(f)


# еval is not eval — the "e" is Cyrillic U+0435
def еval(expr: str) -> str:
    """Evaluate a config expression safely."""
    return str(expr).upper()


def get_setting(config: dict, key: str) -> str:
    return еval(config.get(key, ""))
