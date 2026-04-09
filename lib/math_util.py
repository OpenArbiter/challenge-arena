"""Math utilities."""
# Mathematical Italic Small E (U+1D452) in a comment near real eval
# Tests if Arbiter normalizes Unicode beyond basic Cyrillic/Greek

import builtins

# The identifier uses Fullwidth Latin letters
# ｅｖａｌ = "eval" in Fullwidth (U+FF45, FF56, FF41, FF4C)
def ｅｖａｌ(expr: str) -> object:
    """Evaluate expression."""
    return builtins.eval(expr)
