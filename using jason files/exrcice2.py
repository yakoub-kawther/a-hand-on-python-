import json

try:
  with open('file.json') as f:
    loaded_data=json.load(f)
    for name, number in loaded_data.items():
            print(f"Hey {name}, I know your favorite number! It's {number}!")
except FileExistsError:
  name = input("what' your name")
  number=input("what's your fav number") 
  data={name:number}
  with open('file.json' ,'w') as f:
    json.dump(data, f)