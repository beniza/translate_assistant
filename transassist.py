import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QLineEdit
from ctypes import alignment
from googletrans import Translator

# NOTE: The current stable release of googletrans doesn't work. However 
# version 4 rc supports it. I installed it using pip install googletrans==4.0.0rc1
# To uninstall currently installed version, pip uninstall googletrans

# NOTE: This is my very first Qt application

# TODO: Add support for [deep-translator](https://pypi.org/project/deep-translator/),\
# [py translaor](https://pypi.org/project/py-translator/) and
# [translate-api](https://pypi.org/project/translate-api/)

class MyTranslator(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Translate")

        self.textbox = QLineEdit(self)
        self.textbox.move(20,40)

        self.label = QtWidgets
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button)

        self.translator = Translator()

        self.button.clicked.connect(self.translate)

    @QtCore.Slot()
    def translate(self):
        t = str(self.textbox.text())
        t = t.replace("/", " ")

        result = self.translator.translate(t, dest='en')
        self.textbox.setText(result.text)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyTranslator()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())