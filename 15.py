#we have january 26 Monday 1xx6 year
# generate all possible years
import datetime
import requests
from bs4 import BeautifulSoup
year = [year for year in range(1006,2000,10) if datetime.date(year,1,26).isoweekday()==1]
year =  [str(year) for year in year]
# source code hints:  he ain't the youngest, he is the second  and  buy flowers for tomorrow
# we parse wiki page about january 27
url = 'https://en.wikipedia.org/wiki/January_27'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
births_section = soup.find('span', id='1601–1900_2')
births_list = births_section.find_next('ul')
births = births_list.find_all('li')
names = []
for birth in births:
    names.append(str(birth.get_text()))

for i in names:
    if (i[:4]) in year:
        print(i) #we get 1756 – Wolfgang Amadeus Mozart, Austrian pianist and composer (d. 1791)

# next http://www.pythonchallenge.com/pc/return/mozart.html
