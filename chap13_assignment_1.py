import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_328968.html" 
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the __ tags
tags = soup('span')
sum = 0

for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:', tag
    #print 'URL:', tag.get('href', None)
    #print 'Contents:', tag.contents[0]
    sum = sum + float(tag.contents[0])
    #print 'Attrs:', tag.attrs
    
print sum