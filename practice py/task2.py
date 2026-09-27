v=["Silicon Valley","Paris","Cairo","Athens","Tokyo"]
#print(sorted(v))
#print(v)
#v.reverse()
#print(v)
v.sort()
print(v)
v.sort(reverse=True)
print(v)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("the first three items of list are : ")
for item in players[:3]:
  print(item)
print("the middle three items of list are : ")
for item in players[int(len(players)/2)]:
  print(item)
print("the last three items of list are : ")
for item in players[-3:]:
  print(item)