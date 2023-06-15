year = input("Введите год вашего рождения: ")
month = input("Введите месяц вашего рождения: ")
day = input("Введите число вашего рождения: ")

date = "{:02d}.{:02d}.{}".format(int(day), int(month), year)
print("Дата вашего рождения:", date)
