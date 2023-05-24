user_in = input ("введите трехзначное число")
num = int(user_in)
central_digit = num %10
num = num // 10
centr_number = central_digit *10000 +num
print(centr_number)
#не совсем понял как правильно решать эту задачу, поэтому не знаю правильного решения