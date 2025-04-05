# your_script.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class HelloWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello PyQt5")
        self.setGeometry(100, 100, 300, 100)

        layout = QVBoxLayout()
        label = QLabel("Hello from PyQt5!")
        layout.addWidget(label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloWindow()
    window.show()
    sys.exit(app.exec_())
