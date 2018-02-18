inn = input("Number")
innx = int(inn)
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print("That is equal to",factorial(innx))
