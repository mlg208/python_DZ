user_in = input("введите длину стороны квадрата")
try:
    long = int(user_in)
except ValueError:
    message = "вы ввели не цифры"
    print (message)
else: 
    result = long ** 2
    print ("площадь вашего квадрата равна", result)