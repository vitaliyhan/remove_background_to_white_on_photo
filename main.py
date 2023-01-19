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


folder_in = "img"
folder_out = "img_out"
files = os.listdir(folder_in)
for file in files:
    remove(file, folder_in, folder_out)

print("Прошло ", time.time() - now)
