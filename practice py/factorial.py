import math

def extraLongFactorial(n):

  if n<=0 :
    return "must be grater than 0"
  elif n > 100:
    return "must be less than 100"
  else:
    return str(math.factorial(n))
  
if __name__ == "__main__":
  n = int(input().strip())

  print(extraLongFactorial(n))
  