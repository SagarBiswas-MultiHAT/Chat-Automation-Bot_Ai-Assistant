import argparse
import time

import pyautogui
import pyperclip


def print_once() -> None:
    pos = pyautogui.position()
    output = f"{pos.x}, {pos.y}"
    print(output)
    pyperclip.copy(output)
    print("Copied to clipboard.")


def watch_positions(interval: float) -> None:
    print("Watching cursor position. Press Ctrl+C to stop.")
    try:
        while True:
            pos = pyautogui.position()
            print(f"{pos.x}, {pos.y}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Stopped.")


def interactive() -> None:
    print("Move your cursor to the target point.")
    print("Press Enter to capture, or type q then Enter to quit.")
    while True:
        choice = input("> ").strip().lower()
        if choice == "q":
            break
        print_once()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Get cursor position")
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Continuously print cursor position",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=0.2,
        help="Watch interval in seconds (default: 0.2)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.watch:
        watch_positions(args.interval)
    else:
        interactive()


if __name__ == "__main__":
    main()