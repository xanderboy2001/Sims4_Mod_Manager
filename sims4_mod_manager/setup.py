import json

from sims4_mod_manager.utils import config_path, get_mods_dir


def is_first_run() -> bool:
    return not config_path.exists()


def create_default_config():
    config_path.parent.mkdir(parents=True, exist_ok=True)
    default_config = {"mods_folder": str(get_mods_dir())}
    with config_path.open("w", encoding="utf-8") as f:
        json.dump(default_config, f, indent=4)


def load_config():
    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def first_run():
    create_default_config()
