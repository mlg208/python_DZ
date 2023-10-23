import re
#определить текущий курс 
usd_to_kzt = 426.5  
eur_to_kzt = 506.8  

def convert_currency(match):
    amount = float(match.group(1))
    currency = match.group(2)
    if currency == '$' or currency == 'USD':
        converted = round(amount * usd_to_kzt, 2)
        return f'{converted} ₸'
    elif currency == '€' or currency == 'EUR':
        converted = round(amount * eur_to_kzt, 2)
        return f'{converted} ₸'

input_filename = 'input.txt'  
output_filename = 'output.txt'

with open(input_filename, 'r', encoding='utf-8') as file:
    text = file.read()

pattern = r'(\d+\.\d+)\s*([$€]|USD|EUR)'

converted_text = re.sub(pattern, convert_currency, text)

with open(output_filename, 'w', encoding='utf-8') as output_file:
    output_file.write(converted_text)

print(f'Конверсия завершена. Результат сохранен в {output_filename}')
