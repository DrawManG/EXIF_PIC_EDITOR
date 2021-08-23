from Module.copy_image import copy_image
from Module.conv_name import conv_name
from Module.edit_photo import edit_photo

import datetime
import random
import os
import time

class mega_script:
 def mega_script(save_path, photo_path, name, data,lineedit_fontsize,mode_pic):
    i=0
    while i < len(photo_path):
        print('до изменения  ' +str(data[i]))
        converted_date = datetime.datetime.strptime(data[i], '%Y.%m.%d %H:%M:%S')
        converted_date = converted_date + datetime.timedelta(minutes=random.randint(2,5))
        data[i] = str(converted_date).replace('-','.')
        print('После изменения  ' + str(data[i]))
        if int(converted_date.hour) >= 22 and int(converted_date.hour) <= 24:
            print('Дата после 22 найдена:  '+ data[i])
            converted_date = datetime.datetime.strptime(data[i], '%Y.%m.%d %H:%M:%S')
            new_hour,new_minute,new_second = str("{0:0=2d}".format(random.randint(8, 9))),\
                                             str("{0:0=2d}".format(random.randint(0, 59))),\
                                             str("{0:0=2d}".format(random.randint(0, 59)))
            y, m, d = converted_date.year, converted_date.month, converted_date.day
            data[i] = datetime.datetime.strptime(
                str(y) + "." + str(m) + "." + str(d) + " " + str(new_hour) + ":" + str(new_minute) + ":" + str(
                    new_second), '%Y.%m.%d %H:%M:%S')

            data[i] = str(data[i] + datetime.timedelta(days=1)).replace('-','.')
            print('Дата изменена на: ' + data[i])
        if int(converted_date.hour) >= 0 and int(converted_date.hour) < 8:
            print('Дата с 0 до 8 найдена: '+ data[i])
            converted_date = datetime.datetime.strptime(data[i], '%Y.%m.%d %H:%M:%S')
            new_hour, new_minute, new_second = str("{0:0=2d}".format(random.randint(8, 9))), \
                                               str("{0:0=2d}".format(random.randint(0, 59))), \
                                               str("{0:0=2d}".format(random.randint(0, 59)))
            y,m,d = converted_date.year,converted_date.month,converted_date.day

            data[i] = str(datetime.datetime.strptime(str(y)+"."+str(m)+"."+str(d)+" "+str(new_hour)+":"+str(new_minute)+":"+str(new_second), '%Y.%m.%d %H:%M:%S')).replace('-','.')
            print('Дата изменена на: ' + data[i])
        i=i+1
    name_photos = conv_name.conv_name(photo_path,data) 
    photo_path_new = copy_image.copy_image(save_path, photo_path, name_photos)
    if not mode_pic == 1:
        edit_photo.edit_photo(save_path, photo_path_new, name_photos, data,lineedit_fontsize)
    i = 0
    while i < len(photo_path_new):
        pattern = '%Y.%m.%d %H:%M:%S'
        epoch = int(time.mktime(time.strptime(data[i], pattern)))
        from win32_setctime import setctime
        setctime(photo_path_new[i], epoch)
        os.utime(photo_path_new[i], (epoch, epoch))
        i = i + 1
