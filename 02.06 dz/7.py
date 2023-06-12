def convert_to_seconds(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds
hours = int(input("Введите часы: "))
minutes = int(input("Введите минуты: "))
seconds = int(input("Введите секунды: "))

result = convert_to_seconds(hours, minutes, seconds)
print("Время в секундах:", result)