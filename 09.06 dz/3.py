number = int(input("Введите число: "))
count = 0

while number >= 50:
    number /= 2
    count += 1

print("Полученное число:", number)
print("Количество делений:", count)
