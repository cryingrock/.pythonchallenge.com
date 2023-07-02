from PIL import Image, ImageEnhance

def pythonchallenge11(path,contrast, brightness):
    image = Image.open(path)
    new_image = ImageEnhance.Contrast(image)
    new_image = new_image.enhance(contrast)

    new_iamge_2 = ImageEnhance.Brightness(new_image)
    new_iamge_2 = new_iamge_2.enhance(brightness)


    return new_iamge_2




result = pythonchallenge11('cave.jpg',0.65,5) #we see the word evil
result.show() #http://www.pythonchallenge.com/pc/return/evil.html

