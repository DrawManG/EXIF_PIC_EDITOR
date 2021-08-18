import os

class get_all_files:
 def get_all_files(rootdir):
    rootdir = os.path.normcase(rootdir)
    file_paths = []
    for dirpath, dirs, files in os.walk(rootdir):
        for filename in files:
            if (filename.upper().endswith(".JPG") or filename.upper().endswith(".JPEG") or \
                filename.upper().endswith(".PNG")) and (not "modified" in dirpath):
                file_paths.append(os.path.join(dirpath, filename))

    return file_paths