#http://www.pythonchallenge.com/pc/return/evil.html open image
#http://www.pythonchallenge.com/pc/return/evil1.jpg we could change numbers to 2 and 3
#http://www.pythonchallenge.com/pc/return/evil2.jpg text not jpg but gfx
#change to gfx and download the file

with open('evil2.gfx',"rb") as file:
    data = file.read()
    #it was 5 cards at the start

for i in range(5):
    open(str(i)+'.jpg','wb').write(data[i::5])
    #we got 5 pic #disproportional

