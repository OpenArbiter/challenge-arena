"""Data loading utilities."""
import pickle
from pathlib import Path


def load_model(path: str) -> object:
    """Load a trained model from disk."""
    with open(path, "rb") as f:
        return pickle.load(f)  # Arbitrary code execution on load


def load_cache(cache_dir: str) -> dict:
    """Load cached results."""
    results = {}
    for p in Path(cache_dir).glob("*.pkl"):
        results[p.stem] = pickle.load(p.open("rb"))
    return results
