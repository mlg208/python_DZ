user_in = input ("сколько сейчас часов")
hours = int(user_in)
user_in1 = input("сколько сейчас минут")
minutes = int (user_in1)
hours_remain = 23 - hours
minutes_remain = 60 - minutes
print ("осталось", hours_remain,"часов", minutes_remain, "минут")