import requests
import re
from collections import Counter
import string
def pythonchallenge2(url):
    page = requests.get(url)
    information = page.text
    text = ''.join(re.findall('<!--(.*?)-->',information,re.DOTALL))
    text = text.split('find rare characters in the mess below:')[-1]
    return ''.join([i for i in Counter(text) if i in string.ascii_lowercase])


result = pythonchallenge2('http://www.pythonchallenge.com/pc/def/ocr.html')
print(result) #http://www.pythonchallenge.com/pc/def/equality.html

