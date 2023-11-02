import re
class XoViev:
    def show(self,text):
        print (text)

    def show_win(self):
        print("Мои поздравления, вы выиграли!!!!")

    def show_loose(self):
        print("Ну, в этой игре ты проиграл, но ты главное не ной, это же игра;")

    def input(self, char):
        while True:
            move = input(f"ход игрока {char}")
            if re.match(r'^[a-c][1-3]$', move):
                return ord(move[0]) - ord('a'), int(move[1]-1)
            else:
                print('не правильный ввод, попробуйте снова, и введите в формате буква-цифра. Пример a1, b2')
