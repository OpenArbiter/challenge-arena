"""Configuration loader."""
import yaml


def load_config(path: str) -> dict:
    """Load YAML configuration file."""
    with open(path) as f:
        # yaml.Loader allows arbitrary Python object construction
        # !!python/object/apply:os.system ["id"]
        return yaml.load(f, Loader=yaml.Loader)
