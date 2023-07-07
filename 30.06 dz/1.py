
string1 = "Hello, World!"
string2 = 'I like pyrhon'

print("Длина строки 'Hello, World!':", len(string1))

print("Первый символ строки 'Python is awesome':", string2[0])
print("Последний символ строки 'Python is awesome':", string2[-1])

print("Срез строки 'Hello, World!':", string1[7:12])

print("Индекс первого вхождения 'o' в строку 'Hello, World!':", string1.index('o'))
print("Количество вхождений 'o' в строку 'Hello, World!':", string1.count('o'))

print("Начинается ли строка 'Hello, World!' с 'Hello':", string1.startswith('Hello'))
print("Заканчивается ли строка 'Hello, World!' на 'World!':", string1.endswith('World!'))

new_string = string2.replace('awesome', 'amazing')
print("Строка после замены 'awesome' на 'amazing':", new_string)

string3 = 'one,two,three,four,five'
split_list = string3.split(',')
print("Список после разделения строки 'one,two,three,four,five':", split_list)

joined_string = '-'.join(split_list)
print("Строка после объединения списка ['one', 'two', 'three', 'four', 'five'] с разделителем '-':", joined_string)

print("Строка 'Python is awesome' в верхнем регистре:", string2.upper())
print("Строка 'Python is awesome' в нижнем регистре:", string2.lower())
