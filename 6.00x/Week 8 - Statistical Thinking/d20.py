import pylab
import random
import math
import numpy

def rolld20():
    return math.floor(random.random()*20+1)


def rollnumber(L):
    """
    L: number of rolls
    
    returns: higher number between a number of d20 rolls
    """
    rolls = []
    for i in range(L):
        rolls.append(rolld20())
    return max(rolls)

def rollplus(P):
    """
    P: number to add to one roll

    returns: total after one roll of d20 plus a set modifier
    """
    return rolld20()+P

def runsim(rollspertrial, numtrials, rolltype, modifier):
    """
    rollspertrial: number of rolls per trial
    numtrials: number of times to run the test
    rolltype: type of scoring, multiple rolls or straight addition
    modifier: number to add or multiply

    returns: the simulated average score for the given rolls
    """
    avepertrial = []
    for i in range(numtrials):
        trialsum = 0
        for x in range(rollspertrial):
            trialsum += rolltype(modifier)
        avepertrial.append(trialsum/rollspertrial)

    return avepertrial

def makeplot(rollspertrial, numtrials):
    pylab.figure(num=None, figsize=(12, 8), dpi=80, edgecolor='b')
##    for i in range(0,6):
##        valadd = runsim(rollspertrial, numtrials, rollplus, i)
##        pylab.hist(valadd, bins = 20, label="Modifier = +"+ str(i), histtype='stepfilled', align='mid', alpha=0.5)
    valmul = runsim(rollspertrial, numtrials, rollnumber,1)
    valmu2 = runsim(rollspertrial, numtrials, rollnumber,2)
    pylab.hist(valmul, bins = 20, label = "One Dice Roll", histtype='bar', alpha=1, edgecolor='black', align='mid')
    pylab.hist(valmu2, bins = 20, label = "Max of Two \n Dice Rolls", histtype='bar', alpha=0.5, edgecolor='black', align='mid')
    pylab.xticks(numpy.arange(9,16,.5))
    pylab.legend(loc = 'best')
    pylab.title("Result of one dice v Max of two 20-sided die rolls, " +str(rollspertrial)+' rolls per trial, ' + str(numtrials)+' trials')
    pylab.xlabel('Average Score per Trial')
    pylab.ylabel('Frequency of Occurence')
    
makeplot(1000,10000)
pylab.show()
    
    
