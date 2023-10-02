from PyQt6.QtCore import QThread

import socket
import threading

class Udp_Server:
    def __init__(self, port):
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(('0.0.0.0', self.port))
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"UDP Server started on port {self.port}")
        while self.is_running:
            try:
                data, addr = self.server_socket.recvfrom(1024)
                message = data.decode('utf-8')
                print(f"Received message from {addr}: {message}")
                self.server_socket.sendto("OK".encode('utf-8'), addr)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {str(e)}")

    def stop(self):
        self.is_running = False
        self.server_socket.close()
        print("UDP Server stopped")
def run(self):
    print('Udp_sender запущен!')

