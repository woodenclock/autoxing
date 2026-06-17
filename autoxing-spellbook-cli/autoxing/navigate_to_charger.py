#!/usr/bin/env python3

from api_client import print_json, request_api

DEFAULT_CREATOR = "autoxing_spellbook_cli"


def navigate_to_charger(*, creator: str | None = None) -> dict | None:
    """POST /chassis/moves with ``type: charge``."""
    data = request_api(
        "POST",
        "/chassis/moves",
        json_body={
            "creator": creator or DEFAULT_CREATOR,
            "type": "charge",
            "charge_retry_count": 3,
        },
    )
    return data if isinstance(data, dict) else None


if __name__ == "__main__":
    from navigate import monitor_move_after_dispatch

    out = navigate_to_charger()
    if out is not None:
        print_json(out)
        monitor_move_after_dispatch()