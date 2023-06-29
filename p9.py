import requests
import re
import numpy
from matplotlib import pyplot
def pythonchallenge8(url):
    response = requests.get(url, auth=('huge','file'))
    page = response.text
    text = ''.join(re.findall('<!--(.*?)-->', page, re.DOTALL))
    first =  list(''.join(re.findall('first:(.*?)s', text, re.DOTALL)).split(','))
    new_first = [elem.replace('\n', '') for elem in first]
    first_1 = [int(i) for i in new_first]
    # other method just copy and paste values
    second = numpy.array([156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
158,121,157,128,156,134,157,136,156,136])
    print(len(first),len(second)) #442 and 112
    x1 = numpy.r_[first_1[::2]]
    x2= numpy.r_[first_1[1::2]]
    y1 = numpy.r_[second[::2]]
    y2 = numpy.r_[second[1::2]]
    pyplot.plot(y1, -y2)
    pyplot.plot(x1,-x2)
    pyplot.show() #we see a bull



result = pythonchallenge8('http://www.pythonchallenge.com/pc/return/good.html')
#http://www.pythonchallenge.com/pc/return/bull.html