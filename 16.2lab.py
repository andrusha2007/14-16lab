import sys
import requests
import re
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QFrame, QTextEdit
from PyQt5.QtGui import QIcon, QFont

class JokeGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Генератор шуток')
        try:
            self.setWindowIcon(QIcon('joke_icon.png'))
        except:
            pass

        self.setFixedSize(900, 800)
        self.setStyleSheet("background-color: #22222e;")
        self.init_UI()

    def init_UI(self):

        self.frame = QFrame(self)
        self.frame.setGeometry(0, 0, 900, 160)
        self.frame.setStyleSheet("background-color: #fb5b5d;")


        self.title_label = QLabel(self.frame)
        self.title_label.setText("Генератор шуток")
        self.title_label.setFont(QFont("Impact", 30))
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setGeometry(0, 30, 900, 80)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)


        self.joke_btn = QPushButton("Расскажи шутку", self)
        self.joke_btn.setGeometry(220, 190, 500, 100)
        self.joke_btn.setFont(QFont("Impact", 24))
        self.joke_btn.setStyleSheet("""
            QPushButton {
                background-color: #fb5b5d;
                border-radius: 45;
                color: white;
            }
            QPushButton:pressed {
                background-color: #fa4244;
            }
        """)
        self.joke_btn.clicked.connect(self.get_joke)


        self.joke_output = QTextEdit(self)
        self.joke_output.setGeometry(30, 320, 840, 430)
        self.joke_output.setStyleSheet("""
            background-color: #22222e;
            border: 4px solid #f66867;
            border-radius: 20;
            color: white;
            font: 18pt Arial;
            padding: 20px;
        """)
        self.joke_output.setReadOnly(True)
        self.joke_output.setPlaceholderText("Нажми кнопку, чтобы услышать шутку...")

    def get_joke(self):
        url = "http://rzhunemogu.ru/RandJSON.aspx?CType=1"
        try:
            response = requests.get(url, timeout=5)
            raw_text = response.text.strip()
            pattern = r'"content"\s*:\s*"((?:[^"\\]|\\.)*)"'
            match = re.search(pattern, raw_text)
            if match:
                joke_text = match.group(1)
                joke_text = joke_text.replace('\\"', '"')
                joke_text = joke_text.replace('\\n', '\n')
                self.joke_output.setText(joke_text)
            else:
                try:
                    import json
                    data = json.loads(raw_text)
                    joke_text = data.get("content", "Не удалось получить шутку")
                    self.joke_output.setText(joke_text)
                except:
                    self.joke_output.setText("Не удалось разобрать шутку. Попробуйте ещё раз.")
        except requests.exceptions.RequestException:
            self.joke_output.setText("Нет соединения с интернетом.")
        except Exception as e:
            self.joke_output.setText(f"Ошибка: {str(e)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = JokeGenerator()
    window.show()
    sys.exit(app.exec())