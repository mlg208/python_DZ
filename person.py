from random import randint
class Person:
    balance = 0
    name = ""
    IIN = 0
    age = 0
    
    def __init__(self, name, age,):
        self.name = name
        self.age = age
        self.IIN = randint(000000000000, 999999999999)

    def show(self):
        message = " Человек %s, возраст %s, лет, ИИН: %s, баланс %s" %(self.name,
                    self.age, self.IIN, self.balance)
        print(message)
    def earn (self, amount):
        self.balance += amount
    def pay(self,amount):
        if self.balance < amount:
            return 0
        self.balance -= amount
        return amount
print ('это человек',__name__)