from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
from datetime import datetime,timedelta
from Base_info.Data_base import datacenter_coordinates,random_coordinates_X,random_coordinates_Y,arial_font_path,bad_Cordinates

class edit_photo:
 def edit_photo(save_path,photo_path,name,data):
     i = 0
     while i <= len(photo_path) - 1 :
        print("Сейчас идёт файл:  " + name[i])
        im = Image.open(photo_path[i])
        w, h = im.size
        im = Image.open(photo_path[i])
        clac = int((h*100)/w * 10)
        size = int(150/clac*100)
        draw_text = ImageDraw.Draw(im)
        font = ImageFont.truetype(arial_font_path, size= size * 2 , encoding="utf-8")
        time_rl = data[i].split(' ')[1]
        y,m,d = data[i].split(' ')[0].split('.')
        rus_date = ['','янв.', 'фев.', 'мар.', 'апр.', 'май', 'июн.', 'июл.', 'авг.', 'сен.', 'окт.', 'ноя.', 'дек.']
        print(str(d) + " " + str(rus_date[int(m)]) + " " + str(y) + " " + "г.," + " " + str(time_rl))
        random_last = random.randint(2, 3)
        if w == 1920 and h == 1080:
            w = w - 400
            h = h - 400
        draw_text.text(
            (w - (w/4.25) +2, h - (h - 10)),
            str(d) + " " + str(rus_date[int(m)]) + " " + str(y) + " " + "г.," + " " + str(time_rl),
            font=font,
            fill='black')
        draw_text.text(
            (w - (w/4.25) , h - (h - 10)),
            str(d) + " " + str(rus_date[int(m)]) + " " + str(y) + " " + "г.," + " " + str(time_rl),
            font=font,
            fill='white')
        draw_text.text(
            (w - (w/4.25)+2, h - (h - 70)),
            bad_Cordinates + str(random_last) + '"',
            font=font,
            fill='black')
        draw_text.text(
            (w - (w/4.25), h - (h  - 70)),
            bad_Cordinates + str(random_last) + '"',
            font=font,
            fill='white')
        draw_text.text(
            (w - (w/4.25)+2, h - (h  - 130)),
            datacenter_coordinates,
            font=font,
            fill='black')

        draw_text.text(
            (w - (w/4.25), h - (h  - 130)),
            datacenter_coordinates,
            font=font,
            fill='white')
        im.save(str(save_path) + '/' + name[i] + '.jpg')
        i = i + 1
