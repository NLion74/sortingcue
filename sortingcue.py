import os
import shutil

path = 'drive:/path/to/your/cue'
list_ = os.listdir(path)

dir = []
cue = []
files = []
count = 0

for file_ in list_:
    file, ext = os.path.splitext(file_)

    if os.path.isdir(path + '/' + file_):
        dir.append(file_.rsplit("-", 1)[1])
        files.append(file_)

    if os.path.isfile(path + '/' + file_):
        cue.append(file)

for cue_ in cue:
    for i, dir_ in enumerate(dir):
        dir_ = dir_.lstrip()
        if dir_ == cue_:
            print(cue_ + '.cue' + ' has been moved to: ' + path + '/' + files[i])
            shutil.move(path + '/' + cue_ + '.cue', path + '/' + files[i])
        else:
            continue