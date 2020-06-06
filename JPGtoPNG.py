import sys
import os
from PIL import Image
import shutil

old_folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)
else:
    shutil.rmtree(new_folder)           # Removes all the subdirectories!
    os.makedirs(new_folder)

for file in os.listdir(old_folder):
    img = Image.open(f'./{old_folder}{file}')
    clean_name = os.path.splitext(f'{file}')[0]
    img.save(f'./{new_folder}{clean_name}.png')
    print('DONE')