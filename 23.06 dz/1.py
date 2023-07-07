numbers = input("Введите 10 чисел через запятую: ")
numbers_list = numbers.split(',')

if len(numbers_list) < 10:
    print("Вы ввели менее 10 чисел. Пожалуйста, введите 10 чисел через запятую.")
    exit()
elif len(numbers_list) > 10:
    numbers_list = numbers_list[:10]
    print("Вы ввели более 10 чисел. Лишние числа будут удалены.")

numbers_list = [int(num.strip()) for num in numbers_list]

first_list = numbers_list
second_list = [num for num in numbers_list if num % 2 == 0]

print("Первый список:", first_list)
print("Второй список (четные числа):", second_list)
