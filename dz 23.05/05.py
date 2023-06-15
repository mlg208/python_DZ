word = input("Введите слово: ")
censored_word = word[0] + '*' * (len(word) - 2) + word[-1]
print("Зацензуренное слово:", censored_word)