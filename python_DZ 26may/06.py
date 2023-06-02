user_in = input ("введите число a")
user_in1 = input ("введите число b")
try:
    a = int (user_in)
    b = int (user_in1)
except ValueError:
    message = "вы ввели не цифровые значения!"
    print (message)
else:    
    x = b/a
    print (x)