user_in = input("введите километры")
try:
    km = int (user_in)
except ValueError:
    message = "вы явно ввели не километры, попробуйте снова"
    print (message)
else:
    ml = km  * 0.621371
    print ("ваши километры равны", ml, "милям")