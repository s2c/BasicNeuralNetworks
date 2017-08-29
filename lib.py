def forwardMultiplyGate(x,y):
  return x*y

def printOuts(bestOut,bestX,bestY):
  print("Best out is: " + str(bestOut))
  print("BestX is: " + str(bestX))
  print("BestY is: " + str(bestY))
  
def compDerv(x,y,fXY,wrt,h=0.000000001):
  out = fXY(x,y)
  if(x==wrt):
    return (fXY(x+h,y)-out)/h
  else:
    return (fXY(x,y+h)-out)/h
