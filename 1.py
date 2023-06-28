import random
from datetime import datetime

class Person:
    def __init__(self, name, iin):
        self.name = name
        self.iin = iin
        self.order = None

class Order:
    def __init__(self, hotel_name, room, date_from, date_to, visitor_name, visitor_iin):
        self.hotel_name = hotel_name
        self.id = random.randint(1000, 9999)
        self.room = room
        self.date_from = date_from
        self.date_to = date_to
        self.visitor_name = visitor_name
        self.visitor_iin = visitor_iin

    def show_info(self):
        print("Информация о брони:")
        print("Номер брони:", self.id)
        print("Гостиница:", self.hotel_name)
        print("Номер комнаты:", self.room.number)
        print("Дата заезда:", self.date_from)
        print("Дата выезда:", self.date_to)
        print("Имя посетителя:", self.visitor_name)
        print("ИИН посетителя:", self.visitor_iin)

class Room:
    def __init__(self, number):
        self.number = number
        self.bedrooms = 2 if number % 2 == 0 else 1
        self.order = None

    def is_empty(self, date=None):
        if date is None:
            date = datetime.now().date()
        return self.order is None or not (self.order.date_from <= date <= self.order.date_to)

    def show_info(self):
        print("Информация о комнате:")
        print("Номер комнаты:", self.number)
        print("Количество спален:", self.bedrooms)
        if self.order is not None:
            print("Бронь на имя:", self.order.visitor_name)
            print("Дата заезда:", self.order.date_from)
            print("Дата выезда:", self.order.date_to)

class Hotel:
    def __init__(self, name, balance, num_rooms):
        self.name = name
        self.balance = balance
        self.rooms = [Room(i) for i in range(1, num_rooms + 1)]

    def get_price(self, room_number, date_from, date_to):
        room = self.rooms[room_number - 1]
        nights = (date_to - date_from).days
        return nights * room.bedrooms * 100  
    def buy_order(self, room_number, date_from, date_to, visitor_name, visitor_iin):
        room = self.rooms[room_number - 1]
        if room.order is None and room.is_empty(date_from):
            price = self.get_price(room_number, date_from, date_to)
            if self.balance >= price:
                self.balance -= price
                order = Order(self.name, room, date_from, date_to, visitor_name, visitor_iin)
                room.order = order
                return order
            else:
                print("Недостаточно средств на счете гостиницы.")
        else:
            print("Номер комнаты уже забронирован или недоступен в указанный период.")
        return None

    def check_in(self, visitor, date):
        if visitor.order is not None and visitor.order.room.is_empty(date) and date == visitor.order.date_from:
            room = visitor.order.room
            room.order = None
            return True
        else:
            print("Нельзя заселиться в данную комнату в указанный день или бронь отсутствует.")
        return False

    def check_out(self, visitor, date):
        if visitor.order is not None and date >= visitor.order.date_to:
            room = visitor.order.room
            nights = (date - visitor.order.date_to).days
            if nights > 0:
                extra_charge = nights * room.bedrooms * 50  
                self.balance += extra_charge
                print("Дополнительная оплата за проживание:", extra_charge)
            visitor.order = None
            return True
        else:
            print("Посетитель не имеет активной брони или необходимо дополнительно оплатить проживание.")
        return False

hotel = Hotel("Отель Комфорт", 100000, 10)

person1 = Person("Иванов", "010101")
person2 = Person("Петров", "020202")

order1 = hotel.buy_order(2, datetime(2023, 6, 1), datetime(2023, 6, 5), person1.name, person1.iin)
order2 = hotel.buy_order(1, datetime(2023, 6, 3), datetime(2023, 6, 7), person2.name, person2.iin)

if order1 is not None:
    person1.order = order1
if order2 is not None:
    person2.order = order2

room1 = hotel.rooms[0]
room2 = hotel.rooms[1]

room1.show_info()
room2.show_info()

order1.show_info()
order2.show_info()

hotel.check_in(person1, datetime(2023, 6, 1))
hotel.check_out(person2, datetime(2023, 6, 8))

room1.show_info()
room2.show_info()
