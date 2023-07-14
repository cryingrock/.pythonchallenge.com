import requests
from zipfile import ZipFile

class pythonchallenge20:
    def __init__(self,path,original_headers):
        self.path = path
        self.original_headers = original_headers
        self.response = requests.get(path,auth=('butter','fly'), headers=original_headers)

    def range(self):
        return self.response.headers.get('Content-Range') #bytes 0-30202/2123456789 need to find the way to see the full range

    def range_up(self):
        while True:
            try:
                start = int(self.response.headers['Content-Range'].split('-')[-1].split('/')[0])+1
                self.original_headers['Range'] = 'bytes={0}-'.format(start)
                self.response = requests.get(self.path, auth=('butter', 'fly'), headers=self.original_headers)
                print(self.response.text,self.response.headers['Content-Range'])
            except:
                break
        # response: Why don't you respect my privacy?
        #         #  bytes 30203-30236/2123456789
        #         # we can go on in this way for really long time.
        #         #  bytes 30237-30283/2123456789
        #         # stop this!
        #         #  bytes 30284-30294/2123456789
        #         # invader! invader!
        #         #  bytes 30295-30312/2123456789
        #         # ok, invader. you are inside now.
        #         #  bytes 30313-30346/2123456789
        #         # http://www.pythonchallenge.com/pc/hex/invader.html answer is Yes! that's you!
    def range_end_down(self):
        start = 2123456744 #max byte
        self.original_headers['Range'] = 'bytes={0}-'.format(start-1)
        self.response = requests.get(self.path, auth=('butter', 'fly'), headers=self.original_headers)
        print(self.response.text) #and it is hiding at 1152983631.

    def range_end_up(self):
        start = 2123456744  # max byte
        self.original_headers['Range'] = 'bytes={0}-'.format(start + 1)
        self.response = requests.get(self.path, auth=('butter', 'fly'), headers=self.original_headers)
        print(self.response.text) #esrever ni emankcin wen ruoy si drowssap eht
        print(self.response.text[::-1]) #the password is your new nickname in reverse

    def nickname(self):
        nickname = 'invader'
        return nickname[::-1] #redavni

    def number(self):
        self.original_headers['Range'] = 'bytes={0}-'.format(1152983631)
        self.response = requests.get(self.path, auth=('butter', 'fly'), headers=self.original_headers)
        file = open('p20.zip','wb')
        file.write(self.response.content)
        file.close()
result = pythonchallenge20('http://www.pythonchallenge.com/pc/hex/unreal.jpg',{'User-Agent': 'python-requests/2.31.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*','Connection': 'keep-alive', 'Authorization': 'Basic YnV0dGVyOmZseQ=='})


class open:
    def __init__(self,path):
        self.path = path

    def opening(self):
        with ZipFile(self.path,'r') as file:
            file.namelist() #['readme.txt', 'package.pack']
            with file.open('readme.txt', mode='r',pwd=bytes(pythonchallenge20.nickname(self),encoding='utf-8')) as readme:
                return readme.read() #b"Yes! This is really level 21 in here. \nAnd yes, After you solve it, you'll be in level 22!\n\nNow for the level:\n\n* We used to play this game when we were kids\n* When I had no idea what to do, I looked backwards.\n"

file = open('p20.zip')
print(file.opening())
