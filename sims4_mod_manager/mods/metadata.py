from sims4_mod_manager.utils import get_mods_dir

EXTENSION_MAP = {".package": "Package", ".ts4script": "Script"}


def get_metadata(extensions: str | list[str]) -> list[dict[str, str]]:
    if isinstance(extensions, str):
        extensions = [extensions]
    directory = get_mods_dir()
    metadata_list = []

    for extension in extensions:
        for file in directory.rglob(extension):
            try:
                metadata = {
                    "filename": file.name,
                    "path": str(file.resolve()),
                    "type": EXTENSION_MAP.get(file.suffix.lower(), "Unknown"),
                }
                metadata_list.append(metadata)
            except Exception as e:
                print(f"Skipping {file}: {e}")
    return metadata_list
