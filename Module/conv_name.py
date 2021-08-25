import os

class conv_name:
  def conv_name(file_path,data):
    saver = []
    i = 0
    while i <= len(file_path) - 1:
      print('data:',data[i])
      print("idet: ",file_path[i])

      year, mouth, day = data[i].split(' ')[0].split(".")
      hour, minute, second = data[i].split(' ')[1].split(":")
      base = os.path.basename(file_path[i])
      saver.append("IMG_"+year+mouth+day+"_"+hour+minute+second)
      i = i + 1
    return saver