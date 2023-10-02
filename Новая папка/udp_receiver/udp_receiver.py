from PyQt6.QtCore import QThread
import socket

class Udp_receiver:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message):
        try:
            self.client_socket.sendto(message.encode('utf-8'), (self.server_address, self.server_port))
        except Exception as e:
            print(f"Error sending message: {str(e)}")

    def receive(self):
        try:
            data, _ = self.client_socket.recvfrom(1024)
            response = data.decode('utf-8')
            return response
        except Exception as e:
            print(f"Error receiving response: {str(e)}")
            return None

if __name__ == "__main__":
    server_address = 'localhost' 
    server_port = 1234567

    client = Udp_receiver(server_address, server_port)

    while True:
        message = input("Enter a message (or 'q' to quit): ")
        if message == 'q':
            break
        client.send(message)
        response = client.receive()
        print(f"Server response: {response}")

    def run(self):
        print('Udp_receiver запущен!')