from datetime import datetime, timezone


def get_current_iso_datetime():
    return datetime.now(timezone.utc).isoformat()
