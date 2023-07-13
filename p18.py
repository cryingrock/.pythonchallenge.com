#head: can you tell the difference? //  it is more obvious that what you might think
# http://www.pythonchallenge.com/pc/return/brightness.html //  maybe consider deltas.gz
import gzip
import  difflib
def pythonchallenge18(path):
    data1, data2 = [], []
    #find split point
    with gzip.open(path,'rb') as file:
        content = file.readline()
        space= content.decode().index('  ') #53
        space2 = content.decode().index(' 8') #55+1 = 56
        file.close()


    with gzip.open(path, 'rb') as data:
        for line in data:
            data1.append(line[:space].decode()+"\n")
            data2.append(line[space2+1:].decode())

    differ = difflib.Differ()
    compare = list(differ.compare(data1,data2)) # we see + - and spaces
    # #'- 'line unique to sequence  '+ ' line unique to sequence 2 '  ' line common to both sequences
    # we have 3 pictures
    pic1 = open('pic1.png', 'wb')
    pic2 = open('pic2.png', 'wb')
    pic3 = open('pic3.png', 'wb')

    # create 3 pictures:

    for line in compare:
        bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
        if line.startswith('+'):
            pic1.write(bs)
        elif line.startswith('-'):
            pic2.write(bs)
        else:
            pic3.write(bs)

    pic1.close() #butter
    pic2.close() #fly
    pic3.close() #hex/bin.html
    return "Pictures created successfully."


result = pythonchallenge18('deltas.gz')
print(result) #www.pythonchallenge.com/pc/hex/bin.html username butter password fly
