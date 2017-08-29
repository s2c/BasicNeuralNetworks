from random import random

def forwardMultiplyGate(x,y):
  return x*y

def printOuts(bestOut,bestX,bestY):
  print("Best out is: " + str(bestOut))
  print("BestX is: " + str(bestX))
  print("BestY is: " + str(bestY))
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
