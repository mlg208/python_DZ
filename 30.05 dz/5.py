coin = float(input("введите количество USD "))
money = input("выберите валюту(EUR, UAN, AZN)")
EUR = 10
UAN = 20
AZN = 30
if money == "EUR":
    coin_money = coin * EUR
    print (coin_money)
elif money == "UAN":
    coin_money = coin * UAN
    print (coin_money)
elif money == "AZN":
    coin_money = coin * AZN
    print (coin_money)
else:
    print("вы выбрали не ту валюту, пожалуйста повторите попытку")