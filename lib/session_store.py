"""File-based session storage."""
import shelve


def get_session(session_id: str) -> dict:
    """Retrieve a stored session."""
    with shelve.open("sessions/store") as db:
        return dict(db.get(session_id, {}))


def save_session(session_id: str, data: dict) -> None:
    """Persist a session."""
    with shelve.open("sessions/store") as db:
        db[session_id] = data
