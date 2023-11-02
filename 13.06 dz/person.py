class Person:
    def __init__(self, name, age, gender, height, weight, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.address = address

    def introduce(self):
        return f"Hello, I am {self.name}, {self.age} years old."

    def update_address(self, new_address):
        self.address = new_address
        return f"Address updated to {new_address}."

    def get_bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    def is_adult(self):
        return self.age >= 18
