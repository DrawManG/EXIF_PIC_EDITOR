import time
import os
from win32_setctime import setctime

class retime_metadata:
    def retime_metadata(photo_path,data,photo_path_new):
        i=0
        while i < len(photo_path):
            pattern = '%Y.%m.%d %H:%M:%S'
            epoch = int(time.mktime(time.strptime(data[i], pattern)))
            setctime(photo_path_new[i], epoch)
            os.utime(photo_path_new[i], (epoch, epoch))
            i = i + 1