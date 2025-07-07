    dialog = QFileDialog(
            self, "Select Sims 4 Mods Folder", str(Path.home()))
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        # Use native dialog if possible
        dialog.setOption(QFileDialog.DontUseNativeDialog, False)
        # Show hidden files/folders
        dialog.setFilter(dialog.filter() | dialog.Hidden)

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