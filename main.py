import sys
from PyQt6.QtWidgets import QApplication
from router import Router


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    route = Router()
    route.start()

    app.exec()
    