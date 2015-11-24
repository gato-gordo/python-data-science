#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """

    numVirusesAterTrial = []
    for i in range(numTrials):
            viruses = []
            for j in range(numViruses):
                viruses.append(SimpleVirus(maxBirthProb, clearProb))
            patient = Patient(viruses, maxPop)
            patientNumViruses = []
            for k in range(300):
                patientNumViruses.append(patient.getTotalPop())
                patient.update()            
            pylab.plot(range(300), patientNumViruses)
            pylab.show()
            #numVirusesAterTrial.append(len(patient.getViruses()))