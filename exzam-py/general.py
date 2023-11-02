import sys
import re
class XoModel:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]

    def is_empty(self, row, col):
        return self.grid[row][col] == ' '

    def set(self, row, col, char):
        self.grid[row][col] = char

    def row(self, row):
        return tuple(self.grid[row])

    def col(self, col):
        return tuple(self.grid[i][col] for i in range(self.size))

    def diag(self, direction):
        if direction == 1:
            return tuple(self.grid[i][i] for i in range(self.size))
        elif direction == -1:
            return tuple(self.grid[i][self.size - 1 - i] for i in range(self.size))

    def __str__(self):
        board = []
        for i in range(self.size):
            board_row = ' | '.join(self.grid[i])
            board.append(f'{i + 1} | {board_row} |')
        col_numbers = '   ' + '   '.join(str(i + 1) for i in range(self.size))
        separator = '\n  +---' + '---' * (self.size - 1) + '---+'
        return f'    {col_numbers}\n{separator}\n{separator}\n{separator}\n'.join(board)


class XoView:
    def show(self, text):
        print(text)

    def show_win(self):
        print("Поздравляю, вы выиграли!")

    def show_loose(self):
        print("Вы проиграли. Попробуйте ещё раз!")

    def input(self, char):
        while True:
            move = input(f"Ход игрока {char}: ")
            if re.match(r'^[a-c][1-3]$', move):
                return ord(move[0]) - ord('a'), int(move[1]) - 1
            else:
                print("Некорректный ввод. Введите ход в формате 'буквацифра', например: 'b2'.")


import socket

class XoServer:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.hostname, self.port))

    def char_response(self, char):
        self.socket.sendto(char.encode(), (self.client_address))

    def send(self, row, col):
        move = f"{row}{col}"
        self.socket.sendto(move.encode(), (self.client_address))

    def receive(self):
        data, addr = self.socket.recvfrom(1024)
        self.client_address = addr
        return int(data.decode())


class XoClient:
    def __init__(self, server_hostname, server_port):
        self.server_hostname = server_hostname
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def char_request(self):
        request = "CHAR_REQUEST"
        self.socket.sendto(request.encode(), (self.server_hostname, self.server_port))
        data, _ = self.socket.recvfrom(1024)
        return data.decode()

    def send(self, row, col):
        move = f"{row}{col}"
        self.socket.sendto(move.encode(), (self.server_hostname, self.server_port))

    def receive(self):
        data, _ = self.socket.recvfrom(1024)
        return int(data.decode())


from app import XoApplication

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Неправильное количество аргументов или ошибка ввода")
        sys.exit(1)

size = int(sys.argv[1])
mode = sys.argv[2]
hostname = sys.argv[3]
char = sys.argv[4]

app = XoApplication(size, mode, hostname, char)
app.start
exit()



















# Пример использования:
# server = XoServer('localhost', 10101)
# char = server.receive()
# server.send(1, 2)
# move = server.receive()
# server.char_response('X')








# Пример использования:
# client = XoClient('localhost', 10101)
# char = client.char_request()
# client.send(1, 2)
# move = client.receive()