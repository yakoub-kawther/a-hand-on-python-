from random import randint

class Die:
  def __init__(self,sides=6):
    self.sides=sides

  def rollDie(self):
    k=self.sides
    i=0
    while i<k:
      self.sides=randint(1,k)
      print(self.sides)
      i+=1
      
