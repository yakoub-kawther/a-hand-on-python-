person1={'name':'per1', 'lastname':'per1' , 'location':'location1'}

person2={'name':'per2', 'lastname':'per2' , 'location':'location2'}

person3={'name':'per3', 'lastname':'per3' , 'location':'location3'}

person4={'name':'per4', 'lastname':'per4' , 'location':'location4'}

allpersons=[person1 , person2 , person3 , person4]

for person in allpersons:
  print(f" name is {person['name']} ")
  print(f" last name is {person['lastname']} ")
  print(f" location is {person['location']} ")

  