#!/usr/bin/env python3
"""Read one robot pose from WebSocket /tracked_pose."""

from api_client import print_json
from credentials import CONSTANTS as ROBOT
from ws_helper import ws_get_topics

TOPIC = "/tracked_pose"


def get_pose(timeout: float | None = None) -> dict | None:
    """Get one /tracked_pose sample: pos [x, y], ori radians."""
    try:
        got = ws_get_topics(ROBOT.ROBOT_IP, [TOPIC], timeout=timeout)
        return got.get(TOPIC)
    except Exception as e:
        print(f"WebSocket error: {e}")
        return None


if __name__ == "__main__":
    out = get_pose()

    if out is not None:
        print_json(out)