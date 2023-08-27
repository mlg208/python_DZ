#Создание словаря
student = {
    'name': 'Alice',
    'age': 20,
    'major': 'Computer Science',
    'grades': {
        'math': 90,
        'english': 85,
        'history': 78
    }
}

# Доступ к элементам словаря
print("Имя студента:", student['name'])
print("Возраст студента:", student['age'])
print("Оценка по математике:", student['grades']['math'])

# Перебор ключей и значений словаря
print("\nперебор ключей:")
for key in student:
    print(key)

print("\nПеребор значений:")
for value in student.values():
    print(value)

print("\nПеребор ключей и значений:")
for key, value in student.items():
    print(key, ":", value)

# Добавление новых элементов
student['email'] = 'alice@example.com'
print("\nСловарь после добавления email:", student)

# Удаление элемента
del student['major']
print("\nСловарь после удаления major:", student)

# Проверка наличия ключа
print("\nЕсть ли ключ 'age' в словаре:", 'age' in student)
print("Есть ли ключ 'gender' в словаре:", 'gender' in student)

# Получение значения по ключу с предоставлением значения по умолчанию
grade = student.get('grades', {}).get('physics', 'N/A')
print("\nОценка по физике:", grade)

# Очистка словаря
student.clear()
print("\nПустой словарь:", student)
