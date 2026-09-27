guests=["israa","yousra","ikram","marwa","ibtihel"]
newlist=[]

for guest in guests :  #we used a dirent varible here to definr loop to avoid error
  print(f"welcome to my party {guest}")

guests[0]='israa2'

for guest in guests :
  print(f"welcome to my party {guest}")

guests.insert(0,"douaa")
guests.insert(4,"louli")
guests.append("lola")
print(f"{guests}")


while guests:
  guest =guests.pop()
  if guest=="douaa" or guest=="marwa":
    newlist.append(guest)

guests=newlist[::-1]
 

print(f"you are inveted {guests}")


del guests[0]
del guests[0]

print(guests)



  


