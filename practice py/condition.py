#names=["name1 admine" , "name2" , "name3 admine" , "name4" ,"name5" "name6"]
'''
names=[]
admine="admine"
if names == []:
  print("we need some users")
else:
 for name in names:
  if admine in name:
   print(f"Hello {name},would you like to see a status report?")
  else:
   print(f"hello {name}, thank you for logging again")
'''

names=["name1 admine" , "name2" , "name3 admine" , "name4" ,"name5" ,"name6"]
newnames=["name7 " , "name2" , "name8 " , "name9" , "name5" ,"name10"]

for newname in newnames :
  if newname in names:
    print(f"{newname} this user is exist before")
  else:
    print(f"{newname} welcome")
