
#functions nad lists 
def findeit (name , item):
  if name in item:
    return name.capitalize() + " is found"
  else:
    return name.capitalize() + " is not found"
  
myitems = {
  "one" : [1 , 2 , 3],
  "two" : 2,
  "three" : 3
}

print(findeit("kawther" , myitems))