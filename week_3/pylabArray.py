import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
print xVals
xVals = pylab.array(xVals)
yVals = pylabl.array(yVals)
print xVals