import re

def extract_dates(text):
    date_pattern = r'\b(\d{2}[./]\d{2}[./]\d{4})\b'

    dates = re.findall(date_pattern, text)

    return dates

text = """
Завтра встреча запланирована на 25/10/2023.
А послезавтра на 01.11.2023.
Сегодня 15.09.2023, а вчера было 14/09/2023.
"""

date_list = extract_dates(text)

if date_list:
    print("Найденные даты:")
    for date in date_list:
        print(date)
else:
    print("Даты не найдены.")
