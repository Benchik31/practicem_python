from pathlib import Path
import json

CONFIG_PATH = Path(__file__).parent / "config.json"

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

config = load_config()
ROOT_DIR = Path(config["root_dir"]).resolve()