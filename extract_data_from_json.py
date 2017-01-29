import json
import urllib

while True:
    url = raw_input('Enter Location: ')
    if len(url) < 1:
        break
    
    print 'Retrieving',url
    data = urllib.urlopen(url).read()
    print 'Retrieved',len(data),'characters'
    
    # Parse data into JSON dictionary
    dict = json.loads(data)
    
    sum = 0
    
    # Loop through JSON dictionary to compute sum
    for item in dict['comments']:
        sum += float(item['count'])
    
    print 'Count:',len(dict['comments'])
    print 'Sum:',sum