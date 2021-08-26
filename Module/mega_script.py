from Module.copy_image import copy_image
from Module.conv_name import conv_name
from Module.edit_photo import edit_photo
from Module.Sort import sort_massive
from Module.retime_metadata import retime_metadata
import datetime
import random

class mega_script:
 def mega_script(save_path, photo_path, name, data,lineedit_fontsize,mode_pic,mode_sort,name_files):
    w = 0
    name_files = []
    while w<len(photo_path):
        name_files.append(str(photo_path[w]).split("\\")[-1].split('.')[0])
        w+=1
    if mode_sort == 1:
            
            _id,name,data,rubbish = sort_massive.sort_massive(name_files,name,data) #TODO НУЖНА ОТДЕЛЬНАЯ ПЕРЕМЕННАЯ ДЛЯ ИМЕНИ ЕКСЕЛЬ И ИМЕНИ СБОРКИ ФАЙЛОВ
            photo_path_demo = []

            i = 0
            while i < len(_id):
                photo_path_demo.append(photo_path[_id[i]])
                i +=1
            photo_path = photo_path_demo
            print('Ненайдены в Excel: ',rubbish)
            w = 0
            name_files = []
            while w<len(photo_path):
                name_files.append(str(photo_path[w]).split("\\")[-1].split('.')[0])
                w+=1
    else:
        rubbish = []
        _id= []
        photo_path_new = []        
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
    edit_photo.edit_photo(save_path, photo_path_new, name_photos, data,lineedit_fontsize,mode_pic)
    retime_metadata.retime_metadata(photo_path,data,photo_path_new)
    return photo_path,name,data,rubbish,_id,photo_path_new
    
