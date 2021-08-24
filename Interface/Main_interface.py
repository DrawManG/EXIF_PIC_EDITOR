from PyQt5.QtWidgets import QMainWindow

from Interface.PhotoData import PhotoData

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        #self.title =
        self.left = 100
        self.top = 30
        self.width = 700
        self.height = 200
        self.setWindowTitle("Редактор методанных фото V.2")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.PhotoData = PhotoData()
        self.setCentralWidget(self.PhotoData)
        self.show()