def decrypt(text):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('а') - 1) % 32 + ord('а'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('А') - 1) % 32 + ord('А'))
        else:
            decrypted_text += char
    return decrypted_text

with open("encrypted_message.txt", "r", encoding="utf-8") as f:
    encrypted_text = f.read()
decrypted_text = decrypt(encrypted_text)
with open("decrypted_message.txt", "w", encoding="utf-8") as f:
    f.write(decrypted_text)
