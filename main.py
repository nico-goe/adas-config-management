import sys
import os
from src.config_manager import ConfigManager


def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py validate <config_path>")
        return

    command = sys.argv[1]
    path = sys.argv[2]

    # Make path robust (independent of execution location)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, path)

    manager = ConfigManager(full_path)

    # Error handling for missing file
    try:
        config = manager.load_config()
    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return

    if command == "validate":
        is_valid = manager.validate_config(config)
        if is_valid:
            print("✔ Config is valid")
        else:
            print("✘ Config is invalid")

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
