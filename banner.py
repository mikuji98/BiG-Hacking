from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QPropertyAnimation, QRect, Qt, QTimer
from PyQt5.QtGui import QLinearGradient, QBrush, QFont, QPainter, QColor

class AnimatedBanner(QLabel):
    def __init__(self, text="DevDaRK Kabo", parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setObjectName("banner")
        self.setAlignment(Qt.AlignCenter)
        self.setGeometry(0, -60, 600, 60)
        self.setFont(QFont("Segoe UI", 28, QFont.Bold))

        # إعدادات الفلاش
        self.flash_intensity = 0
        self.flash_direction = 1

        # مؤقت لتحديث الرسوم
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_effects)
        self.timer.start(80)

        self.animate()

    def animate(self):
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(3000)
        self.anim.setStartValue(QRect(0, -60, 600, 60))
        self.anim.setEndValue(QRect(0, 20, 600, 60))
        self.anim.setLoopCount(-1)
        self.anim.start()

    def update_effects(self):
        # تأثير الفلاش المتوهج
        self.flash_intensity += self.flash_direction * 15
        if self.flash_intensity >= 255 or self.flash_intensity <= 100:
            self.flash_direction *= -1
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), 0)

        # ألوان متوهجة متغيرة
        glow_color = QColor(0, self.flash_intensity, 255)
        gradient.setColorAt(0, QColor("#0f0f0f"))
        gradient.setColorAt(0.5, glow_color)
        gradient.setColorAt(1, QColor("#0f0f0f"))

        painter.setPen(QColor("#00ffcc"))
        painter.setBrush(QBrush(gradient))
        painter.setFont(self.font())
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())
