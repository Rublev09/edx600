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
    diffTemps = [j - i for i,j in zip(lowTemps, highTemps)]
    pylab.plot(range(1,32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges (Fahrenheit)')
    pylab.show()

producePlot(lowTemp, highTemp)



        
    
