from sims4_mod_manager.utils import config_path, get_mods_dir


def is_first_run() -> bool:
    return not config_path.exists()


def create_default_config():
    config_path.parent.mkdir(parents=True, exist_ok=True)
    default_config = {"mods_folder": str(get_mods_dir())}
