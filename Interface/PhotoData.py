from Module.mega_script import mega_script
from Module.make_photo_array import make_photo_array
from Module.read_xls import read_xls
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLineEdit, QFileDialog, QPushButton, QGridLayout, QMessageBox, QLabel, QComboBox
import os




class PhotoData(QWidget):
    def __init__(self):
        super().__init__()
        self.dates = [] 
        self.photos = []  
        self.photos_dir = ""
        self.names = []  
        self._create_UI()
        self.button_open_excel.clicked.connect(self.open_excel)
        self.button_dir_photo.clicked.connect(self.choose_photo_dir)
        self.button_process.clicked.connect(self.proccessing)

    def _create_UI(self):
        self.layout = QGridLayout(self)
        self.button_open_excel = QPushButton("Открыть файл excel")
        self.excel_path = QLineEdit()
        self.excel_path.setEnabled(False)
        self.combo = QComboBox()
        self.combo.addItems(["Стабилометр", "Срез", "Компрессия","Консолидация"])
        self.len_datas = QLabel("Найдено образцов:   ")
        self.button_dir_photo = QPushButton("Выбрать папку с фото")
        self.photo_path = QLineEdit()
        self.photo_path.setEnabled(False)
        self.len_photo = QLabel("Найдено фото: ")
        self.button_process = QPushButton("Перебить даты")

        self.layout.addWidget(self.button_open_excel, 0, 0)
        self.layout.addWidget(self.combo, 0, 1)
        self.layout.addWidget(self.excel_path, 0, 2)
        self.layout.addWidget(self.len_datas, 0, 3)
        self.layout.addWidget(self.button_dir_photo, 1, 0)
        self.layout.addWidget(self.photo_path, 1, 1, 1, 2)
        self.layout.addWidget(self.len_photo, 1, 3)
        self.layout.addWidget(self.button_process, 2, 0)

    def open_excel(self):
        self.dates = list([])
        self.names = list([])
        excel_file = QFileDialog.getOpenFileName(self, 'Open file')[0]
        if excel_file and excel_file.endswith('.xls'):
            self.names, self.dates =  read_xls.read_xls(excel_file, self.combo.currentText())
            self.excel_path.setText(excel_file)
            self.len_datas.setText("Найдено образцов: " + str(len(self.dates)))

    def choose_photo_dir(self):
        self.photos_dir = QFileDialog.getExistingDirectory(self, "Select Directory")
        if self.photos_dir:
            self.photos = make_photo_array.make_photo_array(self.photos_dir)

            self.photo_path.setText(self.photos_dir)
            self.len_photo.setText("Найдено фото: " + str(len(self.photos)))

    def proccessing(self):
        if len(self.photos) == 0:
            m = QMessageBox()
            m.setText("Отсутствуют фото")
            m.exec()
        elif len(self.dates) == 0:
            m = QMessageBox()
            m.setText("Отсутствуют образцы")
            m.exec()
        else:

            save_path = self.photos_dir + "/modified/"

            if not os.path.exists(save_path):
                os.mkdir(save_path)
            mega_script.mega_script(save_path, self.photos, self.names, self.dates)
            m = QMessageBox()
            m.setText("Готово")
            m.exec()