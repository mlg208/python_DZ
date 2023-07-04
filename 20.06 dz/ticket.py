from random import randint
class Ticket:
    number = 0
    passager_day = 0
    passager_IIN = 0
    passager_name = 0
    source = ""
    distanation = ""
    def __init__(self, source, distanation, passager_age, passager_IIN, passager_name):
        self.number = randint (100000, 999999)
        self.source  = source
        self.distanation = distanation
        self.passager_age = passager_age
        self.passager_IIN = passager_IIN
        self.passager_name = passager_name

    def __repr__(self):
        msg = "билет № %s:, %s -- %s" % (self.number, self.source, self.distanation)
        return msg

    def show (self):
        message = "билет № %s:, %s -- %s" % (self.number, self.source, self.distanation)
        message += " Пассажир: %s, ИИН:%s, возраст %s " % (self.passager_name,
                                self.passager_IIN, self.passager_age)
        print(message)
print('это билет', __name__)