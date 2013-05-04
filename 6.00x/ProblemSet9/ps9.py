# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *


def histsimulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials, delay):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    finalpops = []
    for i in range(numTrials):
        poptimes = []
        viruslist = []
        for i in range(numViruses):
            viruslist.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        dude = TreatedPatient(viruslist, maxPop)
        for timestep in range(delay):
            poptimes.append(dude.update())
        dude.addPrescription('guttagonol')
        for timestep in range(delay,delay+150):
            poptimes.append(dude.update())
        finalpops.append(poptimes[-1])
    pylab.hist(finalpops, bins = 20)
    pylab.title("Resistant Virus simulation, delay = " +str(delay))
    pylab.xlabel("Final Pop")
    pylab.ylabel("Number of trials")
    pylab.show()

def calcFinalPop(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, delay):
        population = 0
        viruslist = []
        for i in range(numViruses):
            viruslist.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        dude = TreatedPatient(viruslist, maxPop)
        for timestep in xrange(150):
            population = dude.update()
        dude.addPrescription('guttagonol')
        for timestep in xrange(150,delay+150):
             population = dude.update()
        dude.addPrescription('grimpex')
        for timestep in xrange(delay+150,delay+300):
             population = dude.update()
        return population
    

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    histsimulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False},
                       .005, numTrials, 0)






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delay0 = []
    delay75 = []
    delay150 = []
    delay300 = []
    for i in xrange(numTrials):
        delay0.append(calcFinalPop(100, 1000, 0.1, 0.05, {'guttagonol': False, 'grimpex': False},
                       .005, 0))
        delay75.append(calcFinalPop(100, 1000, 0.1, 0.05, {'guttagonol': False, 'grimpex': False},
                       .005, 75))
        delay150.append(calcFinalPop(100, 1000, 0.1, 0.05, {'guttagonol': False, 'grimpex': False},
                       .005, 150))
        delay300.append(calcFinalPop(100, 1000, 0.1, 0.05, {'guttagonol': False, 'grimpex': False},
                       .005, 300))
    pylab.figure('Delay 0')
    pylab.hist(delay0, bins = [0,50,1000], label = "0 step delay", histtype='bar', alpha=1.0)
    pylab.figure('Delay 75')
    pylab.hist(delay75, bins = [0,50,1000], label = "75 step delay", histtype='bar', alpha=0.85)
    pylab.figure('Delay 150')
    pylab.hist(delay150, bins = [0,50,1000], label = "150 step delay", histtype='bar', alpha=0.6)
    pylab.figure('Delay 300')
    pylab.hist(delay300, bins = [0,50,1000], label = "300 step delay", histtype='bar', alpha=.45)
    pylab.show()
