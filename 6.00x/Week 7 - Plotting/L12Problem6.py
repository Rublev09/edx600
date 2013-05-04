import pylab

inFile = open('julyTemps.txt')

lowTemp = []
highTemp = []

for line in inFile:
    fields = line.split()
    if not(len(fields) < 3 or not fields[0].isdigit()):
        highTemp.append(int(fields[1]))
        lowTemp.append(int(fields[2]))

def producePlot(lowTemps, highTemps):
    meanTemps = [(j + i)/2 for i,j in zip(lowTemps, highTemps)]
    pylab.plot(range(1,32), highTemps, label="High")
    pylab.plot(range(1,32), meanTemps, label="Mean")
    pylab.plot(range(1,32), lowTemps, label="Low")
    pylab.legend()
    pylab.title('Day by Day Low, Mean, and High in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperatures (Fahrenheit)')
    pylab.show()

producePlot(lowTemp, highTemp)



        
    
