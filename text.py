import os
import string
import pandas as pd

action = input("enter text file name")
action = action + ".txt"

try:
    if os.path.exists(action):
        with open(action , 'r') as myfile:
            reader = myfile.readlines()

    else:
        open(action , 'w')        
except:
    print("not available")


print(f"the amount of lines:{len(reader)}")
punc =0
for line in reader:
    for i in line:
        if i in string.punctuation:
            punc +=1
            del(i)
print(f"count of punctuations = {punc}")
words = 0
for line in reader:
    listofwords = line.split()
    words += len(listofwords)
print(f"count of words = {words}")
allchars = 0
allwords = list()
charsnospace = 0
for line in reader:
    allchars+=len(line)
    wordlist = line.split()
    allwords.extend(wordlist)
    for word in wordlist:
        charsnospace += len(word)
print(f"all chars : {allchars}")
print(f"no space chars: {charsnospace}")
wordsrepeats = dict()
for word in allwords:
    if word not in wordsrepeats.keys():
        wordsrepeats[word] = 1
        continue
    else:
        for word1 in allwords:
            if word == word1:
                wordsrepeats[word] += 1
sorted_repeat = dict()
while len(sorted_repeat) < 5:
    x = 0
    q = ''
    for i in wordsrepeats.keys():
        if wordsrepeats[i] > x:
            x = wordsrepeats[i]
            q = i
    sorted_repeat[q] = x
    del wordsrepeats[q]



print(sorted_repeat)