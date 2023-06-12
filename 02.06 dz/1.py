def number (num1, num2):
    if num1<num2:
        return -1
    elif num1>num2:
        return 1
    else:
        return 0
num1 = float(input("введите первое число"))
num2 = float(input("введите второе число"))
result = number(num1, num2)
print("результат", result)