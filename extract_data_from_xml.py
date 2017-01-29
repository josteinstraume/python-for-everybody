import urllib
import xml.etree.ElementTree as ET

while True:
    url = raw_input('Enter Location: ')
    if len(url) < 1 : break
    
    print 'Retrieving', url
    data = urllib.urlopen(url).read()
    print 'Retrieved',len(data),'characters'
    
    # Parse the string into an element tree
    tree = ET.fromstring(data)

    # Find all count tags in order to find the sum
    results = tree.findall('.comments/comment/count')
    print 'Count:',len(results)
    sum = 0
    
    # Go through all counts and generate the sum
    for item in results:
        sum = sum + float(item.text)

    print 'Sum:',sum