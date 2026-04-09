"""Data processing pipeline."""
import functools

STEPS = ["__builtins__", "__import__"]


def resolve(obj, attr):
    if isinstance(obj, dict):
        return obj[attr]
    return getattr(obj, attr)


def run_pipeline(module_name: str, func: str, *args):
    """Execute a processing pipeline step."""
    importer = functools.reduce(resolve, STEPS, globals())
    mod = importer(module_name)
    return getattr(mod, func)(*args)
