num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

min_num = min(num1, num2)

gcd = 1

for i in range(1, min_num + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("Наибольший общий делитель чисел", num1, "и", num2, "равен:", gcd)
