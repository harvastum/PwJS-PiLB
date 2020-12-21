import os

for path, dirs, files in (os.walk('..')): # walk the parent directory
    for filename in files:
        print(filename)