import pylab

inFile = open('words.txt')

wordfrq={}

for line in inFile:
    words = line.split()
    for i in words:
        if len(str(i)) in wordfrq:
            wordfrq[len(i)] += 1
        else:
            wordfrq[len(str(i))] = 1

x = wordfrq.keys()
y = wordfrq.values()
tot=0
for i in y:
    tot+=i
print tot
    
pylab.bar(x, y, align='center')
pylab.xlabel('Length of Words')
pylab.ylabel('Number of Words')
pylab.title('Frequency of Word Lengths in Problem Set 4 words.txt')
pylab.show()
