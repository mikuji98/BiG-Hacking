from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QStatusBar
from PyQt5.QtCore import Qt
import pyperclip

from commands.security import security_commands
from commands.networking import networking_commands
from commands.android import android_commands
from commands.web import web_commands
from banner import AnimatedBanner

class SectionWindow(QWidget):
    def __init__(self, category):
        super().__init__()
        self.setWindowTitle(f"أوامر {category}")
        self.setFixedSize(900, 600)
        self.setStyleSheet(open("style.qss").read())

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        # بنر متحرك خاص بالقسم
        self.banner = AnimatedBanner()
        self.banner.setText(f"DevDaRK Kabo - {category}")
        layout.addWidget(self.banner)

        # جدول الأوامر
        self.table = QTableWidget()
        layout.addWidget(self.table)

        # شريط الحالة لرسائل النسخ
        self.status_bar = QStatusBar()
        layout.addWidget(self.status_bar)

        self.setLayout(layout)

        self.load_commands(category)

    def load_commands(self, category):
        data = {
            "Security": security_commands,
            "Networking": networking_commands,
            "Android": android_commands,
            "Web": web_commands
        }.get(category, [])

        self.table.setRowCount(len(data))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["الأمر", "الوصف", "نسخ"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        # جعل الأعمدة تأخذ حجم مناسب
        self.table.horizontalHeader().setDefaultSectionSize(250)
        self.table.horizontalHeader().setMinimumSectionSize(200)

        for i, item in enumerate(data):
            self.table.setItem(i, 0, QTableWidgetItem(item["command"]))
            self.table.setItem(i, 1, QTableWidgetItem(item["description"]))

            copy_btn = QPushButton("📋 نسخ")
            copy_btn.setCursor(Qt.PointingHandCursor)
            copy_btn.clicked.connect(self.make_copy_handler(item["command"]))
            self.table.setCellWidget(i, 2, copy_btn)

    def make_copy_handler(self, cmd):
        def handler():
            pyperclip.copy(cmd)
            self.status_bar.showMessage(f"✅ تم نسخ الأمر: {cmd}", 2000)
        return handler
