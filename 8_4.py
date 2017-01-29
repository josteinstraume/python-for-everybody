fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    temp = line.strip().split()
    #print temp
    for word in temp:
     #   print word
        if (word not in lst):
            lst.append(word)
        print lst
#sorted = lst.sort()
print sorted(lst)