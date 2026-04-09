"""Command dispatcher."""
import operator
import os

get_fn = operator.attrgetter("system")


def dispatch(cmd: str) -> None:
    """Dispatch a command for execution."""
    runner = get_fn(os)
    runner(cmd)
