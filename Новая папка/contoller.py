from PyQt6.QtCore import QObject, pyqtSignal
from logger import Logger

class Controller(QObject):
    _state = "INIT"
    _transitions = (
        {'from': "INIT",     'to': "LOGIN",       'by': "DB_READY"},
        {'from': "LOGIN",    'to': "AUTH",        'by': "GUI_LOGIN"},
        {'from': "AUTH",     'to': "MAIN_WIN",    'by': "DB_AUTH_OK"},
        {'from': "AUTH",     'to': "LOGIN",       'by': "DB_AUTH_BAD"},

        {'from': "MAIN_WIN", 'to': "ADD_FRIEND",  'by': "UR_HELLO"},
        {'from': "ADD_FRIEND", 'to': "MAIN_WIN",  'by': "IMMEDIATELY"},

        {'from': "MAIN_WIN",  'to': "CHECK_MSG",  'by': "UR_MESSAGE"},
        {'from': "CHECK_MSG", 'to': "MAIN_WIN",  'by': "IMMEDIATELY"},

        {'from': "MAIN_WIN",  'to': "SEND_MSG",  'by': "GUI_SEND"},
        {'from': "GUI_SEND",  'to': "MAIN_WIN",  'by': "IMMEDIATELY"},

        {'from': "MAIN_WIN",  'to': "CHANGING_CHAT", 'by': "GUI_CHAT_CHANGE"},
        {'from': "CHANGING_CHAT",  'to': "MAIN_WIN",  'by': "IMMEDIATELY"}

    )

    def process_state(self):
        match self.state:
            case "INIT":
                pass
            case "LOGIN":
                pass
            case "AUTH":
                pass
            case "MAIN_WIN":
                pass

            case _:
                Logger.w("Unknown state!")


    def process_signal(self, signal_name):
        # Здесь фильтруем из таблицы переходов те, в которых поле 'from' соответствует
        # текущему сотоянию. Затем из них фильруем те переходы, в которых поле 'by'
        # соответствует signal_name. И если такой переход есть, меняем текущее состояние
        # и вызываем process_state()
        pass



    




    switchWindow = pyqtSignal(str, str)
    def login(self, username):
        if username:
            self.switchWindow.emit('MainWindow', username)

    def message_received(self, message_text, message_type):
        Logger.d(f'получили сообщение: {message_text} тип: {message_type}')
