user = input("введите первое число")
user1 = input("введите второе число")
num1 = float(user)
num2 = float (user1)


template = """
сумма чисе:       %.2f
разность чисел:   %.2f
произведeниe:     %.2f
частное:          %.2f
"""
Sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
message = template % (Sum, sub, mul, div)
print(message) 