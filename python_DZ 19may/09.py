user = input("введите пятизначное число")
num = int(user)
last_digit = num % 10
num = num //10
new_number = last_digit *10000 + num
print(new_number)