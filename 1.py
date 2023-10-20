import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Простой калькулятор")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        self.result_label = QLabel("0") 
        layout.addWidget(self.result_label)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
        ]

        grid_layout = QGridLayout()
        row, col = 1, 0

        for button_text in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def on_button_click(self):
        clicked_button = self.sender()
        if clicked_button:
            button_text = clicked_button.text()
            current_text = self.result_label.text() 

            if button_text == '=':
                try:
                    result = str(eval(current_text))
                    self.result_label.setText(result)
                except Exception:
                    self.result_label.setText("Ошибка")
            elif button_text == 'C':
                self.result_label.setText('0')
            else:
                if current_text == '0':
                    self.result_label.setText(button_text)
                else:
                    self.result_label.setText(current_text + button_text)

def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
