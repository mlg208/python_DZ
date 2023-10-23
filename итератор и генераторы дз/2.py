import re

def find_phone_numbers(text):
    phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'

    phone_numbers = re.findall(phone_pattern, text)

    return phone_numbers

text = """
Звоните мне по номеру 123-456-7890 или 555.555.5555 в любое время.
Мой второй номер: 9876543210.
"""

phone_numbers = find_phone_numbers(text)

if phone_numbers:
    print("Найденные номера телефонов:")
    for phone in phone_numbers:
        print(phone)
else:
    print("Номеры телефонов не найдены.")
