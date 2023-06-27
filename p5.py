from urllib.request import urlopen
import pickle
def pythonchallenge5(url):
    #firsty try with base url link and we got src="banner.p
    #after after the hint we need to upload pickle
    html = urlopen(url)
    data = pickle.load(html)
    html.close()
    c = []
    for line in data:
        print(''.join([i*j for i,j in line]))






result = pythonchallenge5('http://www.pythonchallenge.com/pc/def/banner.p')
#www.pythonchallenge.com/pc/def/channel.html