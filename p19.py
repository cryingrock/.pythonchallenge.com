import requests
from bs4 import BeautifulSoup
import re, base64
import wave
import audioop


def pythonchallenge18(path):
    response = requests.get(path, auth=('butter','fly'))
    soup = str(BeautifulSoup(response.content,'html.parser'))
    #find base64 from url
    code = ''.join(re.findall('base64\n\n(.*?)\n\n-',soup, re.DOTALL))
    #create audio file from code
    audio = open('indian.wav','wb')
    audio.write(base64.b64decode(code))
    audio.close() #sorry, something is wrong


def pythonchallenge18_1(file):
    with wave.open(file, 'rb') as audio:
        parameters = (audio.getparams())
        with wave.open('indian1.wav','wb') as audio_out:
            audio_out.setparams(parameters)


            frames = audio.readframes(parameters.nframes)
            converted_frames = audioop.byteswap(frames, audio.getsampwidth())

            audio_out.writeframes(converted_frames) #you are the idiot
            #http://www.pythonchallenge.com/pc/hex/idiot.html



r =  pythonchallenge18_1('indian.wav')

result  = pythonchallenge18('http://www.pythonchallenge.com/pc/hex/bin.html')
#next = http://www.pythonchallenge.com/pc/hex/idiot2.html
