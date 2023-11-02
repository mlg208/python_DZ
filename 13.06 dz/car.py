class Car:
    def __init__(self, make, model, year, color, fuel_type, price):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type
        self.price = price

    def start_engine(self):
        return f"The {self.make} {self.model}'s engine is running."

    def get_description(self):
        return f"{self.year} {self.make} {self.model} in {self.color}."

    def calculate_tax(self):
        return 0.1 * self.price

    def repaint(self, new_color):
        self.color = new_color
        return f"The car is now {new_color}."
