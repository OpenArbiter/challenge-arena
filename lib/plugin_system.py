"""Plugin system with dynamic module loading."""
import importlib
import json
from pathlib import Path


def load_plugins() -> list:
    """Load plugins specified in config."""
    config = json.loads(Path("config/plugins.json").read_text())
    plugins = []
    for entry in config.get("plugins", []):
        # Module path comes from config — could be anything
        mod = importlib.import_module(entry["module"])
        fn = getattr(mod, entry["function"])
        plugins.append(fn)
    return plugins
