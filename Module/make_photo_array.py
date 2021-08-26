
from Module.get_all_files import get_all_files

class make_photo_array:
 def make_photo_array(dir):
    photos = get_all_files.get_all_files(dir)
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