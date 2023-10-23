import re

def is_valid_email(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.search(email_pattern, email):
        return True
    else:
        return False

email = "example@123email.com"
if is_valid_email(email):
    print(f"{email,} - это валидный адрес электронной почты.")
else:
    print(f"{email, } - это невалидный адрес электронной почты.")
