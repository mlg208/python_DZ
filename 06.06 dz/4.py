import random

def get_random_int(min_val, max_val):
    result = random.randint(min_val, max_val)
    return result

def game(my_random, min_val, max_val, attempts):
    if attempts == 0:
        print("У вас закончились попытки. Загаданное число было", my_random)
        return
    
    user_in = input("Угадайте число от {} до {}: ".format(min_val, max_val))
    try:
        user_num = int(user_in)
    except ValueError:
        print("Пожалуйста, введите целое число.")
        game(my_random, min_val, max_val, attempts)
    else:
        if my_random > user_num:
            print("Неверно! Загаданное число больше ;)")
        elif my_random < user_num:
            print("Неверно! Загаданное число меньше ;)")
        else:
            print("Поздравляем! Вы угадали число {}!".format(my_random))
            return
        
        game(my_random, min_val, max_val, attempts - 1)

num = get_random_int(0, 20)
game(num, 0, 20, 7)
