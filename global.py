from kassa import Kassa
from person import Person
from train import Train

print('Главная программа', __name__)

ilon = Person("Ilon Mask", 50)
ilon.earn(100000)
ilon.pay(20000)
ilon.show()

moscow_kassa = Kassa()
price = moscow_kassa.get_price("Москва", "Париж")
moscow_kassa.buy_ticket("Москва", "Париж", ilon)
moscow_kassa.buy_ticket("Алматы", "Япония", ilon)
moscow_kassa.buy_ticket("Антарктида", "Гинева", ilon)

train = Train(moscow_kassa, "Москва", "Париж")
train.show()

print(moscow_kassa.tickets)
train.board(ilon)
print(moscow_kassa.tickets)
