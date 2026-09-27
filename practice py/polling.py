favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

lst=['jen' , 'sarah' , 'edward' , 'phil' , 'ken']

for name in lst :
 if name  in favorite_languages.keys():
  print(f"thank you {name} for taking the poll , i see you like {favorite_languages[name].title()} ")
 else:
  print("you have to take the poll")

