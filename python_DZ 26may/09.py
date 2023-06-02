user = input("введите пятизначное число")
try:
    num = int(user)
except ValueError:
    message = "вы ввели не число"
    print (message)
else:
    last_digit = num % 10
    num = num //10
    new_number = last_digit *10000 + num
    print(new_number)