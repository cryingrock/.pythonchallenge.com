# Source code  remember: 100*100 = (100+99+99+98) + (...
from PIL import Image

def pythonchallenge14(path):
    image = Image.open(path)
    original_width, original_height = image.size # (10000, 1)

    new_image = Image.new('RGBA', (100, 100))
    new_width, new_height = new_image.size

    x, y = 0, 0
    dx, dy = 1, 0
    count = 0

    for _ in range(10000):
        pixel = image.getpixel((count % original_width, count // original_width))
        new_image.putpixel((x, y), pixel)
        count += 1
        if (x + dx >= new_width or x + dx < 0 or y + dy >= new_height or y + dy < 0 or new_image.getpixel((x + dx, y + dy)) != (0, 0, 0, 0) ):
            dx, dy = -dy, dx  # Rotate direction

        x += dx  # Move in x-direction
        y += dy  # Move in y-direction
    new_image.show() #we see a cat, code must be cat


result = pythonchallenge14('wire.png')

#http://www.pythonchallenge.com/pc/return/cat.html and text and its name is uzi. you'll hear from him later.
#http://www.pythonchallenge.com/pc/return/uzi.html
