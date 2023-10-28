import re
from datetime import datetime, timedelta

def convert_dates(text):
    def repl(match):
        date_str = match.group(0)
        try:
            # узнаем датн из данного текста
            date_obj = datetime.strptime(date_str, "%d.%m.%Y")
            
            if date_obj >= datetime(date_obj.year, 2, 14):
                date_obj = date_obj + timedelta(days=13)  

            new_date_str = date_obj.strftime("%d.%m.%Y")
            return new_date_str
        except ValueError:
            return date_str  

    date_pattern = r'\d{2}[-.]\d{2}[-.]\d{4}'
    updated_text = re.sub(date_pattern, repl, text)
    return updated_text

old_style_text = "Эта книа была написана 05.10.1916 года и издана 20.01.1917 года."
new_style_text = convert_dates(old_style_text)
print(new_style_text)
