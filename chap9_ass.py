name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, 'r')
text = handle.read()
words = text.split()

words = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
    
bigCount = None
bigWord = None

for word,count in words.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print bigWord, bigCount

