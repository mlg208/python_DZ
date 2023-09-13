import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from calc_view import CalculatorView

with open("style.css", "r", encoding="UTF-8") as fd:
        style = fd.read()

if __name__ == '__main__':
    app = QApplication([])
    window = CalculatorView()
    window.show()
    app.exec_()
