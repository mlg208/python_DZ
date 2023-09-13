class CalculatorModel:
    def __init__(self):
        self.current_value = '0'
        self.memory_value = '0'
        self.operator = None

    def clear(self):
        self.current_value = '0'
        self.operator = None

    def calculate(self):
        if self.operator:
            try:
                if self.operator == '+':
                    self.current_value = str(float(self.memory_value) + float(self.current_value))
                elif self.operator == '-':
                    self.current_value = str(float(self.memory_value) - float(self.current_value))
                elif self.operator == '*':
                    self.current_value = str(float(self.memory_value) * float(self.current_value))
                elif self.operator == '/':
                    if float(self.current_value) == 0:
                        self.current_value = 'Error'
                    else:
                        self.current_value = str(float(self.memory_value) / float(self.current_value))
            except Exception as e:
                self.current_value = 'Error'
            self.operator = None

    def append_digit(self, digit):
        if self.current_value == '0' or self.current_value == 'Error':
            self.current_value = digit
        else:
            self.current_value += digit

    def set_operator(self, operator):
        if self.operator:
            self.calculate()
        self.memory_value = self.current_value
        self.operator = operator
