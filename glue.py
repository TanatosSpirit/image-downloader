import glob
from PIL import Image

col_array = []
row_array = []
for file in glob.glob("*.jpg"):
    row = file.split("_")
    row_array.append(int(row[2]))

    col = row[3].split(".")
    col_array.append(int(col[0]))

row_array = set(row_array)
col_array = set(col_array)

row_array = list(row_array)
col_array = list(col_array)


width = 0
file_name = "image_tile_0_"

for i in range(col_array[-1] + 1):
    file = file_name + str(i) + ".jpg"
    img = Image.open(file)
    w, h = img.size
    width += w

height = 0
file_name = "image_tile_"

for i in range(row_array[-1] + 1):
    file = file_name + str(i) + "_0.jpg"
    img = Image.open(file)
    w, h = img.size
    height += h

new_im = Image.new('RGB', (width, height))

file_name = "image_tile_"
x, y = 0, 0
for i in range(row_array[-1] + 1):
    file = file_name + str(i) + "_"

    for j in range(col_array[-1] + 1):

        file_col = file + str(j) + ".jpg"

        img = Image.open(file_col)
        w, h = img.size

        new_im.paste(img, (x, y, x + w, y + h))

        x += w

    x = 0
    y += h


new_im.save('image.jpg')

