from logger import log
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
from message import Message


class MainWindow(QMainWindow):
    sendMessage = pyqtSignal(str)

    def __init__(self, username):
        super().__init__()
        uic.loadUi("gui/main.ui", self)
        self.username = username
        self.contact_list = []
        
    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Send")
        button.clicked.connect(self.send_message)
        self.add_contact("General")

    def send_message(self):
        log.d("Кнопка нажата")
        textedit = self.findChild(QTextEdit, "MessageToSend")
        message = textedit.toPlainText()
        self.sendMessage.emit(message)
        textedit.clear()

    def show_message(self, msg : Message):
        display = self.findChild(QTextBrowser, 'MessageDisplay')
        display.append(f"{msg.time}|  {msg.senderName}:  {msg.text}")
        
    def add_contact(self, name_contact):
        contactlist = self.findChild(QVBoxLayout, "ContactList")
        newcontact = QLabel(text=name_contact)
        contactlist.addWidget(newcontact)
        self.contact_list.append(name_contact)
        