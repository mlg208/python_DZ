from PyQt6.QtCore import QObject
from logger import Logger
from .gui import Gui
from data_storage import DataStorage
from .udp_receiver import Udp_receiver
from udp_sender import Udp_Server
from contoller import Controller


class Router(QObject):
    def __init__(self):
        super().__init__()
        self.data_storage = DataStorage()
        self.gui = Gui()
        self.udp_receiver = Udp_receiver()
        self.udp_sender = Udp_Server()
        self.controller = Controller()
        # Здесь будем роутить сигналы

        # Сигналы Gui
        self.gui.loginUser.connect(self.data_storage.auth)
        self.gui.loginUser.connect(self.controller.login)

        # Сигналы контроллера
        self.controller.switchWindow.connect(self.gui.set_window)

        # Сигналы Udp ресивера
        self.udp_receiver.message.connect(self.controller.message_received)
        self.gui.sendMessage.connect(self.udp_sender.send)
        
        self.udp_receiver.message.connect(self.gui.show_message)
        

    def start(self):
        Logger.i("Стартуем роутер")
        self.data_storage.start()
        self.gui.start()
        self.udp_receiver.start()
        self.udp_sender.start()

    def stop(self):
        self.udp_sender.stop()
        self.udp_receiver.stop()
        self.gui.stop()
        self.data_storage.stop()
        