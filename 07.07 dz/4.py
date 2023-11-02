fruits = ['apple','banana','cherry','apple','orange','banana']
passed = {} # Словарь для уже просмотренных элементов
duplicates = [] # Список для найденных дубликатов
for item in fruits:
    if item in passed:
        duplicates.append(item)
    else:
        passed[item] = True
    print(f'Найденные дубликаты: {duplicates}')
