def sum (num1, num2, num3):
    combined_number = int(str(num1) + str(num2) + str(num3))
    return combined_number
num1 = int(input("введите первое число"))
num2 = int(input("введите второе число"))
num3 = int(input("введите третье число"))
result = sum (num1, num2, num3)
print ("объединенный цифры равны", result)
