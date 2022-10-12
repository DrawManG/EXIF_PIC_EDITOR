from Module.get_all_files import get_all_files
import os
import random

class make_photo_array:
 def make_photo_array(dir):
    photos = get_all_files.get_all_files(dir)

    '''
    Исправление бага... в названии файла если встречаются !"№;%:*?)*_)(+_ эти символы, то сбивается читка изображения...
    чтоб это исправить и нужен фикс еррор нейм, который их уберёт 
    '''
    def fix_error_name(photos):
        #--- EDIT NAME DUBLICAT ----
        try:
            i = 0
            name = []
            while i < len(photos):
                name.append(photos[i].split('\\')[-1])
                i+=1

            i=0
            cli = 0
            dub_photos = []

            while i < len(name):

                name_tmp = name
                namei = name[i]
                name_tmp[i] = '--'
                if namei in name:
                    print('dublicate: ',namei)
                    cli += 1
                    dub_photos.append(photos[i])

                else:
                    name_tmp[i] = namei
                i+=1

            num = 0
            while num < len(dub_photos):
                path = str(dub_photos[num])
                path_dev = path.split('\\')
                name, format = path.split('\\')[-1].split(".")
                new_name = name + str(random.randint(0,999))
                full_name = new_name + '.' + format
                path_num = 0
                new_path = ''

                while path_num < len(path_dev):

                    if not path_num == len(path_dev) - 1:
                        new_path += path_dev[path_num] + '\\'
                    else:
                        new_path += str(full_name)
                    path_num += 1


                os.rename(os.path.join(path), os.path.join(new_path))
                dub_photos[num] = new_path
                num += 1
                print('renamed dublicate: ',dub_photos)


                num+=1

            photos = get_all_files.get_all_files(dir)
        except:
            pass








        #---------------------------
        num = 0
        symbols = list('!@#$%^&*()+-="№;:?*')
        print('Дo -> После')
        while num < len(photos):
            new_name=''
            path = str(photos[num])
            path_dev = path.split('\\')
            name,format = path.split('\\')[-1].split(".")


            syb = 0

            while syb < len(symbols):
                        if symbols[syb] in name:
                            name = str(name).replace(symbols[syb],'')




                        syb +=1


            full_name = name+'.'+format
            path_num = 0
            new_path = ''

            while path_num < len(path_dev):

                if not path_num == len(path_dev) - 1 :
                        new_path += path_dev[path_num] + '\\'
                else:
                        new_path += str(full_name)
                path_num+=1
            if photos[num] != new_path:
                print(photos[num],'->',new_path)
            os.rename(os.path.join(path),os.path.join(new_path))
            photos[num] = new_path
            num+=1
        return photos
    photos = fix_error_name(photos)
    def sort_func(s, begin=-8, end=-4):
        if s.upper().endswith(".JPG") or s.upper().endswith(".PNG"):
            file_number = s[begin:end]
        elif s.upper().endswith(".JPEG"):
            file_number = s[begin-1:end-1]
        try:
            return float(file_number)
        except:

            if s.upper().endswith(".JPG") or s.upper().endswith(".PNG"):
                file_number = s[begin + 1:end]
            elif s.upper().endswith(".JPEG"):
                file_number = s[begin:end - 1]
            return float(file_number)

    return sorted(photos, key=sort_func)
