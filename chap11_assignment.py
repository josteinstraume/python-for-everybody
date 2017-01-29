# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_328963.txt" 
text = open(name)

numlist = list()

for line in text:
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    for num in nums:
        num = float(num)
        numlist.append(num)

sum = 0

for num in numlist:
    sum = sum + num

print sum



