import sys
import os
from src.config_manager import ConfigManager


def main():
    # Prüfen, ob genug Argumente übergeben wurden
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python main.py validate <config_path>")
        print("  python main.py compare <config1> <config2>")
        return

    # Erstes Argument = Befehl (z. B. validate oder compare)
    command = sys.argv[1]

    # Basisverzeichnis des Projekts (unabhängig davon, wo das Script gestartet wird)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # ========================
    # VALIDATE COMMAND
    # ========================
    if command == "validate":
        # Pfad zur Config aus Argumenten
        path = sys.argv[2]
        full_path = os.path.join(base_dir, path)

        # ConfigManager initialisieren
        manager = ConfigManager(full_path)

        # Versuchen, die Config zu laden
        try:
            config = manager.load_config()
        except FileNotFoundError:
            print(f"Error: File '{path}' not found")
            return

        # Validierung durchführen
        is_valid = manager.validate_config(config)

        # Ergebnis ausgeben
        if is_valid:
            print("✔ Config is valid")
        else:
            print("✘ Config is invalid")

    # ========================
    # COMPARE COMMAND
    # ========================
    elif command == "compare":
        # Prüfen, ob zwei Dateien übergeben wurden
        if len(sys.argv) < 4:
            print("Usage: python main.py compare <config1> <config2>")
            return

        path1 = sys.argv[2]
        path2 = sys.argv[3]

        full_path1 = os.path.join(base_dir, path1)
        full_path2 = os.path.join(base_dir, path2)

        # Zwei ConfigManager für beide Dateien
        manager1 = ConfigManager(full_path1)
        manager2 = ConfigManager(full_path2)

        # Beide Configs laden
        try:
            config1 = manager1.load_config()
            config2 = manager2.load_config()
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return

        # Unterschiede berechnen
        differences = manager1.compare_configs(config1, config2)

        # Ergebnis ausgeben
        if differences:
            print("Differences found:")
            for key, (v1, v2) in differences.items():
                print(f"- {key}: {v1} -> {v2}")
        else:
            print("No differences found")

    # ========================
    # UNBEKANNTER COMMAND
    # ========================
    else:
        print("Unknown command")


# Einstiegspunkt des Programms
if __name__ == "__main__":
    main()
