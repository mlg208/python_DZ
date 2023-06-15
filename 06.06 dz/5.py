import random

def get_random_int(min_val, max_val):
    result = random.randint(min_val, max_val)
    return result

def game(my_random, min_val, max_val):
    user_in = input("Угадайте число от {} до {}: ".format(min_val, max_val))
    try:
        user_num = int(user_in)
    except ValueError:
        print("Пожалуйста, введите целое число.")
        game(my_random, min_val, max_val)
    else:
        if my_random > user_num:
            print("Неверно! Загаданное число больше ;)")
            game(my_random, min_val, max_val)
        elif my_random < user_num:
            print("Неверно! Загаданное число меньше ;)")
            game(my_random, min_val, max_val)
        else:
            print("Поздравляем! Вы угадали число {}!".format(my_random))
            play_again()

def play_again():
    answer = input("Хотите сыграть еще раз? (да/нет): ")
    if answer.lower() == "да":
        num = get_random_int(0, 20)
        game(num, 0, 20)
    else:
        print("Спасибо за игру! До свидания.")

num = get_random_int(0, 20)
game(num, 0, 20)
