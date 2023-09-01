def extract_emails(text):
    emails = []
    i = 0
    while i < len(text):
        if text[i] == "@":
            start = i - 1
            while start >= 0 and (text[start].isalnum() or text[start] in "-._"):
                start -= 1
            start += 1

            end = i + 1
            while end < len(text) and (text[end].isalnum() or text[end] in "-._"):
                end += 1

            #VN: очень неплохой алгоритм. У него есть небольшой недостаток, например
            # something@ , @something или просто @  -- будут считаться валидными адресами email.
            # Также он будет считать адресом something@something, хотя в нём нет точки с именем домена

            emails.append(text[start:end])
            i = end
        else:
            i += 1
    return emails


with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()
email_addresses = extract_emails(text)
email_string = ", ".join(email_addresses)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(email_string)

print("Адреса электронной почты извлечены и сохранены в output.txt")
