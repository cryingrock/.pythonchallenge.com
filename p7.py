#To read an image with Python we need Pillow library
from PIL import Image
def pythonchallenge7(path):
    img_rgb = Image.open(path)
    gray_pixels = []
    width, height = img_rgb.size
    #grey pixels are in the middle of image and they size are 7
    for i in range(width):
        gray_pixels.append(img_rgb.getpixel((i,int(height/2))))
    gray_pixels = gray_pixels[::7]
    text = ''
    for j in gray_pixels:
            text += (chr(j[0]))
            #smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]pe_
    temp = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    answer= ''
    for k in temp:
        answer+=chr(k)
    return answer

result = pythonchallenge7('oxygen.png')
print(result) #www.pythonchallenge.com/pc/def/integrity.html
