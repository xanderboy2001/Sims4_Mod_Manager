import json

from platformdirs import user_downloads_dir

from sims4_mod_manager.utils import config_path, get_mods_dir

DEFAULT_CONFIG = {
    "paths": {
        "mods_folder": str(get_mods_dir()),
        "downloads_folder": str(user_downloads_dir())
    }
}


def create_default_config():
    config_path.parent.mkdir(parents=True, exist_ok=True)
    with config_path.open("w", encoding="utf-8") as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)


def load_config():
    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def print_config(pretty=False):
    config = load_config()
    if pretty:
        print(json.dumps(config, indent=4))
    else:
        print(json.dumps(config))
