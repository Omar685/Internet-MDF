# IMPORT MODULS
import os
import sys
import json
import sqlite3

# IMPORT QFontDatabase, QIcon AND QFont
from PyQt5.QtGui import QFontDatabase, QIcon, QFont
# IMPORT QApplication FOR START APPLICATION
from PyQt5.QtWidgets import QApplication
import API.main_window

# DB to open
if os.path.isfile("./Database/history.db"):
    connection = sqlite3.connect('./Database/history.db', check_same_thread=False)
    cursor = connection.cursor()
else:
    connection = sqlite3.connect("./Database/history.db", check_same_thread=False)
    cursor = connection.cursor()

# Font
textFont = QFont("Arial", 14)

if os.path.isfile("./json/settings.json"):  # If settings file exists, then open it
    with open("./json/settings.json", "r") as f:
        settings_data = json.load(f)
else:  # If settings not exists, then create a new file with default settings
    json_data = json.loads(
    """
    {
        "defaultSearchEngine": "JSTOR",
        "startupPage": "https://www.jstor.org/",
        "newTabPage": "https://www.jstor.org/",
        "homeButtonPage": "https://www.jstor.org/"
    }
    """
    )
    with open("./json/settings.json", "w") as f:
        json.dump(json_data, f, indent=2)
    with open("./json/settings.json", "r") as f:
        settings_data = json.load(f)


def main():
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
