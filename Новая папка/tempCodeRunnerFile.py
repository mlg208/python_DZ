import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from calc_view import CalculatorView

with open('style.css', 'r', encoding='UTF-8') as Myfile:
        print(Myfile)

if __name__ == '__main__':
    app = QApplication([])
    window = CalculatorView()
    window.show()
    app.exec_()
