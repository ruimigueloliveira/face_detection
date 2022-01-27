from PIL import Image

import os
directory = 'photos/'

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

for filename in os.listdir(directory):
    f = 'photos/' + filename
    im = Image.open(f)

    # Add black bars to the side of the images
    new_image = expand2square(im, (0, 0, 0)).resize((1024, 1024), Image.LANCZOS)
    newfilename = 'square_photos/' + 'square_' + filename
    new_image.save(newfilename)
