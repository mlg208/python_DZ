def encrypt(text):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('а') + 1) % 32 + ord('а'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('А') + 1) % 32 + ord('А'))
        else:
            encrypted_text += char
    return encrypted_text

input_text = "Мощная армия дуболомов Урфина Джюса уже третий день осаждает Изумрудный город."
encrypted_text = encrypt(input_text)
with open("encrypted_message.txt", "w", encoding="utf-8") as f:
    f.write(encrypted_text)
