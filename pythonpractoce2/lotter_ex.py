from random import choice , sample

class Lottery:
  def __init__(self , t):
    self.t=t

  def roll_die(self):
    winner=[]
    for _ in range(5):
      k=choice(self.t)
      if k not in winner:
        winner.append(k)

    for i in winner:
      print(i)    

  def my_win(self , my_ticket):
    i=0
    while True:
      k=choice(self.t)
      print(f"we hape the tikcket {k}")
      if(k==my_ticket):
        break
      else:
        i+=1
        continue
    print(f"it tookde {i+1} to win!")