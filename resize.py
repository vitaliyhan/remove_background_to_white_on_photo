import os
from PIL import Image
import config
import mysql.connector


def connect_to_db():
    return mysql.connector.connect(
        host=config.host,
        user=config.user,
        passwd=config.passwd,
        database=config.database
    )


def read_list():
    myCursor.execute("SELECT product_full_image, product_thumb_image FROM jos_vm_product")
    return myCursor.fetchall()


mydb = connect_to_db()
myCursor = mydb.cursor()

width_max = 250
height_max = 250
folder_in = "img_out"
folder_out = "img_out_mini"
files_in = os.listdir(folder_in)

all_img = read_list()
mydb.close()
dict_img = {}
for img_bd in all_img:
    dict_img[img_bd[0]] = img_bd[1][8:]

for file in files_in:
    if file in dict_img:
        print(file, " -> ", dict_img[file])
        image = Image.open(folder_in + "/" + file)
        width, height = image.size
        if width / height >= width_max / height_max:
            new_width = width_max
            new_height = int(width_max * height / width)
        else:
            new_width = int(height_max * width / height)
            new_height = height_max
        resized_image = image.resize((new_width, new_height))
        resized_image.save(folder_out + "/" + dict_img[file])
