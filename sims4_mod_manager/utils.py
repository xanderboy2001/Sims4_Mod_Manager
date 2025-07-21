from platformdirs import user_config_dir

APP_NAME = "Sims4ModManager"
CONFIG_FILENAME = "config.json"

config_path = user_config_dir(APP_NAME) / CONFIG_FILENAME