#!/usr/bin/env python3

import time

from api_client import print_json, request_api


def navigate_to(x: float, y: float, yaw: float):
    payload = {
        "creator": "pick_rack",
        "type": "standard",
        "target_x": x,
        "target_y": y,
        "target_ori": yaw,
        "target_z": 0,
    }

    result = request_api(
        "POST",
        "/chassis/moves",
        json_body=payload,
    )

    print_json(result)
    return result


def start_rack_detection():
    result = request_api("POST", "/services/start_rack_size_detection")
    print_json(result)
    return result


def align_with_rack():
    payload = {
        "creator": "pick_rack",
        "type": "align_with_rack",
    }

    result = request_api("POST", "/chassis/moves", json_body=payload)
    print_json(result)
    return result


def jack_up():
    result = request_api("POST", "/services/jack_up")
    print_json(result)
    return result


def pick_rack(x: float, y: float, yaw: float):
    print("\n[1/5] Navigating near rack...")
    navigate_to(x, y, yaw)

    input("\nPress ENTER when navigation has completed...")

    print("\n[2/5] Starting rack detection...")
    start_rack_detection()

    time.sleep(3)

    print("\n[3/5] Aligning with rack...")
    align_with_rack()

    input("\nPress ENTER when alignment has completed...")

    print("\n[4/5] Robot should now be centered under rack.")

    print("\n[5/5] Jacking up rack...")
    jack_up()

    print("\nRack pickup sequence complete.")


if __name__ == "__main__":
    print("Enter staging pose beside rack")
    pose = input("x y yaw > ").strip().split()

    if len(pose) != 3:
        raise SystemExit("Expected: x y yaw")

    x, y, yaw = map(float, pose)

    pick_rack(x, y, yaw)