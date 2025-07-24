import json

from sims4_mod_manager.utils import data_dir, get_mods_dir

PATTERN_MAP = {"package": "*.package", "script": "*.ts4script"}
EXTENSION_MAP = {".package": "Package", ".ts4script": "Script"}

DATA_FILE = data_dir / "metadata.json"


def get_metadata(filetypes: str | list[str] = None) -> list[dict[str, str]]:
    if not filetypes:
        filetypes = ["package", "script"]
    else:
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


def write_metadata(metadata: list[dict[str, str]]) -> None:
    if not metadata:
        metadata = get_metadata()
    data_dir.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)


def load_metadata() -> None:
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)
