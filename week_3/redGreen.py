import pylab
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here

    threeSame = 0
    for i in range(numTrials):
      balls = ['r', 'r', 'r', 'g', 'g', 'g']
      selected = []
      for j in range(3):
          selected.append(balls.pop(random.randint(0, len(balls) - 1)))
      if selected[0] == selected[1] and selected[1] == selected[2]:
          threeSame += 1
    return float(threeSame) / numTrials

print noReplacementSimulation(10)