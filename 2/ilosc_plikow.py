import os

path, dirs, files = next(os.walk("/dev"))
print(f'Number of files in /dev: {len(files)}')
