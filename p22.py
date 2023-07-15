#http://www.pythonchallenge.com/pc/hex/copper.html source code:  or maybe white.gif would be more bright
#try: http://www.pythonchallenge.com/pc/hex/white.gif
from PIL import Image
class image:
    def __init__(self, path, brightness):
        self.path = path
        self.brightness = brightness
    def frames_number(self):
        image = Image.open(self.path)
        return image
        frames = image.n_frames #133
        frame_colors = []
        for i in range(frames):
            image.seek(image.tell()+1)
            frame = image.convert('RGBA')
            colors = frame.getcolors(frame.size[0] * frame.size[1])
            frame_colors.append(colors) #we see [[(1, (8, 8, 8, 255)), (39999, (0, 0, 0, 255))]]

    def new_gif(self):
        data  =width,height =  image.frames_number(self).size
        gif = image.frames_number(self)
        new = Image.new('RGBA',(400,400)) #creating a new image
        data = new.load()
        #I am trying to find pixel's [(1, (8, 8, 8, 255) coordinates
        start_x,start_y = 100, 100
        center_x, center_y = 100,100
        for frames in range(gif.n_frames):
            gif.seek(frames)
            x,y,x2,y2 = gif.getbbox()
            #print('x', x, ' y',y) start x-100 y-100
            x_difference = x - center_x
            y_difference = y - center_y

            if (x_difference==0 and y_difference==0):
                start_x+=20
                start_y+=20

            start_x+= x_difference
            start_y+=y_difference

            data[start_x,start_y] = (150,150,150)
        new.show() #I see the word BONUS

file = image('white.gif',1)
print(file.new_gif())