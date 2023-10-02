import sys
import threading
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QFileDialog

class WorkerThread(QObject):
    finished = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            self.finished.emit(content)
        except Exception as e:
            self.finished.emit(str(e))

def open_file(self):
    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text Files (*.txt);;All Files (*)", options=options)
    if file_path:
        self.worker_thread.run(file_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Чтение файла в потоке")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        open_button = QPushButton("Открыть", self)
        open_button.clicked.connect(self.open_file)
        layout.addWidget(open_button)

        central_widget.setLayout(layout)

        self.worker_thread = WorkerThread()
        self.worker_thread.finished.connect(self.update_text_edit)

    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            self.worker_thread.run(file_path)

    def update_text_edit(self, content):
        self.text_edit.setPlainText(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
