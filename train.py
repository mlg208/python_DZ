from random import randint
class Train:
    source = ""
    distanation = ""
    number = 0
    kassa = None
    def __init__(self,kassa, source, distanation):
        self.kassa = kassa
        self.source = source
        self.distanation = distanation
        self.number = randint (0000, 9999)
        kassa.register_train(self)
    def board(self, person):
        ticket = self.kassa.get_ticket(person.IIN, self.source, self.distanation)
        if ticket:
            message = "Добро пожаловаьб %s, ваш поезд №%s прибыл, от %s, до %s." %(
            person.name, self.number, self.source, self.distanation)
            print(message)
            self.kassa.delete_ticket(ticket)
        else:
            print ("нет билета")
    
    def show(self):
        message = "поезд №%s, от станциии %s до станции %s." %(self.number,self.source, self.distanation)
        print(message)
print('это поезд',__name__)