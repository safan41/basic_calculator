import subprocess
text = input("What operation would you like to do? 1 = addition, 2 = subtraction, 3 = multiplication, 4 = division, 5 = root, 6 = exponents, factorial = 7, 8 = algebra (WIP) >")
try:
  textint = int(text)
  if (textint == 0):
   print ("This is supposed to be a 'user friendly' calculator. Geez") 
  elif (textint == 1):
    subprocess.call (["python", "add.py"])
  elif (textint == 2):
    subprocess.call (["python", "sub.py"])
  elif (textint == 3):
    subprocess.call (["python", "mult.py"])
  elif (textint == 4):
    subprocess.call (["python", "div.py"])
  elif (textint == 5):
    subprocess.call (["python", "root.py"])
  elif (textint == 6):
    subprocess.call (["python", "exp.py"])
  elif (textint == 7):
    subprocess.call (["python", "fact.py"])
  elif (textint == 8):
    subprocess.call (["python", "algbeta.py"])
  elif (textint == 41):
    subprocess.call (["python", "tri.py"])
  elif (textint == 42):
    print ("The answer to life, the universe, and everything, is not an option")
  else:
    print ("Use one of the options listed please")
except ValueError:
  print ("Please use a number")
