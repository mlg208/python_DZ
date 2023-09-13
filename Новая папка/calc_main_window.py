from PyQt5.QtWidgets import QMainWindow, QApplication
from calc_view import CalculatorView
from calc_model import CalculatorModel
from calc_control import CalculatorController

class CalculatorMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.central_widget = CalculatorView()
        self.setCentralWidget(self.central_widget)

        self.model = CalculatorModel()
        self.controller = CalculatorController(self.model, self.central_widget)

        self.setWindowTitle('Калькулятор')
        self.setGeometry(100, 100, 300, 400)



