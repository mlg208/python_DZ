user_in = input("введите число, для возведения второй степени")
try:
    num = int (user_in)
except ValueError:
    message = "вы ввели неправильные данные"
    print (message)
else:
    result = num ** 2
    print ("ваше число во второй степени равняется", result)