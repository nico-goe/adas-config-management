import sys
from src.config_manager import ConfigManager

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py validate <config_path>")
        return

    command = sys.argv[1]
    path = sys.argv[2]

    manager = ConfigManager(path)
    config = manager.load_config()

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
