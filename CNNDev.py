from random import random
from lib import *
# Random local search

x = -2
y = 3

# Random Local
deltaChange = 0.01
bestOut = -float('inf')
bestX = x
bestY = y

for i in range(0,100):
  xTry = x + deltaChange * random()
  yTry = y + deltaChange * random()
  cur = forwardMultiplyGate(xTry,yTry)
  
  if cur > bestOut:
    bestOut = cur
    bestX = xTry
    bestY = yTry

printOuts(bestOut,bestX,bestY)

# Gradient Descent it looks like

gradX = compDerv(x,y,forwardMultiplyGate,x)
gradY = compDerv(x,y,forwardMultiplyGate,y)
print(gradX,gradY)
