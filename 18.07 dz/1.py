class Animal:
    def __init__(self, name, weight, size):
        self.name = name
        self.weight = weight
        self.size = size
    
    def talk(self):
        print("Mmmmmmm...")
    
    def eat(self, meal):
        meal_length = len(meal)
        self.size += meal_length
        self.weight += meal_length


my_animal = Animal("Леопард", 100, "средний")
print(f"Имя: {my_animal.name}")
print(f"Вес: {my_animal.weight}")
print(f"Размер: {my_animal.size}")
my_animal.talk()
my_animal.eat("мясо")
print(f"После кормежки:")
print(f"Вес: {my_animal.weight}")
print(f"Размер: {my_animal.size}")
