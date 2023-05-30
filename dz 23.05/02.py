user = input("введите слово из трех букв:")
letter = str(user)
first_char = user [0]
second_char = user [1]
third_char = user [2]
code_sum = ord(first_char) + ord(second_char) + ord(third_char)
print ("сумма кодов для символов =", code_sum)