
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Рисовалка")
        self.setFixedSize(600, 450)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.circles = []
        self.color = "red"
        self.size = 30

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.fillRect(self.rect(), QColor("white"))

        for x, y, size, color in self.circles:
            painter.setBrush(QColor(color))
            painter.drawEllipse(x, y, size, size)

        painter.setPen(QColor("black"))
        painter.drawText(10, 20, f"Размер: {self.size}")
        painter.drawText(10, 40, f"Цвет: {self.color}")
        painter.drawText(10, 60, f"Фигур: {len(self.circles)}")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            x = int(event.position().x())
            y = int(event.position().y())

            self.circles.append((x, y, self.size, self.color))

        elif event.button() == Qt.MouseButton.RightButton:
            if len(self.circles) > 0:
                self.circles.pop()

        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_1:
            self.color = "red"

        elif event.key() == Qt.Key.Key_2:
            self.color = "blue"

        elif event.key() == Qt.Key.Key_3:
            self.color = "green"

        elif event.key() == Qt.Key.Key_Up:
            self.size += 10

        elif event.key() == Qt.Key.Key_Down:
            if self.size > 10:
                self.size -= 10

        elif event.key() == Qt.Key.Key_C:
            self.circles.clear()

        self.update()


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
