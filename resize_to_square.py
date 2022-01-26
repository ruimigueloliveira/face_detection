from PIL import Image

import os
directory = 'photos/'

for filename in os.listdir(directory):
    f = 'photos/' + filename
    im = Image.open(f)
    width, height = im.size   # Get dimensions

    new_width = 1024
    new_height = 1024

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    # Crop the center of the image
    new_image = im.crop((left, top, right, bottom))
    newfilename = 'square_photos/' + 'square_' + filename
    new_image.save(newfilename)





