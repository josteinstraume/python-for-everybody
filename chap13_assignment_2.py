import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/known_by_Ajayraj.html" 
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

count = int(raw_input ('Enter count: '))
position = int(raw_input('Enter position: '))

for _ in range(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    if (len(tags) < 3):
        break
    print 'Retrieving: ',tags[position-1]['href']
    url = tags[position-1]['href']