import sys
from pathlib import Path

from PySide6.QtCore import QDir
from PySide6.QtWidgets import (QApplication, QFileDialog, QLabel, QMessageBox,
                               QPushButton, QVBoxLayout, QWidget)


class ModsFolderPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sims 4 Mods Picker")

        self.layout = QVBoxLayout()
        self.label = QLabel("No folder selected.")
        self.layout.addWidget(self.label)

        self.pick_button = QPushButton("Pick Sims 4 Mods Folder")
        self.pick_button.clicked.connect(self.pick_folder)
        self.layout.addWidget(self.pick_button)

        self.setLayout(self.layout)

        # Immediately prompt the user on start
        self.show()
        self.prompt_user()

    def prompt_user(self):
        QMessageBox.information(
            self,
            "Sims 4 Mods Folder",
            "Please select your Sims 4 Mods folder."
        )
        self.pick_folder()

    def pick_folder(self):
        dialog = QFileDialog(
            self, "Select Sims 4 Mods Folder", str(Path.home()))
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        # Use native dialog if possible
        dialog.setOption(QFileDialog.DontUseNativeDialog, False)
        # Show hidden files/folders
        dialog.setFilter(dialog.filter() | QDir.Hidden)

        if dialog.exec():
            folders = dialog.selectedFiles()
            if folders:
                folder = folders[0]
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


def main():
    app = QApplication(sys.argv)
    picker = ModsFolderPicker()
    sys.exit(app.exec())
