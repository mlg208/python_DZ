import socket
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