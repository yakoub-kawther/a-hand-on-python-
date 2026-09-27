cat={'name':'kitty', 'owner':'kawther'}
dog={'name':'jack', 'owner':'aymen'}
caw={'name':'mowe', 'owner':'fadila'}
chiken={'name':'jaja', 'owner':'unknown'}

animals=[cat , dog , caw , chiken]

for animal in animals:
  print("Animal's info:")
  print(f"Name: {animal['name'].title()}")
  print(f"Owner: {animal['owner'].title()}")
  print()