user_in = input ("введите трехзначное число")
num = int(user_in)
last_digit = num %10
num = num // 10
centr_number = last_digit *10000 +num
print(centr_number)
#не смог никак разобраться с этой задачей