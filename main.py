import tqdm
from PIL import Image
from transparent_background import Remover
import time
import os

now = time.time()
remover = Remover(fast=False, jit=False)  # default setting 7


def remove(fname, path_in, path_out):
    img = Image.open(path_in + "/" + fname).convert('RGB')  # read image
    # out = remover.process(img)  # default setting - transparent background
    out = remover.process(img, type='white')  # image matting - green screen
    # out = remover.process(img, type='blur')  # blur background
    Image.fromarray(out).save(path_out + '/' + fname)  # save result


# проверяем папки и процессим только новые
folder_in = "img"
folder_out = "img_out"
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
    # info_str = [str(i), " из ", str(len_files), " ", str(round(i / len_files, 2)), " %  ",
    #             str(int((time.time() - now) / 60)), " мин."]
    # tqdm.tqdm.write("".join(info_str))
    remove(file, folder_in, folder_out)

print("Прошло ", int((time.time() - now) / 60), " мин.")
