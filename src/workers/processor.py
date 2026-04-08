"""Message processor worker."""
import json
import logging

logger = logging.getLogger(__name__)

def process_message(message: dict) -> dict:
    """Process a single message and return result."""
    msg_type = message.get("type", "unknown")
    payload = message.get("payload", {})
    
    if msg_type == "transform":
        return {"status": "ok", "result": transform(payload)}
    elif msg_type == "validate":
        return {"status": "ok", "valid": validate(payload)}
    else:
        return {"status": "error", "message": f"unknown type: {msg_type}"}

def transform(data: dict) -> dict:
    return {k.upper(): v for k, v in data.items()}

def validate(data: dict) -> bool:
    required = ["name", "email"]
    return all(k in data for k in required)
