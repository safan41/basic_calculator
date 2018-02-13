import math
raw = input("What would you like to divide?")
raw2 = input("With?")
try:
  ind = int(raw)
  ind2 = int(raw2)
  print ("That is equal to", ind / ind2)
except ValueError:
    print ("Please use real numbers")
except ZeroDivisionError:
  print ("You can't divide by zero")
