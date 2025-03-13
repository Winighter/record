import os ,sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from py_toggle import PyToggle

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.resize(500, 500)

        self.container = QFrame()
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container { background-color: #222 }")
        self.layout = QVBoxLayout()

        self.toggle = PyToggle()
        self.toggle2 = PyToggle(
            width=200,
            active_color="#F00"
        )
        self.toggle3 = PyToggle(
            width=200,
            bg_color="#FFF"
        )

        self.layout.addWidget(self.toggle, Qt.AlignCenter, Qt.AlignCenter)
        self.layout.addWidget(self.toggle2, Qt.AlignCenter, Qt.AlignCenter)
        self.layout.addWidget(self.toggle3, Qt.AlignCenter, Qt.AlignCenter)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
