# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
# Name:
# Collaborators:
# Time:

from tkinter.messagebox import NO
import numpy
import random
import matplotlib.pylab as pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        # TODO
        self.maxprob = maxBirthProb
        self.clearprob = clearProb

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        return random.random() < self.clearprob

    
    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        # TODO
        if random.random() < self.maxprob*(1-popDensity):
            return SimpleVirus(self.maxprob,self.clearprob)
        else:
            raise NoChildException



class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        # TODO
        self.viruses = viruses
        self.maxpop = maxPop


    def getTotalPop(self):

        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """

        # TODO        
        return len(self.viruses)


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO
        suriving_viruses = []
        for virus in self.viruses:
            if virus.doesClear():
                continue
            else:
                suriving_viruses.append(virus)

        pop_density = len(self.viruses) / float(self.maxpop)

        patient_viruses = []
        for virus in suriving_viruses:
            patient_viruses.append(virus)
            try:
                patient_viruses.append(virus.reproduce(pop_density))
            except NoChildException:
                continue

        self.viruses = patient_viruses
        return len(self.viruses)



#
# PROBLEM 2
#
def simulationWithoutDrug(num_trials, maxBirthProb, clearProb, maxPop, num_viruses, num_time_steps):

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """

    # TODO
    total_trial_results = single_simulation(maxBirthProb, clearProb, maxPop, num_viruses, num_time_steps)

    for trial in range(num_trials - 1):
        trial_results = single_simulation(maxBirthProb, clearProb, maxPop, num_viruses, num_time_steps)

        for num, result in enumerate(trial_results):
            total_trial_results[num] += result

    averaged_results = [time_step_result / float(num_trials) for time_step_result in total_trial_results]

    pylab.plot(averaged_results, label="SimpleVirus")
    pylab.xlabel("Amount of Time")
    pylab.ylabel("Virus Population")
    pylab.title("Virus Simulation without Drug")
    pylab.show()

def single_simulation(maxBirthProb, clearProb, maxPop, num_viruses, num_time_steps):

    viruses = []
    for num in range(num_viruses):
        virus = SimpleVirus(maxBirthProb, clearProb)
        viruses.append(virus)

    patient = SimplePatient(viruses, maxPop)

    virus_populations = []

    for time_step in range(num_time_steps):
        virus_populations.append(patient.update())

    return virus_populations

if __name__ == '__main__':
    simulationWithoutDrug(1,0.1,0.05,1000,100,300)