import socket
class XoServer:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = 10102
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