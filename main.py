#1826344050
#1826344459

#1625314251
#1625314359

class Start_Script():
    def scearch_file_image(self,dir, format=["jpg", "png", "jpeg"]):
        import os

        def test_in(array, x):
            for i in array:
                if i in x:
                    return True
            return False
        dir = os.path.normcase(dir)
        file_paths = []
        for dirpath, dirs, files in os.walk(dir):
            for filename in files:
                if test_in(format, filename):
                    file_paths.append(os.path.join(dirpath, filename))
        return file_paths , dirpath

def proverka():
    i = 0
    while i <= len(image_list) - 1:
        name.append(image_list[i].split("\\", -1)[-1].split('.', 1)[0])
        i = i + 1
        if len(name[i -1]) > 15 or len(name[i -1]) > 14:
            print('good')
            good_file.append(name[i -1])
            original_name.append(name[i - 1])
            dir_good_save.append(dir)
        else:
            refrash_list[i-1] = ''
            print('error количество букв:  ' + str(len(name[i-1])))
    i = 0
    while i <= len(image_list) - 1:
        if not refrash_list[i-1] == '':
            path_good_file.append(refrash_list[i-1])
        i = i+1

def replace_good_files():
    try:
     i = 0
     while i <= len(good_file) - 1 :
        good_file[i] = good_file[i].replace(',', '.').replace('-',':')
        i = i + 1
    except:
        print('error')

def DATA_NEW():
    import os

    list_path = Start_Script().scearch_file_image(path_save)
    i = 0
    while i <= len(list_path) - 1 :
        date_time = good_file[i]
        pattern = '%Y.%m.%d %H:%M:%S'
        import time
        epoch = int(time.mktime(time.strptime(date_time, pattern)))
        from win32_setctime import setctime
        setctime(dir_good_save[i] + "/"+ original_name[i] + '.jpg', epoch)
        os.utime(dir_good_save[i] + "/"+ original_name[i] + '.jpg',(epoch, epoch))
        i = i+1

def __edit_photo_():
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
    import random

    i = 0
    while i <= len(path_good_file) - 1 :
        random_X = random.randint(22222, 55555)
        random_Y = random.randint(33333, 44444)
        im = Image.open(path_good_file[i])
        draw_text = ImageDraw.Draw(im)
        font = ImageFont.truetype(r'C:\Windows\Fonts\timesi.ttf', size=25)
        width, height = im.size
        draw_text.text(
            (width - 400, 20),
            'Дата: ' + good_file[i],
            font=font,
            fill='#1C0606')
        draw_text.text(
            (width - 400, 45),
            'Геопозиция: ' + '55.' + str(random_X) + " , " + "37." + str(random_Y),
            font=font,
            fill='#1C0606')
        #---------------------------------------
        only_path.append(path_good_file[i])
        im.save(str(path_save) + '/' + original_name[i] + '.jpg')
        i = i + 1

if __name__ == '__main__':
    from tkinter import filedialog

    dir_good_save = []
    original_name = []
    path_good_file = []
    only_path = []
    good_file = []
    name = []
    format =["jpg", "png", "jpeg"]
    path = filedialog.askdirectory()
    path_save = filedialog.askdirectory()
    image_list , dir = Start_Script().scearch_file_image(path)
    refrash_list = image_list
    proverka()
    replace_good_files()
    __edit_photo_()
    DATA_NEW()



