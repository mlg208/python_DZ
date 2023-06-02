user_in = input ("введите трехзначное число")
try:
    num = int(user_in)
except ValueError:
    message = "Это не число!"
    print(message)
else:
    last_digit = num %10
    num = num // 10
    centr_number = last_digit *10000 +num
    print(centr_number)
