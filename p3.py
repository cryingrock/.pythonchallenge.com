import requests
import re
def pythonchallenge3(url):
    page = requests.get(url)
    information = page.text
    text = re.findall('[^A-Z][A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]',information)
    word = ''
    for i in text:
        word+=i[4]


    return word


result = pythonchallenge3('http://www.pythonchallenge.com/pc/def/equality.html')
print(result) #http://www.pythonchallenge.com/pc/def/linkedlist.php