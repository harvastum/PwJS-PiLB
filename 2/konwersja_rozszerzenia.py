import os

path, dirs, files = next(os.walk("dummy_files"))

for f in files:
    if f.endswith('.jpg'):
        os.rename(path+os.sep+f, path+os.sep+f.rstrip('.jpg')+'.png')

