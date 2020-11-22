
import argparse
import os
import random
import math
from PIL import Image


def make_collage(image_paths, filename, margin=10):
    """
    Make a collage image with a width equal to `width` from `images` and save to `filename`.
    """
    images = [Image.open(path) for path in image_paths]

    row_count = round(math.sqrt(len(images)))
    col_count = len(images) // row_count

    image_height = max([image.height for image in images])
    image_width = max([image.width for image in images])
    background_size = (image_width*col_count, image_height*row_count)
    background = Image.new(
        'RGBA', background_size, (255, 255, 255, 255))
    print(background_size)
    for row in range(row_count):
        for col in range(col_count):
            image = images[col + row*col_count]
            offset = (col*(image_width + margin), row*(image_height + margin))
            print(offset)
            background.paste(image, offset)
    background.save(filename)
    return True


if __name__ == '__main__':
    import os
    image_paths = [os.path.join(os.curdir, 'screenshots', path)
                   for path in os.listdir('./screenshots')]
    make_collage(image_paths, 'screenshot.png')
