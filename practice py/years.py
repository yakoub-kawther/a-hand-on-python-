import math
def isleap(year):
  leap = False
  if (year % 4 == 0):
     if(year % 100 == 0):
        if(year % 400 == 0):
           leap = True
  
  return leap

if __name__=="__main__":
   year = int(input("inter your year"))
   if 1900<= year <= 10**5:
      print(isleap(year))
   else:
      print("repeat")
      