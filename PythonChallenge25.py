# http://www.pythonchallenge.com/pc/hex/lake1.jpg
# Tittle: imagine how they sound Source: can you see the waves?
# http://www.pythonchallenge.com/pc/hex/lake1.jpg change .jpg to wav
from PIL import Image
import wave
import requests

base_url = "http://www.pythonchallenge.com/pc/hex/lake{}.wav"

for x in range(1,26):
    file_url = base_url.format(x)
    file_name = f"lake{x}.wav"
    response = requests.get(file_url, auth = ('butter','fly'))
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {file_name}")

result = Image.new('RGB', (300, 300), 0)

class waves():
    def __init__(self,path):
        self.path = path

    def waw(self):


        with wave.open(self.path, 'rb') as wav_file:
            byte_data = wav_file.readframes(wav_file.getnframes())
            img = Image.frombytes('RGB', (60, 60), byte_data)

            x_pos = ((i - 1) % 5) * 60
            y_pos = ((i - 1) // 5) * 60

            result.paste(img, (x_pos, y_pos))

for i in range(1,26):
    wave_file = waves(f"lake{i}.wav")
    data = wave_file.waw()

result.save("result_image.png")
result.show()

# next level: http://www.pythonchallenge.com/pc/hex/decent.html