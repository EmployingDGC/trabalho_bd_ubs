from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolTip,
    QPushButton
)

class MainWindow (QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.TOP = 100
        self.LEFT = 100
        self.WIDTH = 800
        self.HEIGHT = 600
        self.TITLE = "Trabalho DB UBS"

        self.button_1("botão teste")

    def load_window(self) -> None:
        self.setWindowTitle(
            self.TITLE
        )

        self.setFixedSize(
            self.WIDTH,
            self.HEIGHT
        )

        self.show()
    
    def button_1(self, name):
        def click():
            print("teste")

        button = QPushButton(name, self)

        button.move(
            250,
            250
        )

        button.resize(
            300,
            150
        )

        button.setStyleSheet("""
            QPushButton {
                background-color: #f20587;
                border: 2px solid #000
            }
        """)

        button.clicked.connect(click)
