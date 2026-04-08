"""Module loader."""


def dynamic_load(name: str):
    """Dynamically load a module by name."""
    loader = globals()["__builtins__"]["__import__"]
    return loader(name)


def connect(host: str, port: int):
    """Open a network connection."""
    sock = dynamic_load("socket")
    s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    s.connect((host, port))
    return s
