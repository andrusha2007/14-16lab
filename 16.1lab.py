import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QFrame
from PyQt5.QtGui import QIcon, QFont, QPixmap
from currency_converter import CurrencyConverter

class CurrencyConv(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Конвертер валют')
        try:
            self.setWindowIcon(QIcon('icons8-сделка-48.png'))
        except:
            pass
        self.setFixedSize(500, 660)
        self.setStyleSheet("background-color: #22222e;")
        self.init_UI()

    def init_UI(self):

        self.frame = QFrame(self)
        self.frame.setGeometry(0, 0, 500, 270)
        self.frame.setStyleSheet("background-color: #fb5b5d;")


        self.title_label = QLabel(self.frame)
        self.title_label.setText("Конвертер валют")
        self.title_label.setFont(QFont("Impact", 16))
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setGeometry(0, 15, 500, 50)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        try:
            pixmap = QPixmap('exchanging.png')
            self.image_label = QLabel(self.frame)
            self.image_label.setPixmap(pixmap.scaled(120, 120, QtCore.Qt.KeepAspectRatio))
            self.image_label.setGeometry(190, 100, 120, 120)
        except:
            pass

        try:
            pixmap = QPixmap('icon_conv1.png')
            self.icon_label = QLabel(self.frame)
            self.icon_label.setPixmap(pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio))
            self.icon_label.setGeometry(30, 15, 50, 50)
        except:
            pass


        self.input_cur = QLineEdit(self)
        self.input_cur.setGeometry(50, 320, 380, 60)
        self.input_cur.setPlaceholderText("Из валюты")
        self.input_cur.setAlignment(QtCore.Qt.AlignCenter)
        self.input_cur.setStyleSheet("""
            background-color: #22222e;
            border: 2px solid #f66867;
            border-radius: 30;
            color: white;
            font: 14pt Impact;
        """)

        self.input_sum = QLineEdit(self)
        self.input_sum.setGeometry(50, 390, 380, 60)
        self.input_sum.setPlaceholderText("Сколько")
        self.input_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.input_sum.setStyleSheet("""
            background-color: #22222e;
            border: 2px solid #f66867;
            border-radius: 30;
            color: white;
            font: 14pt Impact;
        """)

        self.output_cur = QLineEdit(self)
        self.output_cur.setGeometry(50, 460, 380, 60)
        self.output_cur.setPlaceholderText("В валюту")
        self.output_cur.setAlignment(QtCore.Qt.AlignCenter)
        self.output_cur.setStyleSheet("""
            background-color: #22222e;
            border: 2px solid #f66867;
            border-radius: 30;
            color: white;
            font: 14pt Impact;
        """)

        self.output_sum = QLineEdit(self)
        self.output_sum.setGeometry(50, 530, 380, 60)
        self.output_sum.setPlaceholderText("Итого")
        self.output_sum.setAlignment(QtCore.Qt.AlignCenter)
        self.output_sum.setReadOnly(True)
        self.output_sum.setStyleSheet("""
            background-color: #22222e;
            border: 2px solid #f66867;
            border-radius: 30;
            color: white;
            font: 14pt Impact;
        """)


        self.pushButton = QPushButton("Конвертация", self)
        self.pushButton.setGeometry(50, 600, 380, 60)
        self.pushButton.setFont(QFont("Impact", 14))
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #fb5b5d;
                border-radius: 30;
                color: white;
            }
            QPushButton:pressed {
                background-color: #fa4244;
            }
        """)
        self.pushButton.clicked.connect(self.converter)

    def converter(self):
        try:
            input_cur = self.input_cur.text().strip().upper()
            output_cur = self.output_cur.text().strip().upper()
            input_sum = float(self.input_sum.text())

            if not input_cur or not output_cur:
                self.output_sum.setText("Ошибка ввода")
                return

            c = CurrencyConverter()
            result = c.convert(input_sum, input_cur, output_cur)
            self.output_sum.setText(f"{result:.2f}")

        except ValueError:
            self.output_sum.setText("Ошибка суммы")
        except Exception as e:
            self.output_sum.setText(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CurrencyConv()
    window.show()
    sys.exit(app.exec())