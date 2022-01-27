import os
from PIL import Image
from glob import glob
dirs = glob("./*", recursive = True)
dirs_ls = []
for d in dirs:
    d = d[2:]
    dirs_ls.append(d)

# Source
# https://note.nkmk.me/en/python-pillow-square-circle-thumbnail/
def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

img_num = 1
for dir in dirs_ls:
    # Nao copiar o python file
    if dir != 'convert.py':
        for filename in os.listdir(dir):
            f = dir +'/'+ filename
            im = Image.open(f)
            # Add black bars to the side of the images
            new_image = expand2square(im, (0, 0, 0)).resize((256, 256), Image.LANCZOS)
            newfilename = '../no_faces/' + '0_' + str(img_num) + '.jpg'
            new_image.save(newfilename)
            img_num += 1

print('Done')
