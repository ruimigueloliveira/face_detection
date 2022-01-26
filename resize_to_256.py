from PIL import Image

import os
directory = 'square_photos/'

for filename in os.listdir(directory):
    f = 'square_photos/' + filename
    im = Image.open(f)
    new_image = im.resize((256, 256))
    newfilename = '256_photos/' + '256_' + filename
    new_image.save(newfilename)
