import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails = re.findall(email_pattern, text)
    return emails

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()
email_addresses = extract_emails(text)
email_string = ", ".join(email_addresses)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(email_string)

print("Адреса электронной почты извлечены и сохранены в output.txt")
