import sys
import os
from pathlib import Path
from platformdirs import user_config_dir, user_documents_dir

APP_NAME = "Sims4ModManager"
CONFIG_FILENAME = "config.json"

config_dir = Path(user_config_dir(APP_NAME)) / CONFIG_FILENAME

def get_os() -> str:
    platform_name = sys.platform
    if platform_name.startswith("win"):
        return "windows"
    elif platform_name.startswith("darwin"):
        return "mac"
    elif platform_name.startswith("linux"):
        return "linux"
    else:
        return "unknown"

def get_mods_dir() -> str:
    os_name = get_os()
    if os_name in ("windows", "mac"):
        return user_documents_dir()
    elif os_name == "linux":
        return os.path.expanduser('~/.local/share/Steam/steamapps/compatdata/1222670/pfx/drive_c/users/steamuser/Documents/Electronic Arts/The Sims 4/Mods')