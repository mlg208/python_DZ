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

class Herbivore(Animal):
    def __init__(self, name, weight, size, ratio):
        super().__init__(name, weight, size)
        self.ratio = ratio
    
    def eat(self, meal):
        if meal in self.ratio:
            super().eat(meal)
        else:
            print(f"{self.name} не ест {meal}.")

class Predator(Animal):
    def eat(self, meal):
        if isinstance(meal, Animal) and meal.size < self.size and meal.weight < self.weight:
            meal_size = meal.size
            meal_weight = meal.weight
            super().eat(meal.name)
            self.size += meal_size * 0.2
            self.weight += meal_weight * 0.2
        else:
            print(f"{self.name} не может съесть {meal}.")

herbivore = Herbivore("Зебра", 150, "средний", ["трава", "листья"])
predator = Predator("Лев", 200, "большой")
herbivore.talk()
herbivore.eat("трава")
herbivore.eat("мясо")
predator.talk()
predator.eat(herbivore)
