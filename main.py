import sys
import os
from src.config_manager import ConfigManager


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python main.py validate <config_path>")
        print("  python main.py compare <config1> <config2>")
        return

    command = sys.argv[1]

    base_dir = os.path.dirname(os.path.abspath(__file__))

    if command == "validate":
        path = sys.argv[2]
        full_path = os.path.join(base_dir, path)

        manager = ConfigManager(full_path)

        try:
            config = manager.load_config()
        except FileNotFoundError:
            print(f"Error: File '{path}' not found")
            return

        is_valid = manager.validate_config(config)
        if is_valid:
            print("✔ Config is valid")
        else:
            print("✘ Config is invalid")

    elif command == "compare":
        if len(sys.argv) < 4:
            print("Usage: python main.py compare <config1> <config2>")
            return

        path1 = sys.argv[2]
        path2 = sys.argv[3]

        full_path1 = os.path.join(base_dir, path1)
        full_path2 = os.path.join(base_dir, path2)

        manager1 = ConfigManager(full_path1)
        manager2 = ConfigManager(full_path2)

        try:
            config1 = manager1.load_config()
            config2 = manager2.load_config()
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return

        differences = manager1.compare_configs(config1, config2)

        if differences:
            print("Differences found:")
            for key, (v1, v2) in differences.items():
                print(f"- {key}: {v1} -> {v2}")
        else:
            print("No differences found")

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
