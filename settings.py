import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QMessageBox, QFileDialog, QVBoxLayout, QLabel, QPushButton
)
from pathlib import Path
from configparser import ConfigParser


CONFIG_PATH = Path("config.ini")
DEFAULTS = {
    'downloads_path': str(Path.home() / "Downloads"),
    'mods_path': 'Null'
}


class ModsFolderPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sims 4 Mods Picker")

        self.config = ConfigParser()
        self.load_config()

        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.layout.addWidget(self.label)

        self.pick_button = QPushButton("Change Sims 4 Mods Folder")
        self.pick_button.clicked.connect(self.pick_folder)
        self.layout.addWidget(self.pick_button)

        self.setLayout(self.layout)

        # Show current config path or prompt if none set
        if self.mods_path == 'Null' or not Path(self.mods_path).exists():
            self.show()
            self.prompt_user()
        else:
            self.label.setText(f"Current Mods Folder: {self.mods_path}")
            self.show()

    def load_config(self):
        if CONFIG_PATH.exists():
            self.config.read(CONFIG_PATH)
        else:
            self.config['DEFAULT'] = DEFAULTS
            with open(CONFIG_PATH, 'w') as f:
                self.config.write(f)

        self.mods_path = self.config['DEFAULT'].get('mods_path', 'Null')

    def save_config(self):
        self.config['DEFAULT']['mods_path'] = self.mods_path
        with open(CONFIG_PATH, 'w') as f:
            self.config.write(f)

    def prompt_user(self):
        QMessageBox.information(
            self,
            "Sims 4 Mods Folder",
            "Please select your Sims 4 Mods folder."
        )
        self.pick_folder()

    def pick_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Sims 4 Mods Folder",
            str(Path.home())
        )
        if folder:
            if self.is_valid_mods_folder(folder):
                self.mods_path = folder
                self.save_config()
                self.label.setText(f"Selected Mods Folder: {folder}")
            else:
                QMessageBox.warning(
                    self,
                    "Invalid Folder",
                    "The selected folder does not appear to be a valid Sims 4 Mods folder."
                )
                self.pick_folder()  # Retry

    def is_valid_mods_folder(self, folder_path: str) -> bool:
        """Basic validation: checks if folder contains 'Mods' folder or 'Resource.cfg' file"""
        p = Path(folder_path)
        resource_cfg = p / "Resource.cfg"
        mods_subfolder = p / "Mods"
        return resource_cfg.exists() or mods_subfolder.exists()


def main():
    app = QApplication(sys.argv)
    picker = ModsFolderPicker()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
