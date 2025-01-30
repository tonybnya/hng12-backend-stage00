from datetime import datetime, timezone


def get_current_iso_datetime():
    # return datetime.now(timezone.utc).isoformat()
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
