from sims4_mod_manager.utils import get_mods_dir

PATTERN_MAP = {"package": "*.package", "script": "*.ts4script"}
EXTENSION_MAP = {".package": "Package", ".ts4script": "Script"}


def get_metadata(filetypes: str | list[str]) -> list[dict[str, str]]:
    if isinstance(filetypes, str):
        filetypes = [filetypes]
    directory = get_mods_dir()
    metadata_list = []
    patterns = []

    for filetype in filetypes:
        patterns.append(PATTERN_MAP[filetype.lower()])

    for pattern in patterns:
        for file in directory.rglob(pattern):
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
