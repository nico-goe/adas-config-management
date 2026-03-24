import json

class ConfigManager:
    def __init__(self, path):
        self.path = path

    def load_config(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def validate_config(self, config):
        required_keys = ["vehicle", "sensors", "test_case"]
        return all(key in config for key in required_keys)

    def save_config(self, config, output_path):
        with open(output_path, "w") as f:
            json.dump(config, f, indent=4)
