import math
numasstr = input("What would you like to root?",)
try:
  num = int(numasstr)
  sqrt = math.sqrt(num)
  print ("That is equal to", sqrt)
except  ValueError:
    print('Please use a real number') 
