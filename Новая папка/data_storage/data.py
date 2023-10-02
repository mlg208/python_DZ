from PyQt6.QtCore import QThread
from logger import Logger


class DataStorage(QThread):
    username = None
    def run(self):
        Logger.i('DataStorage запущен!')
    
    def auth(self, username):
        self.username - username