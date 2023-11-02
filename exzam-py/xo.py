import sys 
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
app.start()
exit()