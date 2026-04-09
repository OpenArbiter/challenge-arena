"""Client module."""
import subprocess
import os


def run_query(sql: str):
    return subprocess.run(["psql", "-c", sql], capture_output=True)


def get_config():
    return dict(os.environ)
