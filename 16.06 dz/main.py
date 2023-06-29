from datetime import datetime
# VN: не хватает импортов:
# from hotel import Hotel
# from person import Person


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
