import random
import pylab

d1 = {}
for i in range(10000):
    x = random.randrange(10) 
    d1[x] = d1.get(x, 0) + 1

x1 = d1.keys()
y1 = d1.values()
pylab.figure('cheese')
pylab.bar(x1,y1, .35, color='red')

d2 = {}
for i in range(10000):
    x = int(random.random()*10)
    d2[x] = d2.get(x, 0) + 1

x2 = d2.keys()
y2 = d2.values()
pylab.figure('cheese')
pylab.bar(x2,y2, .35, color='green')

d3 = {}
for i in range(10000):
    x = random.randint(0, 10)
    d3[x] = d3.get(x, 0) + 1

x3 = d3.keys()
y3 = d3.values()
pylab.figure('cheese')
pylab.bar(x3,y3,.35, color='blue')

pylab.show()
