num = input("введите любое трехзначное число, но не с одинаковыми цифрами: ")
if num == ("000"):
    print("в вашем числе не должно быть одинаковых цифр!")
elif num ==("111"):
    print("в вашем числе не должно быть одинаковых цифр!")
elif num == ("222"):
    print("в вашем числе не должно быть одинаковых цифр!")
elif num == ("333"):
    print("в вашем числе не должно быть одинаковых цифр!")
elif num ==("444"):
    print("в вашем числе не должно быть одинаковых цифр!")
elif num ==("555"):
    print("в вашем числе не должно быть одинаковых цифр!")
elif num ==("666"):
    print("в вашем числе не должно быть одинаковых цифр!")
elif num ==("777"):
    print("в вашем числе не должно быть одинаковых цифр!")
elif num == ("888"):
    print("в вашем числе не должно быть одинаковых цифр!")
elif num ==("999"):
    print("в вашем числе не должно быть одинаковых цифр!")
else:
    print("вы ввели неверные значения, повторите попытку!")

# VN: Все эти условия можно заменить одним:
# if num[0] == num[1] == num[2]:

# Но в задаче нужно сделать немного другое - узнать, есть ли в числе хотя бы две одинаковых цифры.
# Подумайте, как нужно изменить условие для этого