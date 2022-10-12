
from sys import path

from PyQt5.QtGui import QIntValidator
from Module.create_excel import create_excel
from Module.mega_script import mega_script
from Module.make_photo_array import make_photo_array
from Module.read_xls import read_xls
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QRadioButton, QVBoxLayout, QWidget, QLineEdit, QFileDialog, QPushButton, QGridLayout, QMessageBox, QLabel, QComboBox, QCheckBox
import os
import PIL




class PhotoData(QWidget):
    def __init__(self):
        super().__init__()
        self.dates = [] 
        self.photos = []  
        self.photos_dir = ""
        self.names = []  
        self.names_FILES = []
        self.mode_PIC = 0
        self.mode_SORT = 0
        self._create_UI()
        self.mode = 1
        self.button_open_excel.clicked.connect(self.open_excel)
        self.button_dir_photo.clicked.connect(self.choose_photo_dir)
        self.button_process.clicked.connect(self.proccessing)
        self.switch_mode_EXIF.clicked.connect(self.switch_modeE)
        self.switch_mode_XLS.clicked.connect(self.switch_modeX)
        self.combo.activated.connect(self.clean_combo)
        self.type_sheep = "None"

    
        
    def _create_UI(self):

        self.layout = QGridLayout(self)
        self.button_open_excel = QPushButton("Открыть файл excel")
        self.excel_path = QLineEdit()
        self.excel_path.setEnabled(False)
        self.combo = QComboBox()
        self.combo.addItems(["Стабилометр", "Срез", "Компрессия","Консолидация"])
        self.len_datas = QLabel("Найдено образцов: ")
        self.button_dir_photo = QPushButton("Выбрать папку с фото")
        self.photo_path = QLineEdit()
        self.photo_path.setEnabled(False)
        self.len_photo = QLabel("Найдено фото: ")
        self.button_process = QPushButton("Перебить даты")
        self.lbl_fontsize = QLabel("Размер шрифта: ")
        self.lineedit_fontsize = QLineEdit("50")
        self.lineedit_fontsize.setValidator(QIntValidator())
        self.lbl_switch = QLabel("Режимы:")
        self.switch_mode_XLS = QRadioButton("XLS")
        self.switch_mode_EXIF = QRadioButton("EXIF")
        self.switch_mode_PIC = QCheckBox("ONLY PIC")
        self.switch_mode_SORT = QCheckBox("Sort")
        #self.switch_mode_EXIF.setChecked(True)
        self.switch_mode_XLS.setChecked(True)

        #self.switch_mode_XLS.setChecked(True)

        self.aggregation = QHBoxLayout()
        self.aggregation.addWidget(self.lbl_switch)
        self.aggregation.addWidget(self.switch_mode_XLS)
        self.aggregation.addWidget(self.switch_mode_EXIF)
        self.aggregation.addWidget(self.switch_mode_PIC)
        self.aggregation.addWidget(self.switch_mode_SORT)
        

        self.layout.addWidget(self.button_open_excel, 0, 0)
        self.layout.addWidget(self.combo, 0, 1)
        self.layout.addWidget(self.excel_path, 0, 2)
        self.layout.addWidget(self.len_datas, 0, 3)
        self.layout.addWidget(self.button_dir_photo, 1, 0)
        self.layout.addWidget(self.photo_path, 1, 1, 1, 2)
        self.layout.addWidget(self.len_photo, 1, 3)
        self.layout.addWidget(self.button_process, 3, 0)
        self.layout.addWidget(self.lbl_fontsize,2,0)
        self.layout.addWidget(self.lineedit_fontsize,2,1)
        self.layout.addLayout(self.aggregation,2,2)

    def switch_modeE(self):
        self.button_open_excel.setEnabled(False)
        self.combo.setEnabled(False)
        self.len_datas.setEnabled(False)
        self.switch_mode_SORT.setEnabled(False)
 
    
    def switch_modeX(self):
        self.button_open_excel.setEnabled(True)
        self.combo.setEnabled(True)
        self.len_datas.setEnabled(True)
        self.switch_mode_SORT.setEnabled(True)

    def clean_combo(self):
        try:
            #self.photos = []
            excel_file = self.excel_path.text()
            self.len_datas.setText("Найдено образцов: ")
            self.excel_path.setText("")
            self.dates = [] 
            if excel_file and excel_file.endswith('.xls'):
                self.names, self.dates =  read_xls.read_xls(excel_file, self.combo.currentText())
                self.excel_path.setText(excel_file)
                self.len_datas.setText("Найдено образцов: " + str(len(self.dates)))
        except:
                m = QMessageBox()
                m.setText("То, что вы выбрали, нету в Excel! Посмотрите Excel и сверьте с выбором.")
                m.exec()
                self.excel_path.setText(excel_file)
                self.combo.setCurrentIndex(0)
                self.clean_combo()
        
    def clean_DataBase(self):
        self.len_datas.setText("Найдено образцов: ")
        self.len_photo.setText("Найдено фото: ")
        self.excel_path.setText("")
        self.photo_path.setText("")
        self.dates = [] 
        self.photos = []  
        self.photos_dir = ""
        self.names = []  



    def cleaner(self):
        super().__init__()
        self.len_datas.setText("Найдено образцов: ")
        self.len_photo.setText("Найдено фото: ")
        self.excel_path.setText("")
        self.photo_path.setText("")
        self.dates = [] 
        self.photos = []  
        self.photos_dir = ""
        self.names = []  



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
        if self.switch_mode_XLS.isChecked() == True:
            if self.switch_mode_SORT.isChecked() == True:
                self.mode_SORT = 1
            else:
                self.mode_SORT = 0

        if self.switch_mode_XLS.isChecked() == True:
            self.mode = 1
        else:
            self.mode = 0
        if self.switch_mode_EXIF.isChecked() == True:
            self.mode = 0
        else:
            self.mode = 1
        
        if self.switch_mode_PIC.isChecked() == True:
            self.mode_PIC = 1
        else:
            self.mode_PIC = 0
        try:
            if not self.lineedit_fontsize.text() == "":
                if int(self.lineedit_fontsize.text()) > 55 or int(self.lineedit_fontsize.text()) < 10:
                    m = QMessageBox()
                    m.setText("У вас не правильно выставлен размер шрифта, он начинается от 10 и заканчивается 55. Если у вас его нет, то поставьте")
                    m.exec()
                    return
            else: 
                m = QMessageBox()
                m.setText("Введите размер шрифта")
                m.exec()
                return
        except: 
                    m = QMessageBox()
                    m.setText("УФ, не учёл такой момент,ставлю 50 шрифт, шрифт ставится от 10 до 55")
                    m.exec()
                    self.lineedit_fontsize.setText(str(50))
        if not str(self.lineedit_fontsize.text()) == "":
            self.type_sheep = str(self.lineedit_fontsize.text())
        else:
            self.type_sheep = "EXIF-type"

        if len(self.photos) == 0:
            m = QMessageBox()
            m.setText("Отсутствуют фото")
            m.exec()
            return
        elif len(self.dates) == 0 and self.mode == 1:
            m = QMessageBox()
            m.setText("Отсутствуют образцы")
            m.exec()
            return
        elif self.mode == 0: # exif TODO
            self.mode_SORT = 0
            self.dates = self.exif_dates()
            self.names_FILES = self.self_names_for_exif()
            save_path = self.photos_dir + "/modified/" 
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            if not self.mode_SORT == 0:
                self.megascript_path,self.megascript_name,self.megascript_data,self.megascript_rubbish,self._id,self.megascript_path_new = mega_script.mega_script(save_path, self.photos, self.names , self.dates, self.type_sheep,self.mode_PIC,self.mode_SORT,self.names_FILES)
                i = 0
                self.old_name = []
                while i < len(self.megascript_path_new):
                    print(i,len(self._id),self._id,self.megascript_path_new)
                    self.old_name.append(str(self.megascript_path_new[i]).split("/")[-1].split(".")[0])
                    i+=1 
                create_excel.create_excel(self,self.megascript_name,self.megascript_data,save_path,self.combo.currentText(),self.old_name)
                m = QMessageBox()
                m.setText("Готово, не найдено в файле Excel: "+str(self.megascript_rubbish))
                m.exec()
            else:
                self.names = self.names_FILES
                mega_script.mega_script(save_path, self.photos, self.names_FILES , self.dates, self.type_sheep,self.mode_PIC,self.mode_SORT,self.names_FILES)
                create_excel.create_excel(self,self.names_FILES,self.dates,save_path,"EXIF",self.names_FILES)
                m = QMessageBox()
                m.setText("Готово")
                m.exec()
            old_path = self.excel_path.text()
            self.switch_mode_XLS.setChecked(True)
            self.button_open_excel.setEnabled(True)
            self.combo.setEnabled(True)
            self.len_datas.setEnabled(True)
            self.cleaner()
            self.excel_path.setText(old_path)
            self.clean_combo()
            self.switch_mode_EXIF.setChecked(True)
            self.button_open_excel.setEnabled(False)
            self.combo.setEnabled(False)
            self.len_datas.setEnabled(False)
        else:
            if self.mode_SORT == 0:
                if len(self.dates) < len(self.photos):
                    m = QMessageBox()
                    m.setText("У вас в EXCEL ячеек меньше, чем фотографий, исправьте пожалуйста!")
                    m.exec()
                    return
                    
            save_path = self.photos_dir + "/modified/"
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            self.megascript_path,self.megascript_name,self.megascript_data,self.megascript_rubbish,self._id,self.megascript_path_new = mega_script.mega_script(save_path, self.photos, self.names , self.dates, self.type_sheep,self.mode_PIC,self.mode_SORT,self.names_FILES)
            m = QMessageBox()
            i = 0
            self.old_name = []
            while i < len(self.megascript_path_new):
                
                    self.old_name.append(str(self.megascript_path_new[i]).split("/")[-1].split(".")[0])
                    i+=1 

            create_excel.create_excel(self,self.megascript_name,self.megascript_data,save_path,self.combo.currentText(),self.old_name)
            m.setText("Готово, не найдено в файле Excel: "+str(self.megascript_rubbish))
            m.exec()
            old_path = self.excel_path.text()
            self.switch_mode_XLS.setChecked(True)
            self.button_open_excel.setEnabled(True)
            self.combo.setEnabled(True)
            self.len_datas.setEnabled(True)
            self.cleaner()
            self.excel_path.setText(old_path)
            self.clean_combo()

    def self_names_for_exif(self):
        i = 0
        name_out_path = []
        while i < len(self.photos):
            img_path = str(self.photos[i])
            img_name = img_path.split("\\")[-1]
            name_out_path.append(img_name.split(".")[0])
            i+=1
        return name_out_path

    def exif_dates(self):
        try:
            data_base = []
            i=0
            while i < len(self.photos):
                img = PIL.Image.open(self.photos[i])
                exif_full = img._getexif()[36867]
                year_mouth_day,house_minute_second = str(exif_full).split(' ')
                year_mouth_day = year_mouth_day.replace(":",".")
                data_base.append(year_mouth_day+" "+house_minute_second)
                i+=1
            return data_base
        except Exception as Error:
            print("В списке картинок, есть картинка, которая не имеет Exif. Подробнее: ",Error)
            