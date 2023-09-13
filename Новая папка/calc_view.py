from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QLineEdit, QStackedWidget

class CalculatorView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Калькулятор')
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)

        self.basic_mode_widget = QWidget()
        self.stacked_widget.addWidget(self.basic_mode_widget)

        self.engineering_mode_widget = QWidget()
        self.stacked_widget.addWidget(self.engineering_mode_widget)

        self.stacked_widget.setCurrentWidget(self.basic_mode_widget)

        self.init_basic_mode_ui()
        self.init_engineering_mode_ui()

        self.toggle_mode_button = QPushButton('Инженерный режим')
        self.toggle_mode_button.clicked.connect(self.toggle_mode)
        layout.addWidget(self.toggle_mode_button)

    def init_basic_mode_ui(self):
        basic_layout = QGridLayout(self.basic_mode_widget)
        basic_layout.addWidget(QLabel('Обычный режим'), 0, 0, 1, 4)

        self.input_field = QLineEdit()
        basic_layout.addWidget(self.input_field, 1, 0, 1, 4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 2, 0
        for button_text in buttons:
            button = QPushButton(button_text)
            basic_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def init_engineering_mode_ui(self):
        engineering_layout = QGridLayout(self.engineering_mode_widget)
        engineering_layout.addWidget(QLabel('Инженерный режим'), 0, 0, 1, 4)

    def toggle_mode(self):
        current_widget = self.stacked_widget.currentWidget()
        if current_widget == self.basic_mode_widget:
            self.stacked_widget.setCurrentWidget(self.engineering_mode_widget)
            self.toggle_mode_button.setText('Обычный режим')
        else:
            self.stacked_widget.setCurrentWidget(self.basic_mode_widget)
            self.toggle_mode_button.setText('Инженерный режим')
