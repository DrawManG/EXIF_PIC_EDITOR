import shutil
class copy_image:
 def copy_image(save_path, photo_path, name):
  try:
    path_copy_2 = []
    i = 0
    while i < len(photo_path):
        shutil.copy(photo_path[i], save_path + name[i] + '.JPG')
        path_copy_2.append(save_path + name[i] + '.JPG')
        i = i + 1
    return path_copy_2
  except Exception as e:
     print(e)