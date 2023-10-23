import os
import sys
import json
import sqlite3
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase, QIcon, QFont
import API.main_window
import os

os.system("start ./learn/app.py")

gui_app = QApplication(sys.argv)

# Disable shortcut in context menu
gui_app.styleHints().setShowShortcutsInContextMenus(False)

# Set the window name
QApplication.setApplicationName("Internet MDF")

# Set the window icon
QApplication.setWindowIcon(QIcon(os.path.join("resources", "logos", "browser.png")))

# App styles
if os.path.isfile(os.path.join("styles", "styles.css")):
    with open(os.path.join("styles", "styles.css")) as f:
        gui_app.setStyleSheet(f.read())

QFontDatabase.addApplicationFont(os.path.join("fonts", "fa-solid-900.ttf"))

window = API.main_window.mainWindow()

sys.exit(gui_app.exec_())

# if __name__ == "__main__":
#     main()
