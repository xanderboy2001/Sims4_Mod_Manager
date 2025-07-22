from sims4_mod_manager.cli import main
from sims4_mod_manager.setup import create_default_config, is_first_run

if __name__ == "__main__":
    if is_first_run():
        print("This is the first run. Creating default config...")
        create_default_config()
    main()
