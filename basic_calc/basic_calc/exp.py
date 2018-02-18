import math
raw = input("What is the base?")
raw2 = input("To the power of?")
try:
  ind = int(raw)
  ind2 = int(raw2)
  print ("That is equal to", ind ** ind2)
except ValueError:
    print ("Please use a real numbers")
