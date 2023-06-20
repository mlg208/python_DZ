user = input("введите любое ваше слово:")
word = str(user)  # VN: не нужно строку переводить в строку!
if len(word) >= 2:
    reduction = word[:2] + "-" + word[-2:]  
    print ("сокращение вашего слово это ", reduction)
else:
    print("слово состоит менее чем из двух символов")