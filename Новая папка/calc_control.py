from PyQt5.QtWidgets import QPushButton, QLineEdit
from calc_model import CalculatorModel
from calc_view import CalculatorView

class CalculatorController:
    def __init__(self, model: CalculatorModel, view: CalculatorView):
        self.model = model
        self.view = view

        self.view.init_basic_mode_ui()
        self.view.init_engineering_mode_ui()

        for button in self.view.basic_mode_widget.findChildren(QPushButton):
            if button.text() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                button.clicked.connect(lambda checked, text=button.text(): self.digit_clicked(text))
            elif button.text() in ['+', '-', '*', '/']:
                button.clicked.connect(lambda checked, text=button.text(): self.operator_clicked(text))
            elif button.text() == '=':
                button.clicked.connect(self.calculate)
            elif button.text() == 'C':
                button.clicked.connect(self.clear)

        for button in self.view.engineering_mode_widget.findChildren(QPushButton):
            pass

        self.view.input_field.textChanged.connect(self.input_changed)

    def digit_clicked(self, digit):
        current_text = self.view.input_field.text()
        new_text = current_text + digit
        self.view.input_field.setText(new_text)

    def operator_clicked(self, operator):
        current_text = self.view.input_field.text()
        if current_text:
            new_text = current_text + operator
            self.view.input_field.setText(new_text)

    def calculate(self):
        current_text = self.view.input_field.text()
        try:
            result = str(eval(current_text))
            self.view.input_field.setText(result)
        except Exception as e:
            self.view.input_field.setText('Error')

    def clear(self):
        self.view.input_field.clear()

    def input_changed(self):
        pass
