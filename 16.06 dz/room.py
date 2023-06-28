from datetime import datetime
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