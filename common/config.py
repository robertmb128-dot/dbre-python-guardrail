
# common/config.py
import configparser
from pathlib import Path

def load_config(path):
    config_path = Path(path)

    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {path}")

    config = configparser.ConfigParser()
    config.read(config_path)

    return config
