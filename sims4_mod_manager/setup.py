from sims4_mod_manager.config import create_default_config
from sims4_mod_manager.utils import config_file_path


def is_first_run() -> bool:
    return not config_file_path.exists()


def first_run():
    create_default_config()
