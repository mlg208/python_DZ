from ticket import Ticket

class Kassa:
    balance = 0
    tickets = []
    trains = []

    def register_train(self, train):
        self.trains.append(train)

    def get_price(self, source, destination):
        return (len(source) + len(destination)) * 1000

    def buy_ticket(self, source, destination, person):
        money = person.pay(self.get_price(source, destination))
        if money:
            self.balance += money
            for train in self.trains:
                if train.source == source and train.destination == destination:
                    new_ticket = Ticket(source, destination, person.age, person.IIN, person.name)
                    self.tickets.append(new_ticket)
                    print('Номер вашего билета:', new_ticket.number)
                    break
            else:
                print('Нет подходящего поезда. Билет не продан.')
        else:
            print('Нет денег - нет билета, идите отсюда.')

    def get_ticket(self, IIN, source, destination):
        for ticket in self.tickets:
            if ticket.source == source and ticket.destination == destination and ticket.passager_IIN == IIN:
                return ticket
        return None

    def delete_ticket(self, ticket):
        self.tickets.remove(ticket)