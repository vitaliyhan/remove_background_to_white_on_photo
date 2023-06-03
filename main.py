import tqdm
from PIL import Image
from transparent_background import Remover
import time
import os

now = time.time()
remover = Remover(fast=False, jit=False)


def remove(fname, path_in, path_out, path_out_transparent):
    img = Image.open(path_in + "/" + fname).convert('RGB')  # read image
  
    out = remover.process(img, type='white')  # image matting - white screen, type='blur' - blur
    Image.fromarray(out).save(path_out + '/' + fname)  # save result
     
    out2 = remover.process(img)
    Image.fromarray(out2).save(path_out_transparent + '/' + fname + '.png')  # save result


# проверяем папки и процессим только новые
folder_in = "img"
folder_out = "img_out"
folder_out_transparent = "img_out_transparent"
files_in = os.listdir(folder_in)
files_out = os.listdir(folder_out)

files = []
for file_in in files_in:
    if file_in not in files_out:
        files.append(file_in)

len_files = len(files)
print("Всего ", len(files_in), end="")
print(" уже сделано ", len(files_out), end="")
print(" осталось ", len_files)
i = 0

for file in tqdm.tqdm(files, desc='Изображения'):
    i += 1
    remove(file, folder_in, folder_out, folder_out_transparent)

print("Прошло ", int((time.time() - now) / 60), " мин.")
