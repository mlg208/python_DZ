user_in = input ("сколько сейчас часов")
user_in1 = input("сколько сейчас минут")
try:
    hours = int(user_in)
    minutes = int (user_in1)
except ValueError:
    message = "вы ввели не время"
    print (message)
else:
    hours_remain = 23 - hours
    minutes_remain = 60 - minutes
    print ("осталось", hours_remain,"часов", minutes_remain, "минут")