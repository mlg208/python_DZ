user = input("введите название фильма: ")
user1 = input("введите название кинотеатра ")
user2 = input("введите время вашего фильма ")
Name = str (user)       # VN: не нужно
teatre = str (user1)    # строку переводить
time = str (user2)      # в строку!

# VN: Здесь лучше использовать операцию подстановки - %
ticket = (Name) + " в " + (teatre) + " на "+ (time)
#        ^    ^           ^      ^           ^    ^   бессмысленные скобки
print ("ваш билет на" , ticket, "забронирован")