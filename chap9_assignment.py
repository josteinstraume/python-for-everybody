name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt" 
text = open(name)

counts = dict()

for line in text:
    if line.startswith("From "):
        words = line.split()
        word = words[1]
        #print word, words
        counts[word] = counts.get(word,0) + 1
    
bigCount = None
bigWord = None

#print counts

for word,count in counts.items():
    if bigCount is None or count > bigCount:
    	bigWord = word
        bigCount = count

print bigWord,bigCount