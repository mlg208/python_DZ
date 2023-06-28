import random
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
