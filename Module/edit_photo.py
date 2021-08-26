from ctypes import resize
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
from Base_info.Data_base import datacenter_coordinates,arial_font_path,bad_Cordinates
from PIL import ImageOps

class edit_photo():
    
    def edit_photo(save_path,photo_path,name,data,lineedit_fontsize,mode_pic):
        i = 0
        while i < len(photo_path):
            print("Сейчас идёт файл:  " + name[i])
            im = Image.open(photo_path[i])
            im = ImageOps.exif_transpose(im)
            w, h = im.size
            if w<h:
                fixed_width = 3024
                padding = 50
            elif w>h:
                fixed_width = 4032
                padding = -50
            width_percent = (fixed_width/ float(w))
            heigt_size = int((float(h) * float(width_percent)))
            im = im.resize((fixed_width, heigt_size ), Image.NEAREST)
            w, h = im.size
            size = int(lineedit_fontsize)
            draw_text = ImageDraw.Draw(im)
            font = ImageFont.truetype(arial_font_path, size= size * 2 , encoding="utf-8")
            time_rl = data[i].split(' ')[1]
            y,m,d = data[i].split(' ')[0].split('.')
            rus_date = ['','янв.', 'фев.', 'мар.', 'апр.', 'май', 'июн.', 'июл.', 'авг.', 'сен.', 'окт.', 'ноя.', 'дек.']
            print(str(d) + " " + str(rus_date[int(m)]) + " " + str(y) + " " + "г.," + " " + str(time_rl))
            random_last = random.randint(2, 3)
            if not mode_pic == 1:
                draw_text.text(
                    (w - (w/3+padding)-(size*500/70)  , h - (h - size - 5 )),
                    str(d) + " " + str(rus_date[int(m)]) + " " + str(y) + " " + "г.," + " " + str(time_rl) +"\n"+bad_Cordinates + str(random_last) + '"' + "\n" + datacenter_coordinates,
                    font=font,
                    fill='black')
                draw_text.text(
                    (w - (w/3+padding)-(size*500/70)+4, h - (h - size - 5)),
                    str(d) + " " + str(rus_date[int(m)]) + " " + str(y) + " " + "г.," + " " + str(time_rl) +"\n"+bad_Cordinates + str(random_last) + '"' + "\n" + datacenter_coordinates,
                    font=font,
                    fill='white') 
            im.save(str(save_path) + '/' + name[i] + '.jpg')
            i = i + 1
            
    

