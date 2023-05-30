user = input("введите любое слово: ")
word = str(user)
midpoint = len(word) // 2
first_half = word[:midpoint]
second_half = word[midpoint:]
print ("первая половина", first_half)
print ("вторя половина", second_half)