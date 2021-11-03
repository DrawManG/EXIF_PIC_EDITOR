

from PyQt5.QtWidgets import QApplication
import sys
from Interface.Main_interface import App 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = App()
    sys.exit(app.exec_())