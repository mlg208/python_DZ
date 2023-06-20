days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

while True:
    for day in days_of_week:
        print("День недели -", day)
        choice = input("Хотите увидеть следующий день? (да/нет): ")
        if choice.lower() == "нет":
            break
    else:
        continue
    break

# VN: интересное решение)
# Но лучше избегать бесконечных циклов типа while True, используя вместо True нормальное условие