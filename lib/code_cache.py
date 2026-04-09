"""Code cache for precompiled functions."""
import marshal
import types


def load_cached_function(path: str) -> types.FunctionType:
    """Load a precompiled function from cache."""
    with open(path, "rb") as f:
        code = marshal.load(f)
    return types.FunctionType(code, globals())
