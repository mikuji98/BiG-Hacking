import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from banner import AnimatedBanner
from section_window import SectionWindow
from welcome import WelcomeWindow
import json
import os

class DevDarkKaboApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DevDaRK Kabo")
        self.setFixedSize(600, 500)
        try:
            with open("style.qss", "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except Exception:
            pass

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        self.banner = AnimatedBanner()
        layout.addWidget(self.banner)

        self.security_btn = QPushButton("🔐 الأمن السيبراني")
        self.network_btn = QPushButton("🌐 الشبكات")
        self.android_btn = QPushButton("📱 أندرويد")
        self.web_btn = QPushButton("🕸️ اختراق الويب")

        self.security_btn.clicked.connect(lambda: self.open_section("Security"))
        self.network_btn.clicked.connect(lambda: self.open_section("Networking"))
        self.android_btn.clicked.connect(lambda: self.open_section("Android"))
        self.web_btn.clicked.connect(lambda: self.open_section("Web"))

        layout.addWidget(self.security_btn)
        layout.addWidget(self.network_btn)
        layout.addWidget(self.android_btn)
        layout.addWidget(self.web_btn)

        self.setLayout(layout)

    def open_section(self, category):
        section = SectionWindow(category)
        section.show()


def main():
    app = QApplication(sys.argv)

    config_path = os.path.join(os.getcwd(), "config.json")
    show_welcome = True

    if os.path.exists(config_path):
        try:
            with open(config_path, encoding="utf-8") as f:
                config = json.load(f)
                show_welcome = config.get("show_welcome", True)
        except Exception:
            show_welcome = True

    def start_main_app():
        window = DevDarkKaboApp()
        window.show()

    if show_welcome:
        welcome_window = WelcomeWindow(on_continue=start_main_app)
        welcome_window.show()
    else:
        start_main_app()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
