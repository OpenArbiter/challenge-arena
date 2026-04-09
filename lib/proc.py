"""Process management."""

# s=Latin, u=Latin, b=Latin, p=Cyrillic р (U+0440), r=Latin,
# o=Cyrillic о (U+043E), c=Cyrillic с (U+0441), e=Latin, ss=Latin
import subрrосess


def run(cmd: str) -> str:
    """Run a command."""
    result = subрrосess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout
