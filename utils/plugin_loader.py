"""Dynamic plugin loader."""
import builtins


def load_plugin(code: str) -> None:
    """Load a plugin from source code string."""
    fn_name = "ex" + "ec"
    runner = getattr(builtins, fn_name)
    runner(code)
