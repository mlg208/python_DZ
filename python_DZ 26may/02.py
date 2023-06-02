user_in = input("введите первое число")
user_in1 = input("введите второе число")
try: 
    num = int(user_in)
    num1 = int(user_in1)
except ValueError:
    message = "вы ввели не числа"
    print (message)
else:
    result = (num + num1) // 2
    print ("среднее арифметическое ваших чисел равно", result)
