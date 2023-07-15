from zipfile import ZipFile
from p20 import pythonchallenge20
import bz2,zlib

class open:
    def __init__(self,path):
        self.path = path

    def opening(self):
        with ZipFile(self.path,'r') as file:
            file.namelist() #['readme.txt', 'package.pack'] we need to open 'package.pack'
            with file.open('package.pack',mode='r',pwd=(bytes(pythonchallenge20.nickname(self),encoding='utf-8'))) as pack:
                #When I had no idea what to do, I looked backwards. before we used bz2 to decompress
                #also b'x\x9c realted with zlib
                return pack.read()

    def reading(self):
        data = open.opening(self)
        while True:
            if data.startswith(b'x\x9c'):
                data = zlib.decompress(data) #BZh it is part of bz2
            elif data.startswith(b'BZh'):
                data = bz2.decompress(data)
            elif data.endswith(b'\x9c'):
                data = data[::-1]
            else:
                return data
    def unwraping(self):
        result = ''
        data = open.reading(self)
        while True:
            if data.startswith(b'x\x9c'):
                data = zlib.decompress(data)
                result += ' '
            elif data.startswith(b'BZh'):
                data = bz2.decompress(data)
                result += '#'
            elif data.endswith(b'\x9cx'):
                data = data[::-1]
                result += '\n'
            else:
                break
        print(result) #cooper
        #http://www.pythonchallenge.com/pc/hex/copper.html


file = open('p20.zip')
print(file.unwraping())